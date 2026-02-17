# Observability: Security, Troubleshooting, and Production Best Practices

This guide covers practical aspects of running OpenTelemetry in production: security, troubleshooting, querying data, deployment considerations, cost optimization, and testing.

---

## 🔒 Security & Authentication

### API Key Management

**This Codebase Uses:**
```yaml
# docker-compose.yml
environment:
  GROUNDCOVER_INGESTION_KEY: gcik_AEBAAABK_UVUZYN4T_IQLJSP64_XGUQ65Q3

# collector-config.yaml
exporters:
  otlphttp/groundcover:
    headers:
      apikey: ${env:GROUNDCOVER_INGESTION_KEY}
```

**Best Practices:**

1. **Never Hardcode API Keys in Source Code**
```bash
# ❌ Bad - committed to git
GROUNDCOVER_INGESTION_KEY=gcik_AEBAAABK_...

# ✅ Good - environment variable
export GROUNDCOVER_INGESTION_KEY=$(cat /run/secrets/groundcover_key)
```

2. **Use Secret Management Systems**
```yaml
# Kubernetes Secret
apiVersion: v1
kind: Secret
metadata:
  name: observability-secrets
type: Opaque
data:
  groundcover-key: Z2Npay1BRUJBQUFCSy0uLi4=  # base64 encoded

---
# Reference in deployment
env:
  - name: GROUNDCOVER_INGESTION_KEY
    valueFrom:
      secretKeyRef:
        name: observability-secrets
        key: groundcover-key
```

3. **Rotate Keys Regularly**
```bash
# Generate new key in Groundcover dashboard
# Update secret
kubectl create secret generic observability-secrets \
  --from-literal=groundcover-key=NEW_KEY \
  --dry-run=client -o yaml | kubectl apply -f -

# Restart pods to pick up new secret
kubectl rollout restart deployment/app
```

### TLS/SSL Configuration

**This Codebase:**
- App → Collector: HTTP (internal Docker network, safe)
- Collector → Groundcover: HTTPS (encrypted over internet)

**Production Recommendations:**

```yaml
# collector-config.yaml - Enable TLS for receivers
receivers:
  otlp:
    protocols:
      http:
        endpoint: "0.0.0.0:4318"
        tls:
          cert_file: /certs/server.crt
          key_file: /certs/server.key
          client_ca_file: /certs/ca.crt  # For mutual TLS

# Exporters - enforce TLS
exporters:
  otlphttp/groundcover:
    endpoint: https://i0ps1f.platform.grcv.io
    tls:
      insecure: false  # Enforce TLS verification
      ca_file: /certs/ca-bundle.crt  # Custom CA if needed
```

### Securing Sensitive Data in Attributes

**Problem: Accidentally logging sensitive data**

```java
// ❌ Bad - PII in attributes
span.setAttribute("user_email", "john@example.com");
span.setAttribute("credit_card", "4111-1111-1111-1111");
span.setAttribute("password", userPassword);

// ✅ Good - Sanitized or hashed
span.setAttribute("user_id", userId);  // Use ID instead of email
span.setAttribute("payment_method_type", "credit_card");  // Not the actual number
// Never log passwords!
```

**Filtering in Collector:**

```yaml
# collector-config.yaml
processors:
  attributes:
    actions:
      # Remove sensitive attributes
      - key: credit_card
        action: delete
      - key: ssn
        action: delete
      - key: password
        action: delete

      # Hash email addresses
      - key: user_email
        action: hash

  redaction:
    # Redact patterns in span names and attributes
    allow_all_keys: false
    allowed_keys:
      - http.method
      - http.status_code
      - clientId
    blocked_values:
      - "4[0-9]{12}(?:[0-9]{3})?"  # Credit card regex
      - "[0-9]{3}-[0-9]{2}-[0-9]{4}"  # SSN regex
```

### PII and GDPR Compliance

**Strategies:**

1. **Data Minimization** - Only collect what you need
```java
// ✅ Collect business context, not personal data
span.setAttribute("customer_tier", "premium");  // OK
span.setAttribute("customer_name", name);       // Avoid
```

2. **Data Retention Policies**
```yaml
# Configure short retention for detailed traces
# Longer retention for aggregated metrics

# Groundcover/Backend Configuration:
traces_retention: 7 days    # Detailed traces
metrics_retention: 90 days  # Aggregated metrics
```

3. **Right to be Forgotten**
```bash
# Ensure your backend supports data deletion
# Groundcover: Use their API to delete user data
curl -X DELETE "https://api.groundcover.io/v1/data" \
  -H "Authorization: Bearer $API_KEY" \
  -d '{"user_id": "12345", "delete_all": true}'
```

4. **Anonymization**
```java
// Use pseudonyms for user tracking
String anonymousId = hashUserId(actualUserId);
span.setAttribute("anonymous_user_id", anonymousId);
```

### Network Security

**Firewall Rules:**
```bash
# Only collector needs internet access
# Apps talk to collector on internal network

# Kubernetes NetworkPolicy example
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: collector-egress
spec:
  podSelector:
    matchLabels:
      app: otel-collector
  policyTypes:
    - Egress
  egress:
    # Allow to Groundcover
    - to:
      - namespaceSelector: {}
      ports:
      - protocol: TCP
        port: 443
    # Allow DNS
    - to:
      - namespaceSelector: {}
      ports:
      - protocol: UDP
        port: 53
```

---

## 🔧 Troubleshooting Guide

### Common Issues and Solutions

#### Issue 1: No Data in Groundcover

**Symptoms:**
- Collector running but no data in backend
- Metrics/traces not appearing in dashboards

**Debugging Steps:**

1. **Check Application is Sending Data**
```bash
# View app logs for OpenTelemetry messages
docker logs javaagent-app-1 2>&1 | grep -i otel

# Should see:
# [otel.javaagent] - opentelemetry-javaagent - version: 2.21.0
# [otel.javaagent] - Agent initialized
```

2. **Check Collector is Receiving Data**
```bash
# View collector logs
docker logs javaagent-collector-1

# Look for:
# - "Trace received" or "Metrics received"
# - Export statistics
# - Any error messages

# Check debug exporter output
docker logs javaagent-collector-1 2>&1 | grep -A 5 "ResourceMetrics"
```

3. **Verify Network Connectivity**
```bash
# App can reach collector
docker exec javaagent-app-1 curl -v http://collector:4318/v1/metrics

# Collector can reach Groundcover
docker exec javaagent-collector-1 \
  curl -v https://i0ps1f.platform.grcv.io/v1/metrics \
  -H "apikey: $GROUNDCOVER_INGESTION_KEY" \
  -d '{"test":"data"}'
```

4. **Check Collector Configuration**
```bash
# Validate collector config syntax
docker exec javaagent-collector-1 \
  /otelcol --config=/etc/otel-collector-config.yaml --dry-run

# Should output: "Config validated successfully"
```

**Common Fixes:**

```yaml
# Fix 1: Wrong endpoint
exporters:
  otlphttp/groundcover:
    endpoint: https://i0ps1f.platform.grcv.io  # ✅ Correct
    # endpoint: http://i0ps1f.platform.grcv.io  # ❌ Wrong (http vs https)

# Fix 2: Missing API key
exporters:
  otlphttp/groundcover:
    headers:
      apikey: ${env:GROUNDCOVER_INGESTION_KEY}  # Must be set!

# Fix 3: Not connected to pipeline
service:
  pipelines:
    metrics:
      receivers: [otlp]
      processors: [batch]
      exporters: [debug, otlphttp/groundcover]  # Must list the exporter!
```

#### Issue 2: Authentication Failures

**Symptoms:**
```
Error: 401 Unauthorized
Error: 403 Forbidden
```

