# Complete Guide to OpenTelemetry: Metrics, Traces, and Logs

This guide explains all metric types and observability terminologies with examples from this codebase.

## 📊 METRICS - All Types

### 1. **Counter** (Monotonically Increasing)
- **What**: Value that only goes up (like an odometer)
- **When to use**: Total counts that never decrease
- **Examples**: Total HTTP requests, bytes sent, errors count
- **In this codebase** (Controller.java:62-67):
```java
requestCounter = meter
    .counterBuilder("request.count")
    .setDescription("Total number of requests received")
    .build();

// Usage:
requestCounter.add(randomCount, attributes);  // Adds to total
```

### 2. **Asynchronous Counter**
- **What**: Counter that's read once per export cycle (not continuously incremented)
- **When to use**: When you have the total but can't track each increment
- **Examples**: Total disk reads (from system stats), total cache hits from a cache library
- **Code example**:
```java
meter.counterBuilder("system.disk.reads")
    .buildWithCallback(measurement ->
        measurement.record(getDiskReadsFromOS())  // Called periodically
    );
```

### 3. **UpDownCounter** (Can Increase/Decrease)
- **What**: Value that can go up or down
- **When to use**: Tracking items that can increase or decrease
- **Examples**: Queue length, active connections, items in a cache
- **Code example**:
```java
UpDownCounter queueSize = meter.upDownCounterBuilder("queue.size").build();

queueSize.add(1);   // Item added to queue
queueSize.add(-1);  // Item removed from queue
```

### 4. **Asynchronous UpDownCounter** (Gauge-like)
- **What**: Current value that can go up/down, read periodically
- **When to use**: When you have the current value but don't track each change
- **Examples**: Current memory usage, number of active requests
- **In this codebase** (Controller.java:70-74):
```java
meter.gaugeBuilder("active.requests")
    .setDescription("Number of currently active requests")
    .buildWithCallback(measurement ->
        measurement.record(activeRequests)  // Reads current value
    );
```

### 5. **Gauge** (Synchronous)
- **What**: Current instantaneous value measured at a specific time
- **When to use**: Values that fluctuate and you want to sample
- **Examples**: CPU temperature, current fan speed, fuel level
- **Code example**:
```java
Gauge cpuTemp = meter.gaugeBuilder("cpu.temperature").build();
cpuTemp.record(getCurrentCPUTemp());  // Records current value
```

### 6. **Histogram** (Distribution of Values)
- **What**: Statistical distribution showing how values are spread
- **When to use**: Understanding latency, sizes, or any distribution
- **Examples**: Request duration, response sizes, database query times
- **In this codebase** (Controller.java:53-59):
```java
doWorkHistogram = meter
    .histogramBuilder("yrs_local_metric")
    .setDescription("Time spent doing work in milliseconds")
    .setUnit("ms")
    .ofLongs()
    .build();

// Usage: Records multiple values to build distribution
doWorkHistogram.record(sleepTime, attributes);
```

**Histogram Output** (creates 3 metrics):
- `yrs_local_metric_bucket{le="100"}` - Count of values ≤ 100ms
- `yrs_local_metric_sum` - Total sum of all values
- `yrs_local_metric_count` - Total number of measurements

---

## 🔍 TRACES - Terminologies

### Core Components

#### **Trace**
- **What**: Complete journey of a request through your system
- **Contains**: Multiple spans showing the full request path
- **Example**: User request → API Gateway → Auth Service → Database → Response

#### **Span**
- **What**: Single unit of work (one operation in the trace)
- **Contains**: Operation name, start/end time, attributes, events
- **In this codebase** (Controller.java:161-191):
```java
Span span = tracer.spanBuilder("doWork").startSpan();
span.setAttribute("clientId", clientId);
span.setAttribute("sleep_time_ms", sleepTime);
// ... do work ...
span.end();
```

#### **Tracer**
- **What**: Factory that creates spans
- **Setup**: One per application/library
- **In this codebase** (Controller.java:49):
```java
tracer = openTelemetry.getTracer(Application.class.getName());
```

