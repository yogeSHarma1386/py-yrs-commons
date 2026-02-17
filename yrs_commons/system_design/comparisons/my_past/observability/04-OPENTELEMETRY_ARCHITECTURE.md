# OpenTelemetry Architecture and Advanced Concepts

This guide covers the architecture, instrumentation methods, context propagation, sampling, and best practices for OpenTelemetry.

## 🏗️ OpenTelemetry Architecture

### Components Overview

```
┌─────────────────┐
│  Application    │
│  (Your Code)    │
└────────┬────────┘
         │
         ├─→ Automatic Instrumentation (Java Agent)
         │   - Captures HTTP, DB, etc.
         │
         └─→ Manual Instrumentation (SDK/API)
             - Custom metrics, spans, logs
         │
         ▼
┌────────────────────────┐
│ OpenTelemetry SDK      │
│ - Creates telemetry    │
│ - Batching             │
│ - Resource detection   │
└───────────┬────────────┘
            │
            ▼
┌────────────────────────┐
│  Exporters             │
│  - OTLP (default)      │
│  - Prometheus          │
│  - Jaeger              │
└───────────┬────────────┘
            │
            ▼
┌────────────────────────┐
│ OpenTelemetry Collector│ (Optional but recommended)
│ - Receives telemetry   │
│ - Processes/filters    │
│ - Routes to backends   │
└───────────┬────────────┘
            │
            ▼
┌────────────────────────┐
│   Backend Systems      │
│   - Groundcover        │
│   - Prometheus         │
│   - Grafana            │
│   - Datadog            │
└────────────────────────┘
```

### In This Codebase

```yaml
# docker-compose.yml shows the architecture:

app (Java application)
  ↓ [OTLP HTTP]
  ↓ http://collector:4318/v1/metrics
  ↓ http://collector:4318/v1/traces
  ↓ http://collector:4318/v1/logs
  ↓
collector (OpenTelemetry Collector)
  ↓ [OTLP HTTP + Auth]
  ↓ https://i0ps1f.platform.grcv.io
  ↓
Groundcover (Backend)
```

---

## 🔄 Context Propagation

### What is Context Propagation?

Context propagation enables distributed tracing by passing trace information between services.

**Key Components:**
- **Context**: Object containing trace_id, span_id, trace_flags, trace_state
- **Propagation**: Mechanism to serialize/deserialize context across process boundaries

### W3C Trace Context Standard

OpenTelemetry uses the W3C TraceContext specification by default.

**HTTP Headers:**
```http
traceparent: 00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01
tracestate: vendor1=value1,vendor2=value2
```

**Format breakdown:**
```
traceparent: version-trace_id-parent_span_id-trace_flags
             00     -4bf92f...-00f067...   -01

version:         00 (current version)
trace_id:        128-bit unique identifier (32 hex chars)
parent_span_id:  64-bit span identifier (16 hex chars)
trace_flags:     01 = sampled, 00 = not sampled
```

### How It Works

```
Service A (Frontend)
  ├─ Creates trace_id: abc123
  ├─ Creates span_id: span001
  ├─ Calls Service B with headers:
  │    traceparent: 00-abc123-span001-01
  │
Service B (Backend)
  ├─ Reads headers
  ├─ Uses same trace_id: abc123
  ├─ Creates new span_id: span002
  ├─ Sets parent_span_id: span001
  └─ Result: Spans linked in same trace!
```

### Automatic vs Manual Propagation

**Automatic** (This Codebase):
- OpenTelemetry Java Agent automatically propagates context
- No code changes needed for HTTP, gRPC, Kafka, etc.

**Manual** (When needed):
```java
// Extract context from incoming request
Context extractedContext = propagator.extract(
    Context.current(),
    httpHeaders,
    getter
);

// Inject context into outgoing request
propagator.inject(
    Context.current(),
    httpHeaders,
    setter
);
```

---

## 🎲 Sampling Strategies

### Why Sample?

**Without sampling:**
- 1 million requests/sec = 86.4 billion traces/day
- Massive storage costs
- Most traces are similar (healthy traffic)