**Debugging:**

1. **Verify API Key**
```bash
# Check environment variable is set
docker exec javaagent-collector-1 printenv GROUNDCOVER_INGESTION_KEY

# Test authentication manually
curl -v https://i0ps1f.platform.grcv.io/v1/metrics \
  -H "apikey: gcik_AEBAAABK_UVUZYN4T_IQLJSP64_XGUQ65Q3" \
  -H "Content-Type: application/json" \
  -d '{}' 2>&1 | grep -E "(< HTTP|apikey)"
```

2. **Check Key Format**
```bash
# Groundcover keys start with "gcik_"
echo $GROUNDCOVER_INGESTION_KEY | grep "^gcik_"

# New Relic keys are ~40 chars
# Datadog keys are 32 chars
```

3. **Check Key Permissions**
- Log into Groundcover dashboard
- Verify key has "Write Metrics", "Write Traces", "Write Logs" permissions
- Check key hasn't expired

**Common Fixes:**

```yaml
# Fix 1: Wrong header name
headers:
  apikey: ${env:GROUNDCOVER_INGESTION_KEY}  # ✅ Correct for Groundcover
  # api-key: ...  # ❌ Wrong
  # Authorization: Bearer ...  # Different format

# Fix 2: Key not interpolated
headers:
  apikey: ${env:GROUNDCOVER_INGESTION_KEY}  # ✅ Correct
  # apikey: $GROUNDCOVER_INGESTION_KEY  # ❌ Wrong (shell syntax)
  # apikey: "gcik_..."  # ❌ Hardcoded (bad practice)
```

#### Issue 3: High Cardinality Warnings

**Symptoms:**
```
Warning: Metric cardinality too high
Warning: Dropping metrics due to cardinality limit
```

**Cause:** Too many unique attribute combinations

```java
// ❌ Problem: Millions of unique combinations
requestCounter.add(1,
    Attributes.of(
        "user_id", userId,        // 1M users
        "request_id", requestId   // Unique per request
    ));
// Creates: 1M × ∞ = Infinite unique metrics!
```

**Fix:**

```java
// ✅ Solution: Low-cardinality attributes for metrics
requestCounter.add(1,
    Attributes.of(
        "client_tier", "premium",  // Only 3-5 values
        "region", "us-east-1"      // Only 10-20 values
    ));

// Use high-cardinality attributes in spans (traces) instead
Span span = tracer.spanBuilder("request").startSpan();
span.setAttribute("user_id", userId);     // OK for traces!
span.setAttribute("request_id", requestId); // OK for traces!
```

**Collector-Side Fix:**

```yaml
# Limit cardinality in collector
processors:
  attributes:
    actions:
      # Remove high-cardinality attributes from metrics
      - key: user_id
        action: delete
      - key: request_id
        action: delete
      - key: trace_id
        action: delete
```

#### Issue 4: Missing Trace Context in Logs

**Symptoms:**
- Logs don't show `trace_id` or `span_id`
- Can't correlate logs with traces

**Check:**

```bash
# View raw logs
docker logs javaagent-app-1 2>&1 | head -20

# Should see: trace_id=abc123 span_id=def456
# Missing? Check logback configuration
```

**Fix:**

```xml
<!-- src/main/resources/logback.xml -->
<configuration>
    <appender name="CONSOLE" class="ch.qos.logback.core.ConsoleAppender">
        <encoder>
            <pattern>
                %d{HH:mm:ss.SSS} [%thread] %-5level %logger{36} -
                trace_id=%X{trace_id} span_id=%X{span_id} trace_flags=%X{trace_flags} -
                %msg %mdc%n
            </pattern>
        </encoder>
    </appender>
</configuration>
```

**Verify OpenTelemetry Agent Extension:**

```dockerfile
# Dockerfile - Ensure logback extension is loaded
ENTRYPOINT java -javaagent:/opentelemetry-javaagent.jar \
    -Dotel.javaagent.extensions=/opentelemetry-javaagent-extension.jar \  # Must include this!
    -jar /app.jar
```

#### Issue 5: Collector Using Too Much Memory/CPU

**Symptoms:**
```
OOMKilled (out of memory)
High CPU usage (>50%)
Slow export times
```

**Debugging:**

```bash
# Check resource usage
docker stats javaagent-collector-1

# View collector metrics
curl http://localhost:8888/metrics | grep otelcol
```

**Common Causes:**

1. **No Batching**
```yaml
# ❌ Bad - sends every span immediately
service:
  pipelines:
    traces:
      receivers: [otlp]
      exporters: [otlphttp/groundcover]

# ✅ Good - batches spans
service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: [batch]  # Add batching!
      exporters: [otlphttp/groundcover]
```

2. **Batch Too Large**
```yaml
processors:
  batch:
    timeout: 10s
    send_batch_size: 10000  # ❌ Too large!

# ✅ Better
processors:
  batch:
    timeout: 10s
    send_batch_size: 1024   # Reasonable size
    send_batch_max_size: 2048
```

3. **Too Much Debug Logging**
```yaml
# ❌ Bad for production
exporters:
  debug:
    verbosity: detailed  # Logs EVERYTHING

# ✅ Good - disable or reduce
exporters:
  debug:
    verbosity: normal  # Or remove entirely
```

4. **Memory Limiter Missing**
```yaml
# Add memory limiter
processors:
  memory_limiter:
    check_interval: 1s
    limit_mib: 512      # Collector limit
    spike_limit_mib: 128
  batch:
    timeout: 10s

service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: [memory_limiter, batch]  # Memory limiter FIRST
      exporters: [otlphttp/groundcover]
```

### Useful Debug Commands

```bash
# View all OpenTelemetry environment variables
docker exec javaagent-app-1 printenv | grep OTEL

# Check if Java agent is loaded
docker exec javaagent-app-1 ps aux | grep javaagent

# Test OTLP endpoint manually
curl -X POST http://localhost:4318/v1/metrics \
  -H "Content-Type: application/json" \
  -d '{
    "resourceMetrics": [{
      "resource": {},
      "scopeMetrics": [{
        "scope": {},
        "metrics": [{
          "name": "test.metric",
          "unit": "1",
          "sum": {
            "dataPoints": [{
              "timeUnixNano": "1234567890000000000",
              "asInt": "42"
            }]
          }
        }]
      }]
    }]
  }'

# View collector pipeline structure
docker exec javaagent-collector-1 cat /etc/otel-collector-config.yaml | grep -A 10 "service:"

# Check if collector is healthy
curl http://localhost:13133/  # Health check endpoint (if enabled)

# View collector Prometheus metrics
curl http://localhost:8888/metrics
```

---

## 📊 Querying & Visualizing Data in Groundcover

### Accessing Your Data

**Groundcover Dashboard:**
```
https://console.groundcover.com/
→ Select your cluster
→ Navigate to Metrics, Traces, or Logs
```

### Querying Custom Metrics

**Your custom metrics:**
1. `yrs_local_metric` - Histogram (work duration)
2. `request.count` - Counter (total requests)
3. `active.requests` - Gauge (current active)

**Example Queries:**

```promql
# Total requests in last 5 minutes
sum(rate(request_count[5m]))

# Average work duration by client
avg(yrs_local_metric) by (clientId)

# 95th percentile latency by region
histogram_quantile(0.95, sum(rate(yrs_local_metric_bucket[5m])) by (le, region))

# Error rate
sum(rate(request_count{status="error"}[5m])) / sum(rate(request_count[5m]))

# Requests per second by endpoint
sum(rate(request_count[1m])) by (endpoint)

# Current active requests (gauge)
active_requests
```

### Filtering by Attributes

