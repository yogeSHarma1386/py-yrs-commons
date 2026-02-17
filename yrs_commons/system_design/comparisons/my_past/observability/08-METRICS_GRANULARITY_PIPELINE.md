# Metrics Granularity Pipeline: What Gets Lost and Why

When building a platform product around observability, one of the least visible but most consequential decisions is understanding how **metric fidelity degrades** as data moves through the pipeline. Each layer in the observability stack was designed with different trade-offs, and the result is a progressive narrowing of what you can query at the end.

This document traces a single metric observation from application code to dashboard query, showing exactly what information survives at each stage, what gets dropped, and -- critically -- **why each layer made that design choice**.

---

## The Pipeline at a Glance

```
Your Application Code
    │
    │  "I observed a latency of 372ms"
    │
    ▼
┌───────────────────────────────────┐
│  Layer 1: Metrics Facade          │  Micrometer / OTel SDK
│  In-process aggregation           │
│  Tracks: count, sum, max          │
│  LOST: min                        │
└──────────────┬────────────────────┘
               │
               │  Serialized to OTLP protobuf
               │
               ▼
┌───────────────────────────────────┐
│  Layer 2: Wire Protocol (OTLP)    │  HistogramDataPoint
│  Carries: count, sum, [buckets]   │
│  Optional: min, max               │
│  LOST: max (if cumulative)        │
└──────────────┬────────────────────┘
               │
               │  HTTP/gRPC to backend
               │
               ▼
┌───────────────────────────────────┐
│  Layer 3: Backend Storage         │  VictoriaMetrics / Prometheus
│  Stores: _count, _sum, _bucket   │
│  LOST: min, max (no storage slot) │
└──────────────┬────────────────────┘
               │
               │  PromQL / MetricsQL
               │
               ▼
┌───────────────────────────────────┐
│  Layer 4: Query Layer             │  Groundcover / Grafana
│  Can compute: rate, avg, p95      │
│  CANNOT compute: exact min/max    │
└───────────────────────────────────┘
```

---

## Layer-by-Layer Analysis

### Layer 1: Metrics Facade (Micrometer / OTel SDK)

**What it does:** Aggregates raw observations in-process before export.

**What it tracks:**

| Micrometer Type | Fields Held In-Process | Used For |
|---|---|---|
| `DistributionSummary` | count, totalAmount, max | Counts, byte sizes |
| `Timer` | count, totalTime, max | Latency |
| `Counter` | monotonic sum | Error counts |

**What's lost: `min`**

Micrometer's `DistributionSummary` and `Timer` track max but deliberately **do not track min**.

**Why min was dropped -- the design reasoning:**

1. **Min doesn't compose across instances.** If pod-A sees min=5ms and pod-B sees min=50ms, the fleet min is 5ms. But time-series backends work with `rate()` -- you compute rates from counters over time. There is no meaningful "rate of min." Min is a point statistic that doesn't participate in time-series algebra.

2. **Min doesn't compose across time windows.** If window-1 has min=5ms and window-2 has min=3ms, the combined min is 3ms. But if you're aggregating over a dashboard time range, you'd need every raw data point to recompute the true min. Storing the min-per-window and then taking `min_over_time()` gives you the smallest window-min, which is close but not identical to the true global min.

3. **Min is rarely actionable.** SLOs are defined as "X% of requests under Y threshold" (p95 < 200ms), not "the fastest request was at least Z." You almost never alert on min.

**Real-life scenario -- what you lose:**

```
Batch processor records: recordCount(1), recordCount(50), recordCount(3), recordCount(200)

With min:    count=4, sum=254, min=1, max=200
             → Alert: "min batch < 2, feeder is fragmenting"

Without min: count=4, sum=254, max=200
             → Cannot detect the anomalously small batch
```

**Workaround:** Enable histogram buckets. `histogram_quantile(0.0, ...)` approximates min at bucket-boundary granularity.

---

### Layer 2: Wire Protocol (OTLP)

**What it carries:** The OTLP `HistogramDataPoint` protobuf definition:

```protobuf
message HistogramDataPoint {
  fixed64 count = 4;                    // always present
  optional double sum = 5;              // always present
  repeated fixed64 bucket_counts = 6;   // if histogram enabled
  repeated double explicit_bounds = 7;  // if histogram enabled
  optional double min = 11;             // OPTIONAL
  optional double max = 12;             // OPTIONAL
}
```