**With 1% sampling:**
- 864 million traces/day
- 99% cost reduction
- Still representative of traffic patterns

### Head Sampling (Early Decision)

**Definition**: Decision made at trace creation time, before seeing the full trace.

**Types:**

1. **AlwaysOn**: Sample everything (100%)
```java
// Default in development
Sampler.alwaysOn()
```

2. **AlwaysOff**: Sample nothing (0%)
```java
Sampler.alwaysOff()
```

3. **TraceIdRatioBased**: Consistent probability sampling
```java
// Sample 5% of traces
Sampler.traceIdRatioBased(0.05)
```

4. **ParentBased**: Use parent's sampling decision
```java
// Follow parent's decision, or use fallback
Sampler.parentBased(Sampler.traceIdRatioBased(0.1))
```

**Advantages:**
- Simple and efficient
- Low computational overhead
- Deterministic based on trace_id

**Limitations:**
- Can't make intelligent decisions (e.g., always sample errors)
- Fixed sampling rate

### Tail Sampling (Late Decision)

**Definition**: Decision made after seeing the complete trace.

**Examples:**

1. **Sample all errors:**
```
IF any span has status=ERROR THEN sample
```

2. **Sample slow requests:**
```
IF trace duration > 1 second THEN sample
```

3. **Sample by attributes:**
```
IF clientId = "premium-customer" THEN sample
ELSE sample 1%
```

**Advantages:**
- Intelligent sampling based on full trace data
- Capture all errors regardless of volume
- Different rates for different scenarios

**Disadvantages:**
- Complex to implement
- Requires stateful collector
- Must buffer all trace data temporarily
- Higher resource usage

### This Codebase Sampling

By default, this codebase uses **ParentBased(AlwaysOn)** - everything is sampled.

To change sampling:
```bash
# Environment variable
OTEL_TRACES_SAMPLER=traceidratio
OTEL_TRACES_SAMPLER_ARG=0.1  # 10% sampling
```

Or in code:
```java
SdkTracerProvider.builder()
    .setSampler(Sampler.traceIdRatioBased(0.05))  // 5%
    .build()
```

---

## 🔧 Instrumentation Methods

### 1. Automatic Instrumentation (Zero-Code)

**What**: Captures telemetry without code changes using agents.

**This Codebase Uses:**
```dockerfile
# Dockerfile
ENTRYPOINT java -javaagent:/opentelemetry-javaagent.jar \
    -Dotel.javaagent.extensions=/opentelemetry-javaagent-extension.jar \
    -jar /app.jar
```

**What Gets Instrumented Automatically:**
- HTTP requests/responses (Spring Boot, Servlet, etc.)
- Database calls (JDBC, JPA, Hibernate)
- Message queues (Kafka, RabbitMQ, JMS)
- gRPC, Redis, Elasticsearch, and 100+ libraries

**Benefits:**
- No code changes required
- Consistent instrumentation across libraries
- Automatically updated with new versions

**Limitations:**
- Less control over span details
- May capture too much or too little
- Limited custom attributes

### 2. Manual Instrumentation (Code-Based)

**What**: Explicitly create telemetry in your code using SDK/API.

**This Codebase Uses Manual Instrumentation For:**

**Custom Metrics:**
```java
// Controller.java:53-59
doWorkHistogram = meter
    .histogramBuilder("yrs_local_metric")
    .setDescription("Time spent doing work in milliseconds")
    .build();
```

**Custom Spans:**
```java
// Controller.java:161-191
Span span = tracer.spanBuilder("doWork").startSpan();
span.setAttribute("clientId", clientId);
span.setAttribute("sleep_time_ms", sleepTime);
// ... do work ...
span.end();
```

**Custom Attributes:**
```java
// TelemetryFilter.java:61-67
currentSpan.setAttribute("clientId", clientId);
currentSpan.setAttribute("teamId", teamId);
currentSpan.setAttribute("region", region);
```

**Benefits:**
- Full control over what's captured
- Rich custom attributes
- Business-specific metrics
- Fine-grained spans