```promql
# Only premium clients
yrs_local_metric{is_premium="true"}

# Specific region
request_count{region="us-east-1"}

# Multiple conditions
yrs_local_metric{clientId="client1", region="us-east-1", is_premium="true"}

# Regex matching
request_count{endpoint=~"/api/.*"}
```

### Creating Dashboards

**Dashboard Structure:**

```yaml
Dashboard: Application Performance
├─ Panel 1: Request Rate (Line Chart)
│  Query: sum(rate(request_count[5m])) by (endpoint)
│
├─ Panel 2: P95 Latency (Line Chart)
│  Query: histogram_quantile(0.95, sum(rate(yrs_local_metric_bucket[5m])) by (le))
│
├─ Panel 3: Active Requests (Gauge)
│  Query: active_requests
│
└─ Panel 4: Requests by Client (Pie Chart)
   Query: sum(request_count) by (clientId)
```

**Useful Panels:**

1. **Golden Signals Dashboard**
```promql
# Latency
histogram_quantile(0.95, sum(rate(yrs_local_metric_bucket[5m])) by (le))

# Traffic
sum(rate(request_count[5m]))

# Errors
sum(rate(request_count{status=~"5.."}[5m]))

# Saturation
active_requests / 100  # Assuming 100 max workers
```

2. **Business Metrics Dashboard**
```promql
# Premium vs Free users
sum(rate(request_count[5m])) by (is_premium)

# Regional distribution
sum(request_count) by (region)

# Client activity
topk(10, sum(rate(request_count[5m])) by (clientId))
```

### Exploring Traces

**Find Traces:**
```
Groundcover Console → Traces
→ Filter by:
  - Service: agent-example-app
  - Operation: GET /ping
  - Duration: > 100ms
  - Status: Error
  - Attribute: clientId = "client1"
```

**Trace View Shows:**
```
Trace: 3401db36ec8632809b531910f7616a69
Duration: 156ms

├─ HTTP GET /ping (151ms)
│  ├─ Attributes:
│  │  - http.method: GET
│  │  - http.target: /ping
│  │  - http.status_code: 200
│  │  - clientId: client1
│  │  - region: us-east-1
│  │
│  └─ Child Span: doWork (145ms)
│     ├─ Attributes:
│     │  - sleep_time_ms: 143
│     │  - is_premium: true
│     │  - priority: 3
│     └─ Events:
│        - Starting work
│        - Work completed
```

**Linking Traces to Logs:**
```
Trace → Click "Related Logs" → Shows logs with same trace_id
Log → Click trace_id → Jumps to trace view
```

### Setting Up Alerts

**Example Alert Rules:**

1. **High Error Rate**
```yaml
Alert: HighErrorRate
Condition: sum(rate(request_count{status=~"5.."}[5m])) / sum(rate(request_count[5m])) > 0.05
Duration: 5m
Message: "Error rate above 5% for 5 minutes"
Notification: slack, pagerduty
```

2. **High Latency**
```yaml
Alert: HighP95Latency
Condition: histogram_quantile(0.95, sum(rate(yrs_local_metric_bucket[5m])) by (le)) > 1000
Duration: 10m
Message: "P95 latency above 1 second"
```

3. **Service Down**
```yaml
Alert: ServiceDown
Condition: absent(up{service="agent-example-app"})
Duration: 2m
Message: "Service has been down for 2 minutes"
```

---

## 🚀 Production Deployment Considerations

### Collector Deployment Patterns

#### Pattern 1: Sidecar (Agent Mode)

**Use Case:** Small deployments, simple setup

```yaml
# Kubernetes Deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app
spec:
  template:
    spec:
      containers:
        # Application container
        - name: app
          image: myapp:latest
          env:
            - name: OTEL_EXPORTER_OTLP_ENDPOINT
              value: "http://localhost:4318"  # Sidecar on localhost

        # Collector sidecar
        - name: otel-collector
          image: otel/opentelemetry-collector:latest
          args: ["--config=/etc/otel-collector-config.yaml"]
          volumeMounts:
            - name: config
              mountPath: /etc/otel-collector-config.yaml
              subPath: config.yaml
```

**Pros:**
- Simple setup
- Low latency (localhost)
- No network dependencies

**Cons:**
- High resource usage (one collector per pod)
- Harder to update collector config
- Duplicated processing

#### Pattern 2: Gateway (DaemonSet + Deployment)

**Use Case:** Production, scalable, efficient

```yaml
# DaemonSet - One per node for low latency
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: otel-collector-agent
spec:
  template:
    spec:
      containers:
        - name: otel-collector
          image: otel/opentelemetry-collector:latest
          env:
            - name: OTEL_EXPORTER_OTLP_ENDPOINT
              value: "http://otel-collector-gateway:4318"  # Forward to gateway
---
# Deployment - Centralized gateway (multiple replicas)
apiVersion: apps/v1
kind: Deployment
metadata:
  name: otel-collector-gateway
spec:
  replicas: 3  # Scale based on load
  template:
    spec:
      containers:
        - name: otel-collector
          image: otel/opentelemetry-collector:latest
          # This sends to backend
```

**Architecture:**
```
App → DaemonSet Collector (on same node) → Gateway Collector → Backend
```

**Pros:**
- Efficient resource usage
- Easy to scale gateway
- Centralized processing
- Can do tail sampling

**Cons:**
- More complex setup
- Additional network hop

#### Pattern 3: Gateway Only

**Use Case:** This codebase! Simple, cost-effective

```yaml
# Single collector deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: otel-collector
spec:
  replicas: 2  # For high availability
  template:
    spec:
      containers:
        - name: otel-collector
          image: otel/opentelemetry-collector:latest
```

**Pros:**
- Simplest architecture
- One place to manage config
- Cost-effective

**Cons:**
- Network latency to collector
- Single point of failure (mitigate with replicas)

### High Availability Setup

```yaml
# Collector with multiple replicas
apiVersion: apps/v1
kind: Deployment
metadata:
  name: otel-collector
spec:
  replicas: 3  # Multiple replicas
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0  # Zero downtime
  template:
    spec:
      containers:
        - name: otel-collector
          resources:
            requests:
              memory: "512Mi"
              cpu: "500m"
            limits:
              memory: "1Gi"
              cpu: "1000m"
          livenessProbe:
            httpGet:
              path: /
              port: 13133
          readinessProbe:
            httpGet:
              path: /
              port: 13133
---
# Service with load balancing
apiVersion: v1
kind: Service
metadata:
  name: otel-collector
spec:
  type: ClusterIP
  selector:
    app: otel-collector
  ports:
    - name: otlp-http
      port: 4318
      targetPort: 4318
    - name: otlp-grpc
      port: 4317
      targetPort: 4317
```

### Resource Requirements

**Collector Sizing Guide:**

| Load | Data Volume | CPU | Memory | Replicas |
|------|-------------|-----|--------|----------|
| **Small** | <100GB/day | 500m | 512Mi | 1-2 |
| **Medium** | 100-500GB/day | 1000m | 1Gi | 2-3 |
| **Large** | 500GB-1TB/day | 2000m | 2Gi | 3-5 |
| **Very Large** | >1TB/day | 4000m | 4Gi | 5-10 |

**Application Overhead:**

```yaml
# Java agent overhead: ~2-5% CPU, ~50-100MB memory
containers:
  - name: app
    resources:
      requests:
        memory: "512Mi"  # Base app
        # + 100Mi for OpenTelemetry
        # = 612Mi total
      limits:
        memory: "1Gi"
```

### Monitoring the Collector

**Enable Metrics:**

