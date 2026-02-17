# OpenTelemetry Java Agent Example

This example demonstrates simple usage of the OpenTelemetry Java Agent published
by [opentelemetry-java-instrumentation](https://github.com/open-telemetry/opentelemetry-java-instrumentation).

It consists of a Spring Boot application with:

- A Gradle task for downloading the OpenTelemetry Java Agent
- A simple web API available at `GET http://localhost:8080/ping`. When called,
  auto-instrumentation from the OpenTelemetry Java Agent records spans and
  metrics. Additionally, there is manual trace and metric instrumentation, as
  well as application logging performed in the context of traces using the Log4j
  API
- A Docker Compose setup configured to run the application and export to
  the [Collector](https://opentelemetry.io/docs/collector/) via OTLP
- The Collector is configured with
  the [OTLP receiver](https://github.com/open-telemetry/opentelemetry-collector/tree/main/receiver/otlpreceiver)
  and exports to standard out with
  the [logging exporter](https://github.com/open-telemetry/opentelemetry-collector/tree/main/exporter/debugexporter)

---

## Documentation Guide

This project includes a series of guides that walk through observability concepts, progressing from fundamentals to platform-level design decisions. The documents are numbered to reflect a natural learning path:

| # | Document | What It Covers | Thought Process |
|---|----------|---------------|-----------------|
| 01 | [README](./01-README.md) (this file) | Project setup, how to run | _"How do I get this running?"_ |
| 02 | [Observability Guide](./02-OBSERVABILITY_GUIDE.md) | All metric types, traces, logs fundamentals | _"What are the building blocks of observability?"_ |
| 03 | [Custom Metrics with Tags](./03-CUSTOM_METRICS_WITH_TAGS.md) | Attributes, tags, dimensions, cardinality | _"How do I slice metrics by business dimensions?"_ |
| 04 | [OpenTelemetry Architecture](./04-OPENTELEMETRY_ARCHITECTURE.md) | SDK, Collector, exporters, sampling, context propagation | _"How do all the OTel components fit together?"_ |
| 05 | [OpenTelemetry vs Backends](./05-OPENTELEMETRY_VS_BACKENDS.md) | Groundcover, Grafana, Datadog, New Relic comparison | _"OTel collects data -- but where does it go? How do backends differ?"_ |
| 06 | [Production Practices](./06-OBSERVABILITY_REMAINING_MISC.md) | Security, troubleshooting, cost optimization, testing | _"What breaks in production and how do I prevent it?"_ |
| 07 | [Groundcover APM Deep Dive](./07-GROUNDCOVER_APM.md) | eBPF-based monitoring, service maps, APM capabilities | _"What can Groundcover see without any code changes?"_ |
| 08 | [Metrics Granularity Pipeline](./08-METRICS_GRANULARITY_PIPELINE.md) | Data fidelity loss at each pipeline stage: facade, wire, storage, query | _"What information gets lost as metrics flow through the pipeline, and why?"_ |

### How to read these docs

**If you're new to observability:** Start with 02, then 03, then 04. This gives you the vocabulary.

**If you're evaluating backends:** Jump to 05 for the comparison matrix, then 07 for the Groundcover deep dive.

**If you're a platform engineer deciding on metrics strategy:** Start with 08. It explains the trade-offs that matter when designing an observability product -- what gets lost at each pipeline stage, why each layer made that design choice, and what it means for your dashboards and alerts.

**If you're migrating from New Relic / CloudWatch:** Read 08 first (to understand what changes), then 04 (to understand OTel architecture), then 06 (for production readiness).

---

## Prerequisites

* Java 17 or higher is required to build and run this example
* Docker Compose

## How to Run

Build the application jar:

```shell
../gradlew bootJar
```

Run the application and the Collector with Docker Compose:

```shell
docker compose up --build
```

In a separate shell, exercise the application by calling its endpoint:

```shell
curl http://localhost:8080/ping
```

Watch for spans, metrics, and logs in the Collector log output.

## Declarative Configuration

By default, this example uses the [environment variable configuration schema](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/configuration/sdk-environment-variables.md) to configure the SDK. However, it also includes [sdk-config.yaml](./sdk-config.yaml) which demonstrates how the [declarative configuration](https://opentelemetry.io/docs/specs/otel/configuration/#declarative-configuration) scheme can be used to configure the SDK based on a YAML configuration file instead.

`sdk-config.yaml` extends the [opentelemetry-configuration sdk-config.yaml](https://github.com/open-telemetry/opentelemetry-configuration/blob/v0.3.0/examples/sdk-config.yaml) template, demonstrating:

- Configuration of instrumentation (see `.instrumentation.java`)
- Configuration of [rule-based routing sampler](https://github.com/open-telemetry/opentelemetry-java-contrib/tree/main/samplers) (see `.tracer_provider.sampler.parent_based.root`)

To use declarative configuration instead of the environment variable scheme, add the following before starting the application and Collector:

```shell
export OTEL_EXPERIMENTAL_CONFIG_FILE=/sdk-config.yaml
```

Note: toggling declarative configuration causes the env var configuration scheme to be ignored completely. However, there is support for [env var substitution](https://opentelemetry.io/docs/specs/otel/configuration/data-model/#environment-variable-substitution) within configuration files.