**Limitations:**
- Requires code changes
- More maintenance
- Easy to forget to close spans

### 3. Hybrid Approach (Recommended)

Use both automatic and manual instrumentation together!

```
Automatic:
- HTTP server instrumentation (free!)
- Database instrumentation (free!)
- Library instrumentation (free!)

Manual:
- Business metrics (request.count, revenue)
- Custom spans (doWork, processPayment)
- Custom attributes (clientId, isPremium)
```

This codebase uses the hybrid approach perfectly! ✅

---

## 📦 OpenTelemetry Collector

### What is the Collector?

A vendor-agnostic proxy that receives, processes, and exports telemetry.

**Think of it as a smart router for observability data.**

### Why Use a Collector?

1. **Separation of concerns**: Application doesn't need backend credentials
2. **Preprocessing**: Filter, sample, enrich data before sending
3. **Multiple backends**: Send same data to multiple destinations
4. **Reduced load**: Batching and buffering before export
5. **Failover**: Handle backend downtime gracefully

### Collector Components

```yaml
# collector-config.yaml

receivers:      # How telemetry enters the collector
  otlp:
    protocols:
      http:
        endpoint: "0.0.0.0:4318"

processors:     # What happens to the data (optional)
  batch:        # Batch data for efficiency
  filter:       # Remove unwanted data
  attributes:   # Add/modify attributes

exporters:      # Where telemetry goes
  debug:        # Print to console
  otlphttp/groundcover:
    endpoint: https://i0ps1f.platform.grcv.io
    headers:
      apikey: ${env:GROUNDCOVER_INGESTION_KEY}

service:        # Pipeline configuration
  pipelines:
    metrics:
      receivers: [otlp]
      processors: [batch]
      exporters: [debug, otlphttp/groundcover]
    traces:
      receivers: [otlp]
      exporters: [otlphttp/groundcover]
    logs:
      receivers: [otlp]
      exporters: [otlphttp/groundcover]
```

### Collector Deployment Patterns

**1. Agent (Sidecar):**
```
App → Collector (localhost) → Backend
```
- One collector per application instance
- Low latency
- Higher resource usage

**2. Gateway (Centralized):**
```
App1 ─┐
App2 ─┼→ Collector (shared) → Backend
App3 ─┘
```
- One collector for multiple apps
- Centralized processing
- More efficient resource usage
- This codebase uses this pattern!

---

## 📋 Semantic Conventions

### What are Semantic Conventions?

Standard attribute names for common scenarios.

**Without conventions:**
```
Service A: http.url, status, method
Service B: request.url, http_status, http_method
Service C: url, response_code, verb
```
❌ Inconsistent - hard to query across services!

**With conventions:**
```
All services: http.url, http.status_code, http.method
```
✅ Consistent - easy to query!

### Common Semantic Conventions

**HTTP Attributes:**
```java
span.setAttribute("http.method", "GET");
span.setAttribute("http.url", "https://api.example.com/users");
span.setAttribute("http.status_code", 200);
span.setAttribute("http.user_agent", "Mozilla/5.0...");
```

**Database Attributes:**
```java
span.setAttribute("db.system", "postgresql");
span.setAttribute("db.name", "users_db");
span.setAttribute("db.statement", "SELECT * FROM users WHERE id = ?");
```

**Service Attributes:**
```java
resource.setAttribute("service.name", "payment-api");
resource.setAttribute("service.version", "0.3.0-SNAPSHOT");
resource.setAttribute("service.instance.id", "instance-123");
```

**Network Attributes:**
```java
span.setAttribute("net.peer.name", "api.example.com");
span.setAttribute("net.peer.port", 443);
span.setAttribute("net.transport", "ip_tcp");
```

### In This Codebase

**Semantic Conventions Used:**
```java
// TelemetryFilter.java:68-69
currentSpan.setAttribute("http.method", httpRequest.getMethod());
currentSpan.setAttribute("http.target", httpRequest.getRequestURI());
currentSpan.setAttribute("http.status_code", httpResponse.getStatus());
```