```yaml
# collector-config.yaml
extensions:
  health_check:
    endpoint: "0.0.0.0:13133"

  zpages:
    endpoint: "0.0.0.0:55679"  # Debug pages

  pprof:
    endpoint: "0.0.0.0:1777"   # Performance profiling

service:
  extensions: [health_check, zpages, pprof]
  telemetry:
    metrics:
      address: "0.0.0.0:8888"  # Collector's own metrics
```

**Monitor Collector Metrics:**

```promql
# Collector's own metrics

# Data received
otelcol_receiver_accepted_spans
otelcol_receiver_accepted_metric_points

# Data exported
otelcol_exporter_sent_spans
otelcol_exporter_sent_metric_points

# Export failures
otelcol_exporter_send_failed_spans
otelcol_exporter_send_failed_metric_points

# Queue size (should stay low)
otelcol_exporter_queue_size

# Memory usage
otelcol_process_memory_rss
```

**Alert on Collector Issues:**

```yaml
# Collector is dropping data
Alert: CollectorDroppingData
Condition: rate(otelcol_processor_dropped_spans[5m]) > 0

# Collector export failures
Alert: CollectorExportFailures
Condition: rate(otelcol_exporter_send_failed_spans[5m]) > 10

# Collector queue backing up
Alert: CollectorQueueHigh
Condition: otelcol_exporter_queue_size > 1000
```

---

## 💰 Cost Optimization Strategies

### 1. Sampling Configuration

**Head Sampling** (This codebase currently uses AlwaysOn):

```bash
# Environment variable approach
export OTEL_TRACES_SAMPLER=traceidratio
export OTEL_TRACES_SAMPLER_ARG=0.1  # 10% sampling

# Run with sampling
docker-compose up
```

**Different Rates for Different Services:**

```yaml
# collector-config.yaml
processors:
  probabilistic_sampler:
    sampling_percentage: 10  # 10% of all traces

  # Or more advanced
  tailsampling:
    policies:
      # Always sample errors
      - name: errors-policy
        type: status_code
        status_code:
          status_codes: [ERROR]

      # Always sample slow requests
      - name: slow-requests
        type: latency
        latency:
          threshold_ms: 1000

      # Sample 1% of everything else
      - name: probabilistic-policy
        type: probabilistic
        probabilistic:
          sampling_percentage: 1
```

**Estimated Savings:**

| Sampling Rate | Data Volume | Cost Impact |
|---------------|-------------|-------------|
| 100% (no sampling) | 1TB/day | Baseline |
| 10% sampling | 100GB/day | **90% savings** |
| 5% sampling | 50GB/day | **95% savings** |
| 1% sampling | 10GB/day | **99% savings** |

### 2. Attribute Filtering

**Remove Unnecessary Attributes:**

```yaml
# collector-config.yaml
processors:
  attributes:
    actions:
      # Remove high-cardinality attributes
      - key: request_id
        action: delete
      - key: user_id
        action: delete

      # Keep only specific attributes
      - key: http.user_agent
        action: delete  # Often not needed
```

**Keep Attributes for Spans, Remove from Metrics:**

```yaml
# Separate pipelines with different processing
processors:
  attributes/metrics:
    actions:
      # Remove high-cardinality from metrics only
      - key: user_id
        action: delete

service:
  pipelines:
    metrics:
      processors: [attributes/metrics, batch]  # Remove attributes

    traces:
      processors: [batch]  # Keep all attributes
```

### 3. Data Retention Policies

**Different Retention for Different Signals:**

```yaml
# Groundcover configuration (in their dashboard)
retention:
  traces: 7 days      # Short-term debugging
  metrics: 90 days    # Medium-term trends
  logs: 30 days       # Compliance/audit
```

**Cost Impact:**

| Signal | Retention | Cost per GB/month | Total Cost (1TB) |
|--------|-----------|-------------------|------------------|
| Traces | 7 days | $0.50 | $500 |
| Traces | 30 days | $0.50 | $2000 |
| Metrics | 90 days | $0.30 | $900 |
| Logs | 30 days | $0.40 | $1200 |

**Savings: 7-day vs 30-day trace retention = $1500/month**

### 4. Batching Optimization

```yaml
# Maximize batching for efficiency
processors:
  batch:
    timeout: 30s              # Wait up to 30s to fill batch
    send_batch_size: 2048     # Larger batches
    send_batch_max_size: 4096 # Maximum batch size
```

**Impact:**
- Fewer network requests
- Better compression
- Lower egress costs (for cloud deployments)

### 5. Compression

```yaml
# Enable compression
exporters:
  otlphttp/groundcover:
    endpoint: https://i0ps1f.platform.grcv.io
    compression: gzip  # Reduces data transfer by 70-80%
```

**Bandwidth Savings:**

| Data Size (uncompressed) | With gzip | Savings |
|--------------------------|-----------|---------|
| 1GB | 200-300MB | 70-80% |
| 10GB | 2-3GB | 70-80% |

### 6. Smart Metric Selection

**Only Create Metrics You'll Query:**

```java
// ❌ Too many metrics
LongHistogram endpoint1Histogram = meter.histogramBuilder("endpoint1.duration").build();
LongHistogram endpoint2Histogram = meter.histogramBuilder("endpoint2.duration").build();
LongHistogram endpoint3Histogram = meter.histogramBuilder("endpoint3.duration").build();
// 100 endpoints = 100 metrics!

// ✅ Better: One metric with attribute
LongHistogram httpDuration = meter.histogramBuilder("http.server.duration").build();
httpDuration.record(duration, Attributes.of("endpoint", "/api/users"));
// 1 metric, query by endpoint attribute
```

### 7. Use Gauges Instead of Counters When Possible

```java
// ❌ Expensive: High-frequency counter
for (int i = 0; i < 1000; i++) {
    activeConnections.add(1);  // 1000 data points
    // ... work ...
    activeConnections.add(-1);
}

// ✅ Cheaper: Gauge (sampled periodically)
meter.gaugeBuilder("active.connections")
    .buildWithCallback(m -> m.record(connectionCount));
// Only exported every 60s = way fewer data points
```

### Cost Comparison Example

**Scenario: 100 hosts, 10k req/sec**

| Strategy | Traces/Day | Metrics Points/Day | Monthly Cost | Savings |
|----------|------------|-------------------|--------------|---------|
| **Naive** | 86B traces @ 100% | 500B points | $25,000 | Baseline |
| **+ 10% Sampling** | 8.6B traces | 500B points | $5,000 | 80% |
| **+ Attribute Filtering** | 8.6B traces | 100B points | $3,000 | 88% |
| **+ Compression** | 8.6B traces | 100B points | $1,500 | 94% |
| **+ Smart Retention** | 8.6B traces (7d) | 100B points (90d) | $1,000 | **96%** |

---

## 🧪 Testing Your Instrumentation

### Unit Testing

**Test Metric Creation:**

```java
import io.opentelemetry.api.OpenTelemetry;
import io.opentelemetry.sdk.OpenTelemetrySdk;
import io.opentelemetry.sdk.metrics.SdkMeterProvider;
import io.opentelemetry.sdk.metrics.data.MetricData;
import io.opentelemetry.sdk.testing.exporter.InMemoryMetricReader;
import org.junit.jupiter.api.Test;

public class MetricsTest {

    @Test
    public void testRequestCounter() {
        // Setup in-memory collector
        InMemoryMetricReader reader = InMemoryMetricReader.create();
        SdkMeterProvider meterProvider = SdkMeterProvider.builder()
            .registerMetricReader(reader)
            .build();

        OpenTelemetry openTelemetry = OpenTelemetrySdk.builder()
            .setMeterProvider(meterProvider)
            .build();

        // Create metric
        Meter meter = openTelemetry.getMeter("test");
        LongCounter counter = meter.counterBuilder("request.count").build();

        // Record data
        counter.add(1, Attributes.of(
            AttributeKey.stringKey("endpoint"), "/ping"
        ));

        // Assert
        Collection<MetricData> metrics = reader.collectAllMetrics();
        assertEquals(1, metrics.size());
        assertEquals("request.count", metrics.iterator().next().getName());
    }
}
```

