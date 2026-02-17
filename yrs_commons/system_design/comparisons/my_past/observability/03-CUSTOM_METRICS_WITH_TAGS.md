# Custom Metrics with Multiple Tags in OpenTelemetry

## Overview
In OpenTelemetry, **tags are called "Attributes"**. They work just like:
- AWS CloudWatch **Dimensions**
- New Relic **Tags**
- Datadog **Tags**
- Prometheus **Labels**

## Attribute Types

OpenTelemetry supports different attribute types:

```java
// String attributes (most common)
AttributeKey<String> ATTR_REGION = AttributeKey.stringKey("region");
AttributeKey<String> ATTR_STATUS = AttributeKey.stringKey("status");

// Numeric attributes
AttributeKey<Long> ATTR_USER_ID = AttributeKey.longKey("user_id");
AttributeKey<Double> ATTR_PRICE = AttributeKey.doubleKey("price");

// Boolean attributes
AttributeKey<Boolean> ATTR_IS_PREMIUM = AttributeKey.booleanKey("is_premium");

// Array attributes
AttributeKey<List<String>> ATTR_TAGS = AttributeKey.stringArrayKey("tags");
```

## Ways to Add Multiple Attributes

### Method 1: Using Attributes.builder() (Recommended for Multiple Tags)

```java
// Best for 3+ attributes
doWorkHistogram.record(
    sleepTime,
    Attributes.builder()
        .put(ATTR_METHOD, "GET")
        .put(ATTR_ENDPOINT, "/ping")
        .put(ATTR_STATUS, "success")
        .put(ATTR_REGION, "us-east-1")
        .put(ATTR_USER_ID, 1234L)
        .put(ATTR_IS_PREMIUM, true)
        .build());
```

### Method 2: Using Attributes.of() (For 1-5 Attributes)

```java
// For 2-5 attributes
requestCounter.add(1,
    Attributes.of(
        ATTR_ENDPOINT, "/ping",
        ATTR_STATUS, "success",
        ATTR_REGION, "us-east-1"));
```

### Method 3: Creating Reusable Attribute Sets

```java
// Define common attributes once
Attributes commonAttrs = Attributes.builder()
    .put(ATTR_SERVICE, "payment-service")
    .put(ATTR_VERSION, "1.0.0")
    .put(ATTR_ENVIRONMENT, "production")
    .build();

// Combine with request-specific attributes
requestCounter.add(1,
    Attributes.builder()
        .putAll(commonAttrs)  // Add common attributes
        .put(ATTR_ENDPOINT, "/pay")
        .put(ATTR_STATUS, "success")
        .build());
```

## Complete Example: All Metric Types

### 1. Histogram (Response Time, Request Duration)

```java
LongHistogram responseTimeHistogram = meter
    .histogramBuilder("http.server.duration")
    .setDescription("HTTP server request duration")
    .setUnit("ms")
    .ofLongs()
    .build();

// Record with multiple tags
responseTimeHistogram.record(
    durationMs,
    Attributes.builder()
        .put("http.method", "POST")
        .put("http.route", "/api/users")
        .put("http.status_code", 200)
        .put("region", "us-east-1")
        .put("availability_zone", "us-east-1a")
        .build());
```

### 2. Counter (Request Count, Error Count)

```java
LongCounter requestCounter = meter
    .counterBuilder("http.server.request.count")
    .setDescription("Total HTTP requests")
    .setUnit("requests")
    .build();

// Increment with tags
requestCounter.add(1,
    Attributes.builder()
        .put("http.method", "GET")
        .put("http.route", "/api/products")
        .put("http.status_code", 200)
        .put("region", "us-west-2")
        .put("customer_tier", "premium")
        .build());
```

### 3. Gauge (Active Connections, Memory Usage)

```java
private final AtomicLong activeConnections = new AtomicLong(0);

// Gauge automatically reports current value
meter.gaugeBuilder("system.active.connections")
    .setDescription("Number of active connections")
    .setUnit("connections")
    .buildWithCallback(measurement -> {
        measurement.record(
            activeConnections.get(),
            Attributes.builder()
                .put("pool", "database")
                .put("database", "postgres")
                .put("region", "us-east-1")
                .build());
    });
```

### 4. UpDownCounter (Queue Size, Items in Cart)

```java
LongUpDownCounter queueSizeCounter = meter
    .upDownCounterBuilder("queue.size")
    .setDescription("Current queue size")
    .setUnit("items")
    .build();

// Can go up or down
queueSizeCounter.add(1, Attributes.of("queue", "orders", "priority", "high"));
queueSizeCounter.add(-1, Attributes.of("queue", "orders", "priority", "high"));
```

## Querying Metrics with Tags in Groundcover

Once your metrics are in groundcover, you can:

### Filter by Tags
```
metric: do-work
where: region = "us-east-1" AND is_premium = true
```

### Group by Tags
```
metric: request.count
group by: region, status
aggregation: sum
```

### Create Dashboards
- Split metrics by region
- Compare premium vs free users
- Track errors by endpoint
- Monitor performance by availability zone

## Best Practices

### 1. **Use Meaningful Tag Names**
```java
// Good
.put("http.status_code", 200)
.put("region", "us-east-1")
.put("customer_tier", "premium")

// Bad
.put("sc", 200)
.put("r", "us1")
.put("t", "p")
```

### 2. **Keep Cardinality Low**
```java
// Good - Low cardinality (few unique values)
.put("status", "success")           // 2-3 values
.put("region", "us-east-1")         // 10-20 values
.put("http.method", "GET")          // 5-10 values

// Bad - High cardinality (many unique values)
.put("user_id", userId)             // Millions of values ❌
.put("timestamp", timestamp)        // Infinite values ❌
.put("request_id", requestId)       // Millions of values ❌
```

### 3. **Use Consistent Naming**
```java
// Follow OpenTelemetry semantic conventions
"http.method"           // Use standard names
"http.status_code"
"http.route"
"db.system"
"db.operation"
```

### 4. **Tag Reuse**
```java
// Create common attribute sets
private static final Attributes SERVICE_ATTRS = Attributes.builder()
    .put("service.name", "payment-api")
    .put("service.version", "2.1.0")
    .put("deployment.environment", "production")
    .build();

// Reuse across metrics
histogram.record(value,
    Attributes.builder()
        .putAll(SERVICE_ATTRS)
        .put("operation", "charge")
        .build());
```

## Comparison with Other Platforms

| Platform | Term | Example |
|----------|------|---------|
| **OpenTelemetry** | Attributes | `.put("region", "us-east-1")` |
| **AWS CloudWatch** | Dimensions | `Dimension("Region", "us-east-1")` |
| **New Relic** | Tags | `tag("region", "us-east-1")` |
| **Datadog** | Tags | `tag("region:us-east-1")` |
| **Prometheus** | Labels | `{region="us-east-1"}` |

## Real-World Example: E-Commerce Application

```java
@RestController
public class CheckoutController {

    private final LongHistogram checkoutDuration;
    private final LongCounter checkoutCounter;
    private final Meter meter;

    public CheckoutController(Meter meter) {
        this.meter = meter;

        checkoutDuration = meter
            .histogramBuilder("checkout.duration")
            .setDescription("Checkout processing time")
            .setUnit("ms")
            .ofLongs()
            .build();

        checkoutCounter = meter
            .counterBuilder("checkout.count")
            .setDescription("Total checkouts")
            .build();
    }

    @PostMapping("/checkout")
    public Response checkout(@RequestBody Order order) {
        long startTime = System.currentTimeMillis();
        String paymentMethod = order.getPaymentMethod();
        String customerTier = order.getCustomer().getTier();
        String region = order.getShippingAddress().getRegion();

        try {
            processCheckout(order);
            long duration = System.currentTimeMillis() - startTime;

            // Record success metrics with rich tags
            Attributes successAttrs = Attributes.builder()
                .put("payment.method", paymentMethod)
                .put("customer.tier", customerTier)
                .put("region", region)
                .put("status", "success")
                .put("order.value.bucket", getValueBucket(order.getTotal()))
                .build();

            checkoutDuration.record(duration, successAttrs);
            checkoutCounter.add(1, successAttrs);

            return Response.success();

        } catch (Exception e) {
            long duration = System.currentTimeMillis() - startTime;

            // Record failure metrics
            Attributes failureAttrs = Attributes.builder()
                .put("payment.method", paymentMethod)
                .put("customer.tier", customerTier)
                .put("region", region)
                .put("status", "failure")
                .put("error.type", e.getClass().getSimpleName())
                .build();

            checkoutDuration.record(duration, failureAttrs);
            checkoutCounter.add(1, failureAttrs);

            throw e;
        }
    }

    private String getValueBucket(double total) {
        if (total < 50) return "0-50";
        if (total < 200) return "50-200";
        if (total < 500) return "200-500";
        return "500+";
    }
}
```

## Summary

**Key Points:**
1. ✅ Use `Attributes.builder()` for multiple tags
2. ✅ Support for String, Long, Double, Boolean, Array types
3. ✅ Keep cardinality low (avoid user IDs, timestamps)
4. ✅ Use semantic conventions for standard attributes
5. ✅ Works with all metric types (Histogram, Counter, Gauge)
6. ✅ Tags automatically sent to groundcover for filtering/grouping
7. ✅ Same collector-based approach with authentication works perfectly