**Custom Attributes (Not Semantic Conventions):**
```java
currentSpan.setAttribute("clientId", clientId);       // Custom
currentSpan.setAttribute("teamId", teamId);           // Custom
currentSpan.setAttribute("is_premium", isPremium);    // Custom
```

---

## 🎯 Resource Attributes

### What are Resources?

Immutable metadata about the entity producing telemetry.

**Think of it as: "Who is generating this data?"**

### Automatic Resource Detection

This codebase automatically detects:
```
service.name: agent-example-app              (from env var)
service.version: 0.3.0-SNAPSHOT              (from manifest)
service.instance.id: ea06bce0699...          (auto-generated)
host.name: ea06bce06990                      (container hostname)
host.arch: aarch64                           (system architecture)
os.type: linux                               (operating system)
container.id: ea06bce0699021197bd46ca...     (docker container)
process.executable.path: /opt/java/openjdk...
telemetry.sdk.name: opentelemetry
telemetry.sdk.language: java
telemetry.sdk.version: 1.44.1
telemetry.distro.name: opentelemetry-java-instrumentation
telemetry.distro.version: 2.21.0
```

### Resource vs Attributes

| Resource | Attributes |
|----------|-----------|
| Describes the **service** | Describes the **operation** |
| Set once at startup | Set per span/metric/log |
| Same for all signals | Different per signal |
| `service.name` | `http.method` |
| `service.version` | `clientId` |
| `host.name` | `region` |

---

## 📤 Exporters

### What are Exporters?

Components that send telemetry to backends.

### Common Exporters

**1. OTLP (OpenTelemetry Protocol)** - Default ✅
```java
// Supports: gRPC and HTTP
// This codebase uses OTLP HTTP
OTEL_EXPORTER_OTLP_ENDPOINT=http://collector:4318
```

**2. Prometheus**
```java
// Pull-based metrics
// Exposes /metrics endpoint
```

**3. Jaeger**
```java
// Legacy tracing format
// Being replaced by OTLP
```

**4. Zipkin**
```java
// Legacy tracing format
// Being replaced by OTLP
```

**5. Console/Logging**
```yaml
# collector-config.yaml
exporters:
  debug:
    verbosity: detailed  # Prints to console
```

### This Codebase Configuration

```yaml
# docker-compose.yml
environment:
  OTEL_EXPORTER_OTLP_TRACES_ENDPOINT: "http://collector:4318/v1/traces"
  OTEL_EXPORTER_OTLP_METRICS_ENDPOINT: "http://collector:4318/v1/metrics"
  OTEL_EXPORTER_OTLP_LOGS_ENDPOINT: "http://collector:4318/v1/logs"

# collector-config.yaml
exporters:
  debug:
    verbosity: detailed
  otlphttp/groundcover:
    endpoint: https://i0ps1f.platform.grcv.io
    headers:
      apikey: ${env:GROUNDCOVER_INGESTION_KEY}
```

---

## ⚡ Performance Considerations

### 1. Batching

**Don't send every span immediately** - batch them!

```yaml
# collector-config.yaml
processors:
  batch:
    timeout: 10s           # Send every 10 seconds
    send_batch_size: 1024  # Or when batch reaches 1024 items
```

**Benefits:**
- Fewer network calls
- Better throughput
- Lower overhead

### 2. Sampling

Already covered above - sample to reduce data volume!

### 3. Attribute Limits

```bash
# Limit attribute sizes
OTEL_ATTRIBUTE_VALUE_LENGTH_LIMIT=4096
OTEL_ATTRIBUTE_COUNT_LIMIT=128
```

**Why?**
- Prevent accidentally storing huge values
- Control memory usage
- Limit storage costs

### 4. Async Processing

OpenTelemetry SDK processes telemetry asynchronously by default.

```java
// Span.end() is non-blocking
span.end();  // Returns immediately, export happens later
```

**Result:** Minimal impact on application latency!

### 5. Resource Detection

Resource detection happens once at startup:

```java
// Expensive operations happen only once
SdkTracerProvider.builder()
    .setResource(Resource.getDefault())  // Detects once
    .build()
```

---

## 🏆 Best Practices

### 1. Use Semantic Conventions

✅ **Good:**
```java
span.setAttribute("http.method", "GET");
span.setAttribute("http.status_code", 200);
```

❌ **Bad:**
```java
span.setAttribute("method", "GET");
span.setAttribute("status", 200);
```

### 2. Close Spans in Finally Blocks

✅ **Good:**
```java
Span span = tracer.spanBuilder("operation").startSpan();
try (Scope scope = span.makeCurrent()) {
    // Do work
} finally {
    span.end();  // Always closes
}
```

❌ **Bad:**
```java
Span span = tracer.spanBuilder("operation").startSpan();
// Do work
span.end();  // Might not be called if exception thrown!
```

### 3. Use Low-Cardinality Attributes for Metrics

✅ **Good for metrics:**
```java
// Limited values: 3 clients
attributes.put("clientId", "client1");  // client1, client2, client3

// Limited values: 2 teams
attributes.put("teamId", "teamId1");    // teamId1, teamId2
```

❌ **Bad for metrics:**
```java
// Infinite values - will explode metric cardinality!
attributes.put("userId", "user-12345");
attributes.put("requestId", "req-abc123");
```

**Use high-cardinality attributes for traces and logs instead!**

### 4. Set Service Name

```bash
# Always set service name
OTEL_SERVICE_NAME=payment-api
```

### 5. Use Resource Attributes

```bash
# Add deployment info
OTEL_RESOURCE_ATTRIBUTES=service.name=payment-api,service.version=1.0.0,deployment.environment=production
```

### 6. Enable Trace-Log Correlation

Already done in this codebase! ✅

```java
// OpenTelemetry agent automatically adds trace context to MDC
// Just use %mdc in logback pattern
```

### 7. Monitor Collector Health

```yaml
# collector-config.yaml
extensions:
  health_check:
    endpoint: "0.0.0.0:13133"  # Health check endpoint

  pprof:
    endpoint: "0.0.0.0:1777"    # Performance profiling
```

### 8. Use Collector for Production

```
Development:  App → Backend (direct)
Production:   App → Collector → Backend
```

**Benefits:**
- Buffering and retry logic
- Preprocessing and filtering
- Multiple backend support
- Security (no backend credentials in apps)

---

## 🚀 Migration Path

### Phase 1: Start with Automatic Instrumentation
```bash
# Just add the agent - instant observability!
java -javaagent:opentelemetry-javaagent.jar -jar app.jar
```

### Phase 2: Add Custom Metrics
```java
// Track business metrics
requestCounter.add(1);
revenueHistogram.record(orderTotal);
```

### Phase 3: Add Custom Spans
```java
// Trace important operations
Span span = tracer.spanBuilder("processPayment").startSpan();
```

### Phase 4: Add Custom Attributes
```java
// Enrich with business context
span.setAttribute("customerId", customerId);
span.setAttribute("paymentMethod", "credit_card");
```

### Phase 5: Deploy Collector
```yaml
# Add collector for production
app → collector → backend
```

### Phase 6: Optimize Sampling
```bash
# Reduce costs with intelligent sampling
OTEL_TRACES_SAMPLER=traceidratio
OTEL_TRACES_SAMPLER_ARG=0.05  # 5%
```

---

## 📚 Summary

**This codebase demonstrates:**
- ✅ Automatic instrumentation (Java Agent)
- ✅ Manual instrumentation (custom metrics, spans, attributes)
- ✅ OpenTelemetry Collector (with debug + groundcover exporters)
- ✅ Context propagation (automatic via agent)
- ✅ Trace-log correlation (via MDC)
- ✅ Resource attributes (automatic detection)
- ✅ Semantic conventions (http.method, http.status_code)
- ✅ Custom attributes (clientId, teamId, region)
- ✅ All three signals (metrics, traces, logs)

**Production-ready architecture with minimal code changes!** 🎯