**Test Span Creation:**

```java
import io.opentelemetry.sdk.testing.exporter.InMemorySpanExporter;
import io.opentelemetry.sdk.trace.SdkTracerProvider;
import io.opentelemetry.sdk.trace.export.SimpleSpanProcessor;

@Test
public void testSpanCreation() {
    // Setup in-memory exporter
    InMemorySpanExporter exporter = InMemorySpanExporter.create();
    SdkTracerProvider tracerProvider = SdkTracerProvider.builder()
        .addSpanProcessor(SimpleSpanProcessor.create(exporter))
        .build();

    Tracer tracer = tracerProvider.get("test");

    // Create span
    Span span = tracer.spanBuilder("testOperation").startSpan();
    span.setAttribute("test.attribute", "value");
    span.end();

    // Assert
    List<SpanData> spans = exporter.getFinishedSpanItems();
    assertEquals(1, spans.size());
    assertEquals("testOperation", spans.get(0).getName());
    assertEquals("value", spans.get(0).getAttributes().get(AttributeKey.stringKey("test.attribute")));
}
```

### Integration Testing

**Test End-to-End Flow:**

```bash
#!/bin/bash
# test-telemetry.sh

echo "Starting services..."
docker-compose up -d

echo "Waiting for services to be ready..."
sleep 10

echo "Making test requests..."
for i in {1..10}; do
    curl http://localhost:8080/ping?clientId=test-client
done

echo "Checking collector received data..."
docker logs javaagent-collector-1 2>&1 | grep "ResourceMetrics" | wc -l

echo "Checking traces were created..."
docker logs javaagent-collector-1 2>&1 | grep "ResourceSpans" | wc -l

echo "Test complete!"
```

**Verify Data in Backend:**

```bash
#!/bin/bash
# verify-backend.sh

# Wait for data to reach backend (may take 30-60s)
sleep 60

# Query Groundcover API
curl "https://api.groundcover.io/v1/metrics?query=request_count" \
  -H "Authorization: Bearer $GROUNDCOVER_API_KEY" \
  | jq '.data.result | length'

# Should return > 0 if data is flowing
```

### Load Testing

**Test at Scale:**

```bash
# Use Apache Bench or similar
ab -n 10000 -c 100 http://localhost:8080/ping?clientId=client1

# Monitor collector during load
docker stats javaagent-collector-1

# Check for errors
docker logs javaagent-collector-1 2>&1 | grep -i error
```

**Verify No Data Loss:**

```bash
# Count requests sent
REQUESTS_SENT=$(curl -s http://localhost:8888/metrics | grep otelcol_receiver_accepted_spans | awk '{print $2}')

# Count requests exported
REQUESTS_EXPORTED=$(curl -s http://localhost:8888/metrics | grep otelcol_exporter_sent_spans | awk '{print $2}')

# Should be roughly equal (accounting for batching delays)
echo "Received: $REQUESTS_SENT"
echo "Exported: $REQUESTS_EXPORTED"
```

### Chaos Testing

**Test Collector Failure:**

```bash
# Stop collector
docker stop javaagent-collector-1

# Make requests (should not fail!)
curl http://localhost:8080/ping

# Check app logs for errors
docker logs javaagent-app-1 2>&1 | grep -i error

# Restart collector
docker start javaagent-collector-1

# Data should start flowing again
```

**Test Backend Failure:**

```yaml
# Simulate backend down
exporters:
  otlphttp/groundcover:
    endpoint: https://invalid-endpoint.com  # Wrong endpoint

# Collector should queue and retry
# Check queue metrics
curl http://localhost:8888/metrics | grep otelcol_exporter_queue_size
```

---

## 🎓 Advanced OpenTelemetry Concepts

### OpenTelemetry API vs SDK

Understanding the distinction between API and SDK is crucial for proper dependency management and usage.

#### API (Application Programming Interface)

**What it is:**
- Lightweight interfaces and no-op implementations
- Stable contracts that won't break
- Used directly in application code

**Dependencies:**
```gradle
// Only include API in your application
implementation 'io.opentelemetry:opentelemetry-api:1.44.1'
```

**Usage in Application Code:**
```java
import io.opentelemetry.api.OpenTelemetry;
import io.opentelemetry.api.trace.Tracer;
import io.opentelemetry.api.trace.Span;
import io.opentelemetry.api.metrics.Meter;
import io.opentelemetry.api.metrics.LongCounter;

public class MyService {
    private final Tracer tracer;
    private final LongCounter counter;

    public MyService(OpenTelemetry openTelemetry) {
        // API only - no implementation details
        this.tracer = openTelemetry.getTracer("my-service");
        Meter meter = openTelemetry.getMeter("my-service");
        this.counter = meter.counterBuilder("requests").build();
    }

    public void doWork() {
        Span span = tracer.spanBuilder("doWork").startSpan();
        try {
            counter.add(1);
            // Business logic
        } finally {
            span.end();
        }
    }
}
```

#### SDK (Software Development Kit)

**What it is:**
- Actual implementation of the API
- Configuration and setup code
- Processors, exporters, samplers
- Only needed at application startup

**Dependencies:**
```gradle
// SDK only needed for configuration (usually in main/bootstrap)
implementation 'io.opentelemetry:opentelemetry-sdk:1.44.1'
implementation 'io.opentelemetry:opentelemetry-sdk-trace:1.44.1'
implementation 'io.opentelemetry:opentelemetry-sdk-metrics:1.44.1'
implementation 'io.opentelemetry:opentelemetry-exporter-otlp:1.44.1'
```

**Usage in Bootstrap/Main:**
```java
import io.opentelemetry.api.OpenTelemetry;
import io.opentelemetry.sdk.OpenTelemetrySdk;
import io.opentelemetry.sdk.trace.SdkTracerProvider;
import io.opentelemetry.sdk.trace.export.BatchSpanProcessor;
import io.opentelemetry.sdk.trace.export.SpanExporter;
import io.opentelemetry.exporter.otlp.trace.OtlpGrpcSpanExporter;

public class Application {
    public static void main(String[] args) {
        // SDK configuration - only in bootstrap
        SpanExporter spanExporter = OtlpGrpcSpanExporter.builder()
            .setEndpoint("http://collector:4317")
            .build();

        SdkTracerProvider tracerProvider = SdkTracerProvider.builder()
            .addSpanProcessor(BatchSpanProcessor.builder(spanExporter).build())
            .build();

        OpenTelemetry openTelemetry = OpenTelemetrySdk.builder()
            .setTracerProvider(tracerProvider)
            .build();

        // Pass API interface to application
        MyService service = new MyService(openTelemetry);
        service.doWork();
    }
}
```

#### This Codebase Approach

**Uses Java Agent = No SDK/API in Code!**

```java
// Controller.java - No SDK imports!
import io.opentelemetry.api.OpenTelemetry;  // API only
import io.opentelemetry.api.trace.Tracer;
import io.opentelemetry.api.metrics.Meter;

// Configuration via environment variables and agent
// No SDK code needed!
```

**When to Use Each:**

| Scenario | Use API | Use SDK | Use Java Agent |
|----------|---------|---------|----------------|
| **Libraries** | ✅ Yes | ❌ No | N/A |
| **Application Code** | ✅ Yes | ❌ No | N/A |
| **Bootstrap/Main** | ✅ Yes | ✅ Yes | N/A |
| **Zero-code instrumentation** | N/A | N/A | ✅ Yes (this codebase) |