#### **Tracer Provider**
- **What**: Factory that creates tracers
- **Setup**: Initialized once at application startup

### Span Details

#### **Span Context**
- **Contains**:
  - `trace_id` - Unique ID for the entire trace (32 hex chars)
  - `span_id` - Unique ID for this span (16 hex chars)
  - `trace_flags` - Binary flags (01 = sampled)
  - `trace_state` - Vendor-specific trace info

**Example from logs:**
```
trace_id=3401db36ec8632809b531910f7616a69
span_id=7a6f3bb3352d451a
trace_flags=01
```

#### **Parent Span ID**
- **What**: Links child spans to their parent
- **Creates**: Hierarchical tree of operations
- **Example**: HTTP Request Span → Database Query Span → SQL Execution Span

#### **Span Attributes**
- **What**: Key-value metadata describing the operation
- **Types**: String, Boolean, Number, Arrays
- **In this codebase** (Controller.java:166-174):
```java
span.setAttribute("clientId", clientId);           // String
span.setAttribute("is_premium", isPremium);        // Boolean
span.setAttribute("sleep_time_ms", sleepTime);     // Number
span.setAttribute("priority", random.nextInt(5));  // Number
```

#### **Span Events**
- **What**: Timestamped annotations marking specific moments
- **Use case**: "Exception thrown", "Cache hit", "Retry attempt"
- **Example**:
```java
span.addEvent("cache_miss",
    Attributes.of(AttributeKey.stringKey("key"), cacheKey));
```

#### **Span Links**
- **What**: Connections to other spans (different traces)
- **Use case**: Async operations, batch processing, causally related work
- **Example**: Batch job processing 1000 items → links to each item's trace

#### **Span Status**
- **Unset**: Default, operation completed successfully
- **Error**: Operation failed
- **Ok**: Explicitly marked as successful

**In this codebase** (TelemetryFilter.java:78-80):
```java
if (httpResponse.getStatus() >= 400) {
    currentSpan.setStatus(StatusCode.ERROR, "HTTP " + httpResponse.getStatus());
}
```

#### **Span Kind**
- **CLIENT**: Outgoing request (calling another service)
- **SERVER**: Incoming request (handling a request)
- **INTERNAL**: Internal operation (same process) ← Used in `doWork` span
- **PRODUCER**: Creating a job/message (Kafka producer)
- **CONSUMER**: Processing a job/message (Kafka consumer)

---

## 📝 LOGS - Terminologies

### Core Components

#### **Log / Log Record**
- **What**: Timestamped record of an event
- **Types**: Structured (JSON), Unstructured (plain text), Semi-structured
- **In this codebase**: SLF4J Logger statements

#### **Structured Logs** (Recommended)
- **What**: Machine-readable, consistent format (usually JSON)
- **Benefits**: Easy to parse, query, analyze
- **Example**:
```json
{
  "timestamp": "2025-11-19T17:04:20.160Z",
  "level": "INFO",
  "message": "Processing request",
  "clientId": "acme-corp",
  "teamId": "engineering",
  "trace_id": "3401db36ec8632809b531910f7616a69"
}
```

#### **Unstructured Logs**
- **What**: Plain text, human-readable
- **Issues**: Hard to parse and query at scale
- **Example**: `"User john logged in at 3pm"`

### Log Components

#### **Log Body**
- **What**: Main content of the log message
- **In this codebase**: `"Processing request for clientId=acme-corp..."`

#### **Severity / Log Level**
- **Levels**: TRACE, DEBUG, INFO, WARN, ERROR, FATAL
- **OpenTelemetry**: Maps to SeverityNumber (1-24)
- **This codebase uses**: `LOGGER.info(...)` = INFO = SeverityNumber 9

#### **Timestamp**
- **ObservedTimestamp**: When log was recorded by system
- **Timestamp**: When event actually occurred

#### **Log Attributes**
- **What**: Metadata attached to logs (like span attributes)
- **This codebase**: MDC values automatically become log attributes

#### **Instrumentation Scope**
- **What**: Which logger/class emitted the log
- **Example**: `io.opentelemetry.example.javagent.Controller`