Source: [opentelemetry-proto/metrics.proto](https://github.com/open-telemetry/opentelemetry-proto/blob/main/opentelemetry/proto/metrics/v1/metrics.proto)

**What's lost: `max` (with cumulative temporality)**

Micrometer's `OtlpMeterRegistry` **only sets max with delta temporality**. From the official docs:

> `max` on the Histogram data point is supported only in delta aggregation temporality. This is because the values represented by cumulative min and max stabilize as more events are recorded and are less useful when recorded over application's lifecycle.

Source: [docs.micrometer.io/micrometer/reference/implementations/otlp.html](https://docs.micrometer.io/micrometer/reference/implementations/otlp.html)

**Why max is dropped with cumulative -- the design reasoning:**

Cumulative means "since application start." Once a spike of 5000ms happens at 2 AM on day 1:

```
Day 1 02:00  → cumulative max = 5000ms  (the spike)
Day 1 02:01  → cumulative max = 5000ms  (can never decrease)
Day 1 14:00  → cumulative max = 5000ms  (still that one spike)
Day 30       → cumulative max = 5000ms  (forever, useless)
```

A cumulative max is a high-water mark that only increases. After the first outlier, it's meaningless forever. You can never tell:
- When the spike happened
- Whether it resolved
- What the current worst-case is

Delta temporality solves this (each export window has its own max), but some backends don't support delta.

**Real-life scenario -- what you lose:**

```
API latency monitoring:

With delta max:     "Worst-case latency in the last minute was 5000ms"
                    → Spike visible at 2:00 AM, resolved by 2:01 AM

With cumulative:    "Worst-case latency since app start was 5000ms"
                    → Spike happened... sometime. Maybe months ago. Who knows.
```

**Workaround:** Use histogram buckets + `histogram_quantile(0.99, rate(metric_bucket[1m]))` for approximate worst-case per window.

---

### Layer 3: Backend Storage (VictoriaMetrics / Prometheus)

**What happens:** OTLP histograms are decomposed into Prometheus-compatible time series:

```
my_latency_count                      → 4
my_latency_sum                        → 5148.0
my_latency_bucket{le="10"}            → 0
my_latency_bucket{le="100"}           → 3
my_latency_bucket{le="500"}           → 3
my_latency_bucket{le="1000"}          → 4
my_latency_bucket{le="+Inf"}          → 4
```

**What's lost: min and max (even if they were on the wire)**

Two independent reasons:

**Reason 1: VictoriaMetrics' OTLP parser ignores fields 11 and 12.**

From the VictoriaMetrics source code:

```go
// lib/protoparser/opentelemetry/pb/pb.go
type HistogramDataPoint struct {
    Attributes     []*KeyValue
    TimeUnixNano   uint64
    Count          uint64
    Sum            *float64
    BucketCounts   []uint64
    ExplicitBounds []float64
    Flags          uint32
    // No Min or Max fields — protobuf fields 11 and 12 are silently discarded
}
```

Source: [VictoriaMetrics/VictoriaMetrics pb.go](https://github.com/VictoriaMetrics/VictoriaMetrics/blob/master/lib/protoparser/opentelemetry/pb/pb.go)

**Reason 2: The Prometheus histogram data model has no slot for min/max.**

A Prometheus histogram consists of exactly three series suffixes: `_count`, `_sum`, `_bucket{le="..."}`. There is no `_min` or `_max`.

Source: [prometheus.io/docs/practices/histograms](https://prometheus.io/docs/practices/histograms/)

**Why the Prometheus ecosystem dropped min/max -- the design reasoning:**

1. **Histograms replace min/max with something better.** If you have bucket boundaries `[10, 50, 100, 500, 1000]`, you can compute any quantile (p50, p95, p99, p99.9) via `histogram_quantile()`. A single exact-max number is less useful than an entire distribution.

2. **Prometheus is built for aggregation across instances.** `min` and `max` from individual pods can't be meaningfully combined with `sum()` or `avg()` across a fleet. But bucket counts _can_ be summed: `sum(rate(metric_bucket[5m])) by (le)` gives you the fleet-wide distribution.

3. **Storage efficiency.** Each additional field per metric costs storage. `_min` and `_max` would add two time series per metric for marginal value, when buckets already provide distributional information.

**Real-life scenario -- what you lose:**

```
OTLP sends: count=4, sum=5148, min=48, max=5000, buckets=[0,3,0,0,1]
                                                   boundaries=[10,100,500,1000]

VictoriaMetrics stores:
  _count = 4          ✅
  _sum = 5148         ✅
  _bucket{le="100"}   ✅
  min = 48            ❌ silently dropped
  max = 5000          ❌ silently dropped

You can query:
  histogram_quantile(0.99, ...) → 1000  (bucket boundary, not exact 5000)
  rate(_sum) / rate(_count)    → 1287   (average)

You CANNOT query:
  "exact max was 5000ms"
  "exact min was 48ms"
```

---

### Layer 4: Query Layer (PromQL / MetricsQL)

**What you CAN do:**

```promql
-- Request rate
rate(my_latency_count[5m])

-- Average latency
rate(my_latency_sum[5m]) / rate(my_latency_count[5m])

-- p95 latency (requires histogram buckets)
histogram_quantile(0.95, rate(my_latency_bucket[5m]))

-- p99 latency
histogram_quantile(0.99, rate(my_latency_bucket[5m]))

-- Approximate max (highest occupied bucket boundary)
histogram_quantile(1.0, rate(my_latency_bucket[5m]))

-- Approximate min (lowest occupied bucket boundary)
histogram_quantile(0.0, rate(my_latency_bucket[5m]))
```

**What the min()/max() functions ACTUALLY do in PromQL:**

```promql
-- This does NOT give you "the smallest observation in the distribution"
-- It gives you "which pod had the lowest _count value"
min(rate(my_latency_count[5m]))

-- This does NOT give you "the largest latency observed"
-- It gives you "which pod had the highest _sum value"
max(rate(my_latency_sum[5m]))
```

PromQL's `min()` and `max()` operate on **time series values** (across label dimensions), not on individual observations within a distribution. This is the #1 source of confusion.

---

## The Complete Fidelity Matrix

### What survives at each stage

| Field | New Relic (StatisticSet) | Micrometer (in-process) | OTLP (cumulative) | OTLP (delta) | VictoriaMetrics | PromQL |
|---|---|---|---|---|---|---|
| **count** | count | count | count | count | `_count` | `rate(_count)` |
| **sum** | sum | totalAmount | sum | sum | `_sum` | `rate(_sum)` |
| **min** | min | -- | -- | -- | -- | `≈ histogram_quantile(0)` |
| **max** | max | max | -- | max | -- | `≈ histogram_quantile(1)` |
| **buckets** | -- | if enabled | if enabled | if enabled | `_bucket{le}` | `histogram_quantile()` |
| **time window** | interval | step | timestamps | timestamps | scrape interval | range selector |
| **avg** | sum/count | totalAmount/count | sum/count | sum/count | `_sum/_count` | `rate(_sum)/rate(_count)` |
| **percentiles** | backend-computed | if histogram | via buckets | via buckets | via buckets | `histogram_quantile(0.95)` |

### What's lost at each transition

| Transition | Lost | Why | Workaround |
|---|---|---|---|
| NR → Micrometer | `min` | Doesn't compose across instances or with rate() math | Histogram buckets: `quantile(0.0)` |
| Micrometer → OTLP (cumul.) | `max` | Cumulative max only increases, becomes useless | Use delta temporality (if backend supports) |
| OTLP → VictoriaMetrics | `min`, `max` | Parser ignores fields; no Prometheus storage slot | Histogram buckets: `quantile(0.0/1.0)` |

---

## Real-World Scenario: Queries You Can Run at Each Pipeline Level

Let's trace a **single, concrete metric** through all four layers. The scenario:

> **E-commerce checkout API.** You record latency for every checkout request. Over a 1-minute window, 6 requests are observed with latencies: **12ms, 45ms, 78ms, 150ms, 320ms, 4200ms** (the last one is a database timeout).

Raw observations: `[12, 45, 78, 150, 320, 4200]`

---

### Level 0: New Relic (the "before" baseline)

NR receives a CloudWatch-style `StatisticSet`:

```
count=6, sum=4805, min=12, max=4200, time_window=60s
```

**Queries you CAN run in NRQL:**

```sql
-- 1. Average checkout latency
SELECT average(checkout_latency) FROM Metric WHERE service='checkout-api'
-- Result: 800.8ms

-- 2. Worst-case latency (exact)
SELECT max(checkout_latency) FROM Metric WHERE service='checkout-api'
-- Result: 4200ms  ← EXACT

-- 3. Best-case latency (exact)
SELECT min(checkout_latency) FROM Metric WHERE service='checkout-api'
-- Result: 12ms  ← EXACT

-- 4. Alert: "any window where max > 3000ms"
SELECT max(checkout_latency) FROM Metric
WHERE max > 3000 SINCE 1 hour ago
-- Result: fires, because max=4200 > 3000

-- 5. Alert: "feeder anomaly — min dropped below expected"
SELECT min(checkout_latency) FROM Metric
WHERE min < 5 SINCE 1 hour ago
-- Result: does NOT fire (min=12, which is > 5)

-- 6. Throughput
SELECT rate(count(checkout_latency), 1 minute) FROM Metric
-- Result: 6 req/min
```

**Supported:** count, sum, min, max, avg, rate — all exact.

---

### Level 1: Micrometer (in-process)

Micrometer `Timer` holds after the 6 observations:

```
count=6, totalTime=4805ms, max=4200ms
(no min tracked)
```

**Queries you CAN run via Micrometer API (in-process Java code):**

```java
Timer timer = registry.timer("checkout_latency", tags);

// 1. Count of observations
timer.count();          // → 6

// 2. Total accumulated time
timer.totalTime(TimeUnit.MILLISECONDS);  // → 4805.0

// 3. Average (derived)
timer.mean(TimeUnit.MILLISECONDS);       // → 800.8

// 4. Max since last publish
timer.max(TimeUnit.MILLISECONDS);        // → 4200.0  ← STILL AVAILABLE

// 5. Percentiles (if publishPercentileHistogram=true)
// Micrometer computes these client-side from histogram buckets
timer.takeSnapshot().percentileValues();
// → [p50=78ms, p95=320ms, p99=4200ms]  (bucket approximations)
```

**Queries you CANNOT run:**

```java
// ❌ No min API exists
timer.min(TimeUnit.MILLISECONDS);   // DOES NOT EXIST

// ❌ No median API without histogram enabled
timer.median();                      // DOES NOT EXIST without histogram
```

**Supported:** count, sum, avg, max, percentiles (with histogram). **Lost:** min.

---

### Level 2: OTLP Wire (cumulative temporality)

What Micrometer serializes to the OTLP `HistogramDataPoint` protobuf:

```
HistogramDataPoint {
  count: 6
  sum: 4805.0
  bucket_counts: [0, 1, 2, 3, 4, 5, 6]    // if histogram enabled
  explicit_bounds: [5, 10, 25, 50, 75, 100, 250, 500, 1000, 5000, 10000, 30000]
  min: NOT SET                              // Micrometer never sets min
  max: NOT SET                              // Not set with cumulative temporality
}
```

**If you could intercept and query the OTLP data (e.g., via OTel Collector debug exporter):**

```yaml
# collector-config.yaml debug output
Metric: checkout_latency
  Type: Histogram
  DataPoints:
    - Count: 6
      Sum: 4805
      BucketCounts: [0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0]
      ExplicitBounds: [5, 10, 25, 50, 75, 100, 250, 500, 1000, 5000, ...]
      Min: <not present>        # ← gone at Layer 1
      Max: <not present>        # ← gone at Layer 2 (cumulative)
```

**What a delta-capable backend (Datadog, NR OTLP) could compute from this:**

```
count:   6         ✅
sum:     4805      ✅
avg:     800.8     ✅ (sum/count)
p95:     ~1000     ✅ (from bucket interpolation)
p99:     ~5000     ✅ (from bucket interpolation)
min:     ❌        (not on wire)
max:     ❌        (not on wire with cumulative)
```

**Supported:** count, sum, avg, bucket distribution, percentile approximation. **Lost:** min (Layer 1), max (Layer 2).

---

### Level 3: VictoriaMetrics / Prometheus Storage

VictoriaMetrics decomposes the OTLP histogram into individual Prometheus time series:

```
checkout_latency_count                            6
checkout_latency_sum                              4805
checkout_latency_bucket{le="5"}                   0
checkout_latency_bucket{le="10"}                  0
checkout_latency_bucket{le="25"}                  1
checkout_latency_bucket{le="50"}                  2
checkout_latency_bucket{le="75"}                  2
checkout_latency_bucket{le="100"}                 3
checkout_latency_bucket{le="250"}                 3
checkout_latency_bucket{le="500"}                 4
checkout_latency_bucket{le="1000"}                4
checkout_latency_bucket{le="5000"}                5
checkout_latency_bucket{le="10000"}               6
checkout_latency_bucket{le="+Inf"}                6
```

No `checkout_latency_min` or `checkout_latency_max` series exist. Not because they weren't useful, but because the storage format has no place for them.

**Supported at storage level:** count, sum, cumulative bucket counts. **Lost:** min, max (no storage slot).

---

### Level 4: PromQL / MetricsQL in Groundcover

**Queries you CAN run:**

```promql
-- 1. Request rate (requests per second)
rate(checkout_latency_count[5m])
-- Result: 0.1 rps (6 requests / 60 seconds)

-- 2. Average latency
rate(checkout_latency_sum[5m]) / rate(checkout_latency_count[5m])
-- Result: 800.8ms  ✅

-- 3. p50 (median) latency
histogram_quantile(0.50, rate(checkout_latency_bucket[5m]))
-- Result: ~75ms  ✅ (bucket boundary approximation; true median is ~61ms)

-- 4. p95 latency
histogram_quantile(0.95, rate(checkout_latency_bucket[5m]))
-- Result: ~5000ms  ✅ (the 4200ms observation lands in the ≤5000 bucket)

-- 5. p99 latency
histogram_quantile(0.99, rate(checkout_latency_bucket[5m]))
-- Result: ~5000ms  ✅

-- 6. Approximate max (highest occupied bucket)
histogram_quantile(1.0, rate(checkout_latency_bucket[5m]))
-- Result: 10000  ⚠️ (bucket boundary, NOT exact 4200)

-- 7. Approximate min (lowest occupied bucket)
histogram_quantile(0.0, rate(checkout_latency_bucket[5m]))
-- Result: 25  ⚠️ (bucket boundary, NOT exact 12)

-- 8. Error budget: "% of requests under 500ms SLO"
sum(rate(checkout_latency_bucket{le="500"}[5m]))
  /
sum(rate(checkout_latency_count[5m]))
-- Result: 0.667 = 66.7%  ✅ (4 of 6 requests ≤ 500ms)

-- 9. Fleet-wide p95 across all pods
histogram_quantile(0.95,
  sum(rate(checkout_latency_bucket[5m])) by (le)
)
-- Result: aggregated p95 across all pods  ✅

-- 10. Rate of change (is latency getting worse?)
deriv(
  rate(checkout_latency_sum[5m]) / rate(checkout_latency_count[5m])
[30m])
-- Result: positive = degrading, negative = improving  ✅
```

**Queries you CANNOT run (and the NR equivalent you're losing):**

```promql
-- ❌ "What was the exact worst-case checkout latency?"
--    NR equivalent: SELECT max(checkout_latency) → 4200ms
--    PromQL:        histogram_quantile(1.0, ...) → 10000 (bucket boundary, not 4200)
--    Gap: 10000 vs 4200 — bucket tells you "somewhere in (5000, 10000]", not the exact value

-- ❌ "What was the exact fastest checkout?"
--    NR equivalent: SELECT min(checkout_latency) → 12ms
--    PromQL:        histogram_quantile(0.0, ...) → 25 (bucket boundary, not 12)
--    Gap: 25 vs 12 — bucket tells you "somewhere in (10, 25]", not the exact value

-- ❌ "Alert when any single request exceeds 5000ms"
--    NR equivalent: SELECT max(checkout_latency) WHERE max > 5000
--    PromQL:        Cannot detect this. The 4200ms observation falls in the ≤5000 bucket,
--                   so histogram_quantile sees it as "within bounds." A true 5001ms request
--                   would land in the next bucket, but you'd only know "it was in (5000, 10000]."

-- ❌ "Show me the exact distribution of all observations"
--    NR equivalent: SELECT histogram(checkout_latency) → exact values plotted
--    PromQL:        You see bucket counts, not individual values. You know 1 request was
--                   in (10,25], 1 in (25,50], etc. — but not the exact 12, 45, 78...
```

---

### Side-by-Side: One Scenario, All Layers

| Query Intent | NR (NRQL) | Micrometer (Java) | OTLP (wire) | Groundcover (PromQL) |
|---|---|---|---|---|
| **Count** | `count(metric)` → 6 | `timer.count()` → 6 | `count: 6` | `rate(_count[5m])` → 0.1/s |
| **Sum** | `sum(metric)` → 4805 | `timer.totalTime()` → 4805 | `sum: 4805` | `rate(_sum[5m])` → 80.1/s |
| **Average** | `average(metric)` → 800.8 | `timer.mean()` → 800.8 | sum/count → 800.8 | `rate(_sum)/rate(_count)` → 800.8 |
| **Exact max** | `max(metric)` → **4200** | `timer.max()` → **4200** | not set (cumul.) | **Cannot** |
| **Approx max** | n/a | n/a | n/a | `histogram_quantile(1.0)` → **10000** |
| **Exact min** | `min(metric)` → **12** | **Cannot** | **Cannot** | **Cannot** |
| **Approx min** | n/a | n/a | n/a | `histogram_quantile(0.0)` → **25** |
| **p50** | `percentile(metric, 50)` → ~61 | snapshot → ~75 | via buckets → ~75 | `histogram_quantile(0.50)` → ~75 |
| **p95** | `percentile(metric, 95)` → ~4200 | snapshot → ~5000 | via buckets → ~5000 | `histogram_quantile(0.95)` → ~5000 |
| **SLO % under 500ms** | `percentage(... < 500)` → 66.7% | **Cannot** (no query API) | via buckets | `_bucket{le="500"}/_count` → 66.7% |
| **Fleet-wide p95** | `percentile(... FACET pod)` | **Cannot** (single-instance) | **Cannot** (single-instance) | `histogram_quantile(0.95, sum by (le))` → **Fleet p95** |
| **Rate of change** | `derivative(avg)` | **Cannot** | **Cannot** | `deriv(rate(_sum)/rate(_count))` |

Key takeaway from the table: **NR wins on exactness (min, max), PromQL wins on composability (fleet-wide aggregation, rate math, SLO budgets).** The pipeline doesn't just lose information -- it also gains capabilities that NR's per-StatisticSet model can't do.

---

## Platform Engineering Thought Process

When designing an observability platform product, these are the trade-off axes at each layer:

### 1. Exactness vs. Composability

**Exact values** (min=48ms, max=5000ms) are precise but don't combine.

```
Pod-A: max=500ms,  Pod-B: max=200ms
Fleet max = max(500, 200) = 500ms     ← only works with min/max aggregator

Pod-A: bucket{le=500}=95,  Pod-B: bucket{le=500}=180
Fleet: bucket{le=500} = 275           ← composable via sum()
Fleet p95 = histogram_quantile(0.95, sum(rate(bucket[5m])) by (le))
```

The Prometheus ecosystem chose composability. The entire `rate()` + `sum() by (le)` + `histogram_quantile()` pipeline works because bucket counts are additive. Min and max are not.

### 2. Per-Window Precision vs. Cumulative Simplicity

**Delta temporality** gives per-window stats (max in _this_ minute). **Cumulative** gives monotonically increasing counters.

```
Delta:       Richer data, but requires stateful backends that can diff
Cumulative:  Simpler, works with Prometheus, but loses max
```

VictoriaMetrics (Groundcover's backend) chose cumulative-only for histograms, which locks out delta-exclusive features like per-window max.

### 3. Wire Fidelity vs. Storage Cost

OTLP carries `optional min`, `optional max` on every `HistogramDataPoint`. If you have 10,000 metrics exported every 60s, that's 10,000 extra min + max values per export.

```
With min/max:    10,000 metrics × 2 extra fields × 1440 exports/day = 28.8M extra data points/day
Without:         Zero additional storage
```

Prometheus-family backends traded those two fields for lower cardinality and simpler storage.

### 4. The Bucket Compromise

Histogram buckets are the "good enough" answer that replaced exact min/max:

```
Exact min/max:     min=48ms, max=5000ms (precise, not composable)
Bucket approx:     quantile(0.0) ≈ 10ms bucket, quantile(1.0) ≈ 1000ms bucket
                   (imprecise, fully composable)
```

The trade-off: bucket boundaries determine approximation quality. With Micrometer's default Timer buckets (roughly 1ms to 30s with ~70 buckets), you get good resolution. With coarse buckets (only 5 boundaries), approximations can be far from truth.

**Platform decision:** Enable `percentile-histogram=true` and accept the cardinality cost of ~70 extra bucket series per metric, in exchange for `histogram_quantile()` capability across the full range.

---

## Practical Implications for Your Product

### What to tell your team

1. **"We lose exact min/max in the Groundcover migration."** Be upfront. If anyone has NR dashboards showing min, those panels will either disappear or show approximate values via `histogram_quantile(0)`.

2. **"p95/p99 are the replacement for max."** In most cases, p99 is more useful than max anyway. Max is dominated by a single outlier; p99 tells you what 99% of your users actually experience.

3. **"Enable histogram buckets."** Without them, you only get count/sum/average. With them, you get full percentile support. The cardinality cost is ~70 series per metric.

4. **"Average is always available."** `rate(sum) / rate(count)` works at every stage of the pipeline with zero configuration.

### Decision checklist for new metrics

| Question | If Yes | If No |
|---|---|---|
| Do I need percentiles (p50/p95/p99)? | Enable `percentile-histogram=true` | Count + sum + avg is enough |
| Do I need exact min/max? | Stay on New Relic or use a delta-capable backend | Approximate via `histogram_quantile(0/1)` |
| Is this metric high-cardinality (many tag combos)? | Skip histogram, use Counter | DistributionSummary + histogram is fine |
| Do I alert on "worst case per window"? | Use p99 instead of max | No change needed |

---

## Summary: The Information Hierarchy

```
Most Information                                          Least Information
────────────────────────────────────────────────────────────────────────────
NR StatisticSet   >   Micrometer   >   OTLP (delta)   >   OTLP (cumul.)   >   Prometheus/VM
count ✓               count ✓          count ✓             count ✓              _count ✓
sum ✓                 sum ✓            sum ✓               sum ✓                _sum ✓
min ✓                 ✗                ✗                   ✗                    ✗
max ✓                 max ✓            max ✓               ✗                    ✗
time window ✓         step ✓           timestamps ✓        timestamps ✓         scrape ✓
                      buckets*         buckets*            buckets*             _bucket{le}*

* = only if histogram is enabled
```

Each arrow represents a deliberate design decision:
- **NR → Micrometer:** min dropped (not composable across instances)
- **Micrometer → OTLP cumul.:** max dropped (cumulative max is meaningless)
- **OTLP → Prometheus/VM:** min/max dropped (no storage slot, not composable)

The Prometheus ecosystem's answer: **replace exact point statistics with distributional information (histogram buckets)**. It's less precise for a single data point but more powerful for fleet-wide, time-range, and cross-service queries.

---

## References

- [OTLP HistogramDataPoint protobuf spec](https://github.com/open-telemetry/opentelemetry-proto/blob/main/opentelemetry/proto/metrics/v1/metrics.proto) -- fields 11 (min) and 12 (max) are `optional`
- [Micrometer OTLP docs](https://docs.micrometer.io/micrometer/reference/implementations/otlp.html) -- "max on the Histogram data point is supported only in delta aggregation temporality"
- [VictoriaMetrics OTLP parser](https://github.com/VictoriaMetrics/VictoriaMetrics/blob/master/lib/protoparser/opentelemetry/pb/pb.go) -- `HistogramDataPoint` struct has no min/max fields
- [VictoriaMetrics OTLP limitations](https://docs.victoriametrics.com/guides/getting-started-with-opentelemetry) -- "supports only AggregationTemporalityCumulative for histogram"
- [Prometheus histogram practices](https://prometheus.io/docs/practices/histograms/) -- `_count`, `_sum`, `_bucket{le}` only
- [OTel-to-Prometheus compatibility spec](https://opentelemetry.io/docs/specs/otel/compatibility/prometheus_and_openmetrics) -- conversion rules