**Best Practice:**
```
Libraries → depend on API only (vendor-neutral)
Applications → depend on API + SDK (for bootstrap)
OR use Java Agent → zero code changes!
```

---

### Span Processors Configuration

Span processors determine how spans are processed and exported.

#### Types of Span Processors

**1. SimpleSpanProcessor**

**Behavior:**
- Exports each span immediately when it ends
- Synchronous export (blocks until export completes)
- No batching

**Use Case:**
- Development and debugging
- When you need immediate visibility
- Low-throughput applications

**Configuration:**
```java
import io.opentelemetry.sdk.trace.export.SimpleSpanProcessor;

SdkTracerProvider tracerProvider = SdkTracerProvider.builder()
    .addSpanProcessor(SimpleSpanProcessor.create(spanExporter))
    .build();
```

**Pros:**
- ✅ Immediate export (no delay)
- ✅ Simple to understand
- ✅ No buffering (low memory)

**Cons:**
- ❌ High overhead (one export per span)
- ❌ Blocks application threads
- ❌ Poor performance at scale

**2. BatchSpanProcessor** (Recommended for Production)

**Behavior:**
- Collects spans in a batch
- Exports asynchronously in background thread
- Configurable batch size and timeout

**Configuration:**
```java
import io.opentelemetry.sdk.trace.export.BatchSpanProcessor;

BatchSpanProcessor batchProcessor = BatchSpanProcessor.builder(spanExporter)
    .setScheduleDelay(5000, TimeUnit.MILLISECONDS)  // Export every 5 seconds
    .setMaxQueueSize(2048)                          // Queue up to 2048 spans
    .setMaxExportBatchSize(512)                     // Export 512 spans per batch
    .setExporterTimeout(30, TimeUnit.SECONDS)       // Timeout after 30s
    .build();

SdkTracerProvider tracerProvider = SdkTracerProvider.builder()
    .addSpanProcessor(batchProcessor)
    .build();
```

**Parameters:**

| Parameter | Default | Description |
|-----------|---------|-------------|
| `scheduleDelay` | 5000ms | Max time to wait before export |
| `maxQueueSize` | 2048 | Max spans in queue (oldest dropped if full) |
| `maxExportBatchSize` | 512 | Max spans per export batch |
| `exporterTimeout` | 30s | Timeout for export operation |

**Pros:**
- ✅ Asynchronous (non-blocking)
- ✅ Efficient (batches spans)
- ✅ Lower network overhead
- ✅ Better throughput

**Cons:**
- ❌ Delayed export (up to scheduleDelay)
- ❌ Memory buffering required
- ❌ Potential data loss if app crashes

**3. Multi-Span Processor**

**Use Case:** Send spans to multiple destinations

```java
SpanExporter jaegerExporter = JaegerGrpcSpanExporter.builder().build();
SpanExporter loggingExporter = LoggingSpanExporter.create();

SdkTracerProvider tracerProvider = SdkTracerProvider.builder()
    .addSpanProcessor(BatchSpanProcessor.builder(jaegerExporter).build())
    .addSpanProcessor(SimpleSpanProcessor.create(loggingExporter))  // Also log
    .build();
```

#### This Codebase (Java Agent)

**Agent Uses BatchSpanProcessor by Default**

Configure via environment variables:
```bash
# Batch processor configuration
OTEL_BSP_SCHEDULE_DELAY=5000              # 5 seconds
OTEL_BSP_MAX_QUEUE_SIZE=2048              # Queue size
OTEL_BSP_MAX_EXPORT_BATCH_SIZE=512        # Batch size
OTEL_BSP_EXPORT_TIMEOUT=30000             # 30 seconds timeout
```

**In docker-compose.yml:**
```yaml
environment:
  OTEL_BSP_SCHEDULE_DELAY: "5000"
  OTEL_BSP_MAX_QUEUE_SIZE: "2048"
  OTEL_BSP_MAX_EXPORT_BATCH_SIZE: "512"
```

**Tuning for Different Scenarios:**

```bash
# High-throughput (more buffering)
OTEL_BSP_SCHEDULE_DELAY=10000             # 10s delay
OTEL_BSP_MAX_QUEUE_SIZE=4096              # Large queue
OTEL_BSP_MAX_EXPORT_BATCH_SIZE=1024       # Large batches

# Low-latency (faster export)
OTEL_BSP_SCHEDULE_DELAY=1000              # 1s delay
OTEL_BSP_MAX_QUEUE_SIZE=512               # Small queue
OTEL_BSP_MAX_EXPORT_BATCH_SIZE=128        # Small batches

# Resource-constrained (low memory)
OTEL_BSP_SCHEDULE_DELAY=5000
OTEL_BSP_MAX_QUEUE_SIZE=512               # Smaller queue
OTEL_BSP_MAX_EXPORT_BATCH_SIZE=256        # Smaller batches
```

---

### Metrics Temporality

Metrics temporality defines **when** metric values are meaningful and how aggregation works.

#### Understanding Temporality

**Key Question:** Is this metric value:
- **Cumulative** - Total since process start?
- **Delta** - Change since last export?

#### Cumulative Temporality (Default in OpenTelemetry)

**Definition:** Metric represents the total value from the start of the application.

**Example - Counter:**
```
Time T0 (app start):  counter = 0
Time T1 (1 min):      counter = 100   (exported: 100)
Time T2 (2 min):      counter = 250   (exported: 250)
Time T3 (3 min):      counter = 500   (exported: 500)
                                       ↑ Cumulative total
```

**Visual:**
```
Exported Values: 100, 250, 500, 780, 1000...
                 └─ Each value is cumulative total
```

**Characteristics:**
- ✅ Client maintains state
- ✅ Backend can miss data points (reconstruct from next value)
- ✅ Better for unreliable networks
- ❌ Requires more client memory
- ❌ Requires backend to calculate deltas for rates

**Used By:**
- Prometheus (pull model)
- OpenTelemetry default
- Most modern systems

**Backend Processing:**
```promql
# Backend calculates rate from cumulative
rate(request_count[5m])
# Internally: (latest_value - previous_value) / time_difference
```

#### Delta Temporality

**Definition:** Metric represents the change since last export.

**Example - Counter:**
```
Time T0 (app start):  counter = 0
Time T1 (1 min):      counter incremented by 100   (exported: 100)
Time T2 (2 min):      counter incremented by 150   (exported: 150)
Time T3 (3 min):      counter incremented by 250   (exported: 250)
                                                    ↑ Delta since last export
```

**Visual:**
```
Exported Values: 100, 150, 250, 280, 220...
                 └─ Each value is the delta
```

**Characteristics:**
- ✅ Less client memory (no state)
- ✅ Simpler backend aggregation (just sum)
- ❌ Cannot miss data points (data loss!)
- ❌ Requires reliable network
- ❌ Harder to debug (no "current total")

**Used By:**
- StatsD
- AWS CloudWatch
- Azure Monitor
- Some legacy systems

**Backend Processing:**
```
# Backend just sums deltas
sum(deltas) = total increase
```

#### Temporality by Metric Type

| Metric Type | Cumulative | Delta |
|-------------|------------|-------|
| **Counter** | Total count since start | Count since last export |
| **Histogram** | All values since start | Values since last export |
| **Gauge** | Current value (no temporality) | N/A |
| **Sum (UpDownCounter)** | Current sum | Change in sum |

#### Configuring Temporality

**In OpenTelemetry SDK:**