#### **Trace Context in Logs**
- **What**: Links logs to traces for correlation
- **This codebase includes**:
  - `trace_id` - Which trace this log belongs to
  - `span_id` - Which span was active when log was written
  - `trace_flags` - Sampling decision

**Example from logs:**
```
Body: Str(Processing request for clientId=client2...)
Trace ID: 421c3f7bcf18c69631275d83d7272b76
Span ID: 1a3f68079b6104cf
Flags: 1
```

---

## 🌐 COMMON CONCEPTS (Across All Signals)

### **Attributes**
- **What**: Key-value pairs for filtering and grouping
- **Cardinality**:
  - **Low cardinality** (metrics): region, status, endpoint (limited values)
  - **High cardinality** (traces/logs): userId, requestId (unlimited values)
- **In this codebase** (Controller.java:120-129):
```java
Attributes.builder()
    .put(ATTR_METHOD, "GET")
    .put(ATTR_ENDPOINT, "/ping")
    .put(ATTR_REGION, region)
    .put(ATTR_CLIENT_ID, clientId)
    .build()
```

### **Resource Attributes**
- **What**: Metadata about the service itself (not the request)
- **Examples**:
  - `service.name` = "agent-example-app"
  - `service.version` = "0.3.0-SNAPSHOT"
  - `host.name`, `container.id`, `cloud.provider`

### **Instrumentation Scope**
- **What**: Identifies which library/component created the telemetry
- **Example**: `io.opentelemetry.example.javagent.Application`

### **Meter**
- **What**: Factory for creating metric instruments
- **In this codebase** (Controller.java:50):
```java
Meter meter = openTelemetry.getMeter(Application.class.getName());
```

### **MDC (Mapped Diagnostic Context)**
- **What**: Thread-local storage for log context (SLF4J concept)
- **This codebase setup** (TelemetryFilter.java:52-57):
```java
MDC.put("clientId", clientId);
MDC.put("teamId", teamId);
MDC.put("correlationId", correlationId);
```
- **Result**: All logs in that thread automatically include these values

### **Context Propagation**
- **What**: Passing trace context across service boundaries
- **Methods**: HTTP headers (W3C Trace Context), gRPC metadata
- **Automatic**: OpenTelemetry agent handles this automatically

---

## 📚 Summary Table

| Signal | Primary Use | Key Concepts | Cardinality |
|--------|-------------|--------------|-------------|
| **Metrics** | Aggregated statistics | Counter, Histogram, Gauge, Attributes | Low (for attributes) |
| **Traces** | Request flow & timing | Span, Trace, Parent-Child, Events, Links | High |
| **Logs** | Detailed events | Body, Severity, MDC, Trace Correlation | High |

---

## 🎯 When to Use Each Signal

### Use Metrics When:
- Tracking aggregated data (request rates, error counts)
- Monitoring system health (CPU, memory, disk)
- Creating dashboards and alerts
- Need low storage overhead

### Use Traces When:
- Understanding request flow through services
- Identifying performance bottlenecks
- Debugging distributed systems
- Analyzing service dependencies

### Use Logs When:
- Recording detailed application events
- Debugging specific issues
- Audit trails and compliance
- Capturing error details and stack traces

---

## 📖 This Codebase Implementation

### Metrics
- **Histogram**: `yrs_local_metric` - measures work duration distribution
- **Counter**: `request.count` - total requests processed
- **Async Gauge**: `active.requests` - current active requests

### Traces
- **Root Span**: HTTP request (created by OpenTelemetry agent)
- **Child Span**: `doWork` operation with custom attributes

### Logs
- **Structured with MDC**: All logs include trace context and custom attributes
- **Logback pattern**: `%mdc` automatically includes all MDC values
- **Trace-Log Correlation**: Every log linked to its trace via trace_id and span_id

### Attributes Used Across All Signals
- `clientId` (values: client1, client2, client3)
- `teamId` (values: teamId1, teamId2)
- `region` (values: us-east-1, eu-west-1)
- `isPremium` (values: true, false)
- `userId` (unique per request)
- `correlationId` (unique per request)

All three signals work together for complete observability!