```java
import io.opentelemetry.sdk.metrics.export.AggregationTemporalitySelector;
import io.opentelemetry.sdk.metrics.export.MetricReader;

// Cumulative (default)
MetricReader reader = PeriodicMetricReader.builder(exporter)
    .setAggregationTemporalitySelector(
        AggregationTemporalitySelector.alwaysComulative()
    )
    .build();

// Delta
MetricReader reader = PeriodicMetricReader.builder(exporter)
    .setAggregationTemporalitySelector(
        AggregationTemporalitySelector.deltaPreferred()
    )
    .build();

// Mixed (per instrument type)
MetricReader reader = PeriodicMetricReader.builder(exporter)
    .setAggregationTemporalitySelector(
        AggregationTemporalitySelector.deltaPreferred()
            .withCumulativePreference(InstrumentType.COUNTER)
    )
    .build();
```

**With Java Agent (Environment Variables):**

```bash
# Prefer delta temporality
OTEL_EXPORTER_OTLP_METRICS_TEMPORALITY_PREFERENCE=DELTA

# Prefer cumulative (default)
OTEL_EXPORTER_OTLP_METRICS_TEMPORALITY_PREFERENCE=CUMULATIVE

# Let backend decide
OTEL_EXPORTER_OTLP_METRICS_TEMPORALITY_PREFERENCE=LOWMEMORY
```

**In docker-compose.yml:**
```yaml
environment:
  OTEL_EXPORTER_OTLP_METRICS_TEMPORALITY_PREFERENCE: "CUMULATIVE"
```

#### Backend Preferences

| Backend | Preferred Temporality | Reason |
|---------|----------------------|--------|
| **Prometheus** | Cumulative | Pull model, expects cumulative |
| **Groundcover** | Cumulative | Built on VictoriaMetrics (Prometheus-compatible) |
| **Datadog** | Delta | Push model, stateless aggregation |
| **New Relic** | Both | Accepts both, converts internally |
| **AWS CloudWatch** | Delta | Native delta model |

#### Example Scenario

**Application Counter:**
```java
LongCounter requestCounter = meter
    .counterBuilder("http.requests")
    .build();

// Requests come in...
requestCounter.add(10);  // +10
requestCounter.add(15);  // +15
requestCounter.add(20);  // +20
// Total = 45 requests
```

**With Cumulative Export (every 60s):**
```
Minute 1: export 45
Minute 2: export 120  (45 + 75 new requests)
Minute 3: export 200  (120 + 80 new requests)
```

**With Delta Export (every 60s):**
```
Minute 1: export 45
Minute 2: export 75   (just the new requests)
Minute 3: export 80   (just the new requests)
```

**This Codebase:** Uses **Cumulative** (default for Groundcover/Prometheus-compatible backends)

---

### Collector Processors Reference

Processors sit in the collector pipeline and modify, filter, or enrich telemetry data.

#### Common Processors

**1. Batch Processor** (Essential)

**Purpose:** Batch data before export for efficiency

```yaml
processors:
  batch:
    timeout: 10s               # Export every 10 seconds
    send_batch_size: 1024      # Or when 1024 items collected
    send_batch_max_size: 2048  # Absolute max batch size
```

**Use:** Always use in production!

**2. Memory Limiter** (Critical for Production)

**Purpose:** Prevent OOM by limiting memory usage

```yaml
processors:
  memory_limiter:
    check_interval: 1s        # How often to check memory
    limit_mib: 512            # Hard limit
    spike_limit_mib: 128      # Spike tolerance (limit_mib + spike)
```

**Behavior:**
- Checks memory every `check_interval`
- If memory > `limit_mib`, refuse new data
- If memory > `limit_mib + spike_limit_mib`, drop data

**Must be first in pipeline:**
```yaml
processors: [memory_limiter, batch, attributes]  # memory_limiter FIRST
```

**3. Attributes Processor**

**Purpose:** Add, modify, or remove attributes

```yaml
processors:
  attributes:
    actions:
      # Insert new attribute
      - key: environment
        value: "production"
        action: insert

      # Update existing attribute
      - key: http.url
        action: update
        value: "redacted"

      # Delete attribute
      - key: password
        action: delete

      # Hash sensitive data
      - key: user_email
        action: hash

      # Extract from existing attribute
      - key: http.url
        pattern: ^(?P<http_protocol>.*):\/\/(?P<http_domain>.*)\/(?P<http_path>.*)
        action: extract

      # Upsert (insert or update)
      - key: region
        value: "us-east-1"
        action: upsert
```

**4. Resource Processor**

**Purpose:** Modify resource attributes (service metadata)

```yaml
processors:
  resource:
    attributes:
      - key: service.name
        value: "my-service"
        action: upsert
      - key: deployment.environment
        value: "production"
        action: insert
```

**5. Transform Processor** (Powerful!)

**Purpose:** Advanced transformations using OTTL (OpenTelemetry Transformation Language)

```yaml
processors:
  transform:
    trace_statements:
      - context: span
        statements:
          # Rename attribute
          - set(attributes["endpoint"], attributes["http.target"])
          - delete_key(attributes, "http.target")

          # Conditional logic
          - set(attributes["is_error"], true) where status.code == STATUS_CODE_ERROR

          # Truncate long strings
          - truncate_all(attributes, 4096)

          # Set span name
          - set(name, Concat([attributes["http.method"], " ", attributes["http.target"]], ""))

    metric_statements:
      - context: metric
        statements:
          # Convert units
          - set(unit, "ms") where name == "latency"
```

**6. Filter Processor**

**Purpose:** Drop telemetry based on conditions

```yaml
processors:
  filter:
    traces:
      span:
        # Drop health check spans
        - 'attributes["http.target"] == "/health"'
        - 'attributes["http.target"] == "/metrics"'

    metrics:
      metric:
        # Drop high-cardinality metrics
        - 'name == "http.request.duration" and attributes["user_id"] != nil'

    logs:
      log_record:
        # Drop debug logs in production
        - 'severity_number < SEVERITY_NUMBER_INFO'
```

**7. Probabilistic Sampler**

**Purpose:** Sample a percentage of traces

```yaml
processors:
  probabilistic_sampler:
    hash_seed: 22              # Seed for consistent sampling
    sampling_percentage: 10.0  # Sample 10%
```

**8. Tail Sampling** (Advanced)

**Purpose:** Make sampling decisions after seeing complete trace

```yaml
processors:
  tail_sampling:
    decision_wait: 10s         # Wait for complete trace
    num_traces: 100000         # Keep in memory
    expected_new_traces_per_sec: 10
    policies:
      # Always sample errors
      - name: error-policy
        type: status_code
        status_code:
          status_codes: [ERROR]

      # Always sample slow traces
      - name: slow-traces
        type: latency
        latency:
          threshold_ms: 1000

      # Sample by attribute
      - name: premium-customers
        type: string_attribute
        string_attribute:
          key: customer_tier
          values: ["premium", "enterprise"]

      # Sample 1% of everything else
      - name: default
        type: probabilistic
        probabilistic:
          sampling_percentage: 1
```

#### This Codebase Configuration

```yaml
# collector-config.yaml
processors:
  batch:
    timeout: 10s
    send_batch_size: 1024

service:
  pipelines:
    metrics:
      receivers: [otlp]
      processors: [batch]
      exporters: [debug, otlphttp/groundcover]

    traces:
      receivers: [otlp]
      processors: [batch]
      exporters: [otlphttp/groundcover]

    logs:
      receivers: [otlp]
      processors: [batch]
      exporters: [otlphttp/groundcover]
```

---

### Advanced Collector Processors (Filter & Transform)

#### Filtering Examples

**1. Remove Health Check Endpoints**

```yaml
processors:
  filter/healthcheck:
    traces:
      span:
        - 'attributes["http.target"] == "/health"'
        - 'attributes["http.target"] == "/ping"'
        - 'attributes["http.target"] == "/ready"'
        - 'attributes["http.target"] == "/live"'

service:
  pipelines:
    traces:
      processors: [filter/healthcheck, batch]
```

**2. Drop Internal Services**

```yaml
processors:
  filter/internal:
    traces:
      span:
        - 'resource.attributes["service.name"] == "internal-debug"'
        - 'resource.attributes["deployment.environment"] == "test"'
```

**3. Filter by Attribute Value**

```yaml
processors:
  filter/production:
    traces:
      span:
        # Only keep production traffic
        - 'attributes["environment"] != "production"'

    metrics:
      metric:
        # Drop test client metrics
        - 'attributes["clientId"] == "test-client"'
```

**4. Filter Logs by Severity**

```yaml
processors:
  filter/logs:
    logs:
      log_record:
        # Drop debug and trace logs
        - 'severity_number < SEVERITY_NUMBER_INFO'
```

#### Transform Examples

**1. Add Environment Tags**

```yaml
processors:
  transform/environment:
    trace_statements:
      - context: span
        statements:
          - set(attributes["environment"], "production")
          - set(attributes["region"], "us-east-1")

    metric_statements:
      - context: metric
        statements:
          - set(attributes["environment"], "production")
```

**2. Normalize HTTP Attributes**

```yaml
processors:
  transform/http:
    trace_statements:
      - context: span
        statements:
          # Standardize method to uppercase
          - set(attributes["http.method"], ConvertCase(attributes["http.method"], "upper"))

          # Remove query parameters from URL
          - replace_pattern(attributes["http.url"], "\\?.*", "")

          # Extract host from URL
          - set(attributes["http.host"], ExtractPatterns(attributes["http.url"], "^https?://([^/]+)"))
```

**3. Redact Sensitive Data**

```yaml
processors:
  transform/redact:
    trace_statements:
      - context: span
        statements:
          # Redact email addresses
          - replace_pattern(attributes["user.email"], "^(.)[^@]*@", "$1***@")

          # Redact API keys
          - replace_pattern(attributes["api_key"], ".*", "***REDACTED***")

          # Remove PII attributes
          - delete_key(attributes, "credit_card")
          - delete_key(attributes, "ssn")
          - delete_key(attributes, "password")
```

**4. Derive New Attributes**

```yaml
processors:
  transform/derive:
    trace_statements:
      - context: span
        statements:
          # Create endpoint attribute from method + path
          - set(attributes["endpoint"], Concat([attributes["http.method"], " ", attributes["http.target"]], ""))

          # Set error flag based on status code
          - set(attributes["is_error"], true) where attributes["http.status_code"] >= 400

          # Categorize response time
          - set(attributes["latency_bucket"], "fast") where duration < 100000000    # < 100ms
          - set(attributes["latency_bucket"], "medium") where duration >= 100000000 and duration < 500000000
          - set(attributes["latency_bucket"], "slow") where duration >= 500000000
```

**5. Aggregate High-Cardinality Attributes**

```yaml
processors:
  transform/aggregate:
    metric_statements:
      - context: metric
        statements:
          # Replace user_id with tier
          - set(attributes["user_tier"], "premium") where attributes["user_id"] in ["123", "456", "789"]
          - set(attributes["user_tier"], "free") where attributes["user_tier"] == nil
          - delete_key(attributes, "user_id")

          # Bucket numeric values
          - set(attributes["response_size_bucket"], "small") where attributes["response_size"] < 1000
          - set(attributes["response_size_bucket"], "medium") where attributes["response_size"] >= 1000 and attributes["response_size"] < 10000
          - set(attributes["response_size_bucket"], "large") where attributes["response_size"] >= 10000
          - delete_key(attributes, "response_size")
```

**6. Set Span Name from Attributes**

```yaml
processors:
  transform/span_name:
    trace_statements:
      - context: span
        statements:
          # Set span name to HTTP method + endpoint
          - set(name, Concat([attributes["http.method"], " ", attributes["http.route"]], "")) where attributes["http.route"] != nil
```

#### Complete Production Example

```yaml
processors:
  # 1. Memory protection (MUST BE FIRST)
  memory_limiter:
    check_interval: 1s
    limit_mib: 1024
    spike_limit_mib: 256

  # 2. Filter out noise
  filter/noise:
    traces:
      span:
        - 'attributes["http.target"] == "/health"'
        - 'attributes["http.target"] == "/metrics"'
    logs:
      log_record:
        - 'severity_number < SEVERITY_NUMBER_INFO'

  # 3. Redact sensitive data
  transform/security:
    trace_statements:
      - context: span
        statements:
          - replace_pattern(attributes["user.email"], "^(.)[^@]*@", "$1***@")
          - delete_key(attributes, "password")
          - delete_key(attributes, "api_key")

  # 4. Add environment context
  resource:
    attributes:
      - key: deployment.environment
        value: "production"
        action: upsert
      - key: region
        value: "us-east-1"
        action: insert

  # 5. Normalize and enrich
  transform/enrich:
    trace_statements:
      - context: span
        statements:
          - set(attributes["http.method"], ConvertCase(attributes["http.method"], "upper"))
          - set(attributes["is_error"], true) where attributes["http.status_code"] >= 400

  # 6. Batch for efficiency
  batch:
    timeout: 10s
    send_batch_size: 1024

service:
  pipelines:
    traces:
      receivers: [otlp]
      processors:
        - memory_limiter      # Protect memory
        - filter/noise        # Remove noise
        - transform/security  # Security
        - resource            # Add context
        - transform/enrich    # Enrich
        - batch               # Batch
      exporters: [otlphttp/groundcover]
```

**Benefits of This Pipeline:**
1. ✅ Memory protected (no OOM)
2. ✅ Less noise (health checks removed)
3. ✅ Secure (PII redacted)
4. ✅ Enriched (environment tags)
5. ✅ Normalized (consistent format)
6. ✅ Efficient (batched)

---

## 📚 Summary Checklist

### Security ✅
- [ ] API keys stored in secrets (not hardcoded)
- [ ] TLS enabled for production
- [ ] Sensitive data not in attributes
- [ ] PII compliance addressed
- [ ] Network policies configured

### Troubleshooting ✅
- [ ] Debug exporter enabled for testing
- [ ] Health checks configured
- [ ] Collector metrics exposed
- [ ] Logging configured for correlation
- [ ] Know how to check each component

### Querying ✅
- [ ] Understand your custom metrics
- [ ] Dashboards created
- [ ] Alerts configured
- [ ] Trace-log correlation working

### Production ✅
- [ ] Deployment pattern chosen (sidecar/gateway)
- [ ] High availability (multiple replicas)
- [ ] Resource limits set
- [ ] Collector monitoring in place
- [ ] Backup/disaster recovery plan

### Cost Optimization ✅
- [ ] Sampling configured (if needed)
- [ ] Unnecessary attributes removed
- [ ] Retention policies set
- [ ] Compression enabled
- [ ] Batching optimized

### Testing ✅
- [ ] Unit tests for metrics/spans
- [ ] Integration tests end-to-end
- [ ] Load testing performed
- [ ] Chaos testing (collector/backend failures)

---

## 🎓 Next Steps

1. **For Development:**
   - Use debug exporter to see all data
   - 100% sampling to see everything
   - Verbose logging

2. **For Staging:**
   - Enable sampling (10-20%)
   - Test with production-like load
   - Verify alerts trigger correctly

3. **For Production:**
   - Optimize sampling (1-5%)
   - Enable all security features
   - Monitor collector health
   - Set up on-call alerts

**This codebase is production-ready with these considerations applied!** 🚀
