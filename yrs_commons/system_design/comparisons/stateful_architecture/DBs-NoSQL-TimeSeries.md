# Time Series Database Comparison

## Table 1: Core Characteristics

| Database | Data Structures Used | Real-World Application | Why It's Used |
|----------|---------------------|------------------------|---------------|
| InfluxDB | TSM (Time-Structured Merge) tree, inverted index | IoT monitoring, DevOps metrics, real-time analytics | Purpose-built for time series, InfluxQL, high ingestion |
| TimescaleDB | PostgreSQL extension, hypertables, chunks | Financial data, IoT, business metrics | Full SQL support, PostgreSQL ecosystem, compression |
| Prometheus | Custom time series storage, LevelDB index | Kubernetes monitoring, system metrics, alerting | Pull-based model, built-in alerting, cloud-native |
| Apache Druid | Column-oriented, segment files, bitmap indexes | Real-time analytics, user behavior, advertising | Sub-second queries, high concurrency, rollups |
| OpenTSDB | HBase storage, time-based keys | Large-scale metrics, infrastructure monitoring | HBase scale, tags-based model, long retention |

## Use Cases Description

### InfluxDB
- **IoT Monitoring**: Sensor data, device telemetry
- **Application Performance**: APM metrics, custom metrics
- **Financial Markets**: Tick data, real-time prices
- **Infrastructure Monitoring**: Server metrics, network data

### TimescaleDB
- **Financial Analysis**: Trading data, portfolio analytics
- **IoT Analytics**: Complex queries on sensor data
- **Business Intelligence**: Time-based business metrics
- **Geospatial Time Series**: Location tracking over time

### Prometheus
- **Kubernetes Monitoring**: Container and cluster metrics
- **Microservices**: Service mesh observability
- **SRE/DevOps**: SLI/SLO tracking, alerting
- **Application Metrics**: Custom application monitoring

### Apache Druid
- **User Analytics**: Clickstream, user behavior analysis
- **Digital Advertising**: Ad performance, real-time bidding
- **Network Telemetry**: Flow analysis, security monitoring
- **Gaming Analytics**: Player behavior, real-time dashboards

### OpenTSDB
- **Large Infrastructure**: Data center monitoring at scale
- **Telecommunications**: Network performance metrics
- **Scientific Computing**: Experiment data collection
- **Industrial IoT**: Manufacturing sensor networks

## Table 2: CA Systems (Consistency + Availability)

| Database | CAP Classification | Characteristics |
|----------|-------------------|-----------------|
| InfluxDB | CA (single node), AP (clustered) | Eventually consistent in cluster mode |
| TimescaleDB | CA (follows PostgreSQL) | Strong consistency with PostgreSQL ACID |
| Prometheus | CA (single node) | No built-in clustering, federation for scale |
| Apache Druid | AP (distributed) | Eventually consistent, availability focused |
| OpenTSDB | CP (HBase backend) | Inherits HBase consistency model |

## Table 3: CP Systems (Consistency + Partition Tolerance)

| Database | Configuration | Trade-offs |
|----------|--------------|------------|
| InfluxDB | Single node only | No partition tolerance in CP mode |
| TimescaleDB | Synchronous replication | Standard PostgreSQL trade-offs |
| Prometheus | Not distributed | Single node consistency only |
| Apache Druid | Not typical usage | Designed for availability |
| OpenTSDB | Default (via HBase) | May be unavailable during HBase issues |

## Table 4: PA Systems (Partition Tolerance + Availability)

| Database | Configuration | Trade-offs |
|----------|--------------|------------|
| InfluxDB | Enterprise clustering | Eventual consistency, potential data gaps |
| TimescaleDB | Async replication | PostgreSQL streaming replication lag |
| Prometheus | Federation | Independent instances, no consistency |
| Apache Druid | Default operation | Query-time consistency issues possible |
| OpenTSDB | HBase eventually consistent | Depends on HBase configuration |

## Volume Considerations

| Aspect | InfluxDB | TimescaleDB | Prometheus | Apache Druid | OpenTSDB |
|--------|----------|-------------|-------------|--------------|----------|
| **Sweet Spot** | 1TB-10TB | 10GB-100TB | 100GB-1TB | 1TB-100TB | 10TB-1PB |
| **Compression Ratio** | 10-100x | 10-20x | 1.3-2x | 10-40x | HBase compression |
| **Retention Management** | Automatic policies | PostgreSQL partitioning | Time-based blocks | Segment management | HBase TTL |
| **Points/Second Ingestion** | 1M+ (clustered) | 100K-1M | 1M+ samples | 1M+ events | 100K+ (HBase limited) |
| **Key Difference** | Best compression | SQL flexibility | Operational simplicity | Analytics optimized | Massive scale |

## Latency Requirements

| Aspect | InfluxDB | TimescaleDB | Prometheus | Apache Druid | OpenTSDB |
|--------|----------|-------------|-------------|--------------|----------|
| **Write Latency** | <1ms | 1-10ms | <1ms (batch) | 1-10ms | 10-100ms |
| **Simple Query** | 1-10ms | 1-100ms | 1-10ms | <100ms | 10-1000ms |
| **Complex Analytics** | 10-1000ms | 10-1000ms | Not designed for | 100-1000ms | Seconds |
| **Real-time View** | Immediate | Immediate | 15s-2min scrape | <1min segments | Near real-time |
| **Key Difference** | Fast simple queries | Full SQL power | Pull-based delay | Best analytics speed | HBase overhead |

## Read/Write Workload Patterns

| Aspect | InfluxDB | TimescaleDB | Prometheus | Apache Druid | OpenTSDB |
|--------|----------|-------------|-------------|--------------|----------|
| **Write Pattern** | Line protocol, HTTP/UDP | SQL INSERT, COPY | Pull scraping | Streaming/batch | HTTP/Telnet API |
| **Write Optimization** | TSM engine | Hypertable chunks | Append-only blocks | Immutable segments | HBase writes |
| **Query Optimization** | Time-range focused | B-tree + chunk exclusion | Time-series specific | Pre-aggregation | Tag-based queries |
| **Downsampling** | Continuous queries | Continuous aggregates | Recording rules | Rollup at ingest | Pre-aggregation |
| **Key Difference** | Purpose-built writes | PostgreSQL flexibility | Pull vs push | Real-time rollups | Tag-centric model |

## Data Structure Requirements

| Aspect | InfluxDB | TimescaleDB | Prometheus | Apache Druid | OpenTSDB |
|--------|----------|-------------|-------------|--------------|----------|
| **Data Model** | Measurements, tags, fields | Tables with time column | Metrics with labels | Datasources, dimensions | Metrics with tags |
| **Schema** | Schema-less | Schema-full (SQL) | Flexible labels | Semi-structured | Schema-less tags |
| **Supported Types** | Float, int, string, boolean | All PostgreSQL types | Float64 only | Various types | Numeric only |
| **Metadata** | Tags (indexed) | Regular columns | Labels | Dimensions | Tags (indexed) |
| **Key Difference** | Flexible fields | Rich SQL types | Simple but powerful | Analytics-focused | Tag-based design |

## Consistency & Availability Requirements

| Aspect | InfluxDB | TimescaleDB | Prometheus | Apache Druid | OpenTSDB |
|--------|----------|-------------|-------------|--------------|----------|
| **Consistency Model** | Eventual (clustered) | Strong (PostgreSQL) | Single node | Eventually consistent | HBase consistency |
| **Replication** | Enterprise feature | PostgreSQL replication | None built-in | Segment replication | HBase replication |
| **High Availability** | Enterprise clustering | PostgreSQL HA | Federation only | Built-in HA | HBase HA |
| **Backup Strategy** | Snapshots | pg_dump, WAL | Snapshots | Deep storage | HBase backup |
| **Key Difference** | Commercial HA | Mature PostgreSQL | Simple operational | Distributed by design | Depends on HBase |

## Replication & Distribution Techniques

| Aspect | InfluxDB | TimescaleDB | Prometheus | Apache Druid | OpenTSDB |
|--------|----------|-------------|-------------|--------------|----------|
| **Sharding** | By time range | PostgreSQL sharding | Federation (manual) | Automatic by time | HBase regions |
| **Distribution** | Hash + time | Distributed hypertables | Independent instances | Segment distribution | HBase distribution |
| **Multi-DC** | Enterprise feature | PostgreSQL solutions | Federation | Multi-tier storage | HBase multi-DC |
| **Load Balancing** | Built-in (Enterprise) | External required | External required | Built-in | HBase balancing |
| **Key Difference** | Time-based sharding | PostgreSQL-based | Manual federation | Automatic distribution | HBase handles it |

## Conflict Resolution Strategies

| Aspect | InfluxDB | TimescaleDB | Prometheus | Apache Druid | OpenTSDB |
|--------|----------|-------------|-------------|--------------|----------|
| **Duplicate Points** | Last write wins | PostgreSQL constraints | Last scrape wins | Handled at ingestion | Last write wins |
| **Late Arrival** | Accepted within window | Always accepted | Rejected (2 hours) | Reprocessing possible | Accepted |
| **Resolution Method** | Timestamp-based | SQL constraints | Scrape-based | Ingestion rules | HBase versioning |
| **Out-of-Order** | Limited support | Full support | Not supported | Batch reindexing | Supported |
| **Key Difference** | Time windows | Full flexibility | Strict time order | Batch corrections | HBase flexibility |

## Scaling Approaches

| Aspect | InfluxDB | TimescaleDB | Prometheus | Apache Druid | OpenTSDB |
|--------|----------|-------------|-------------|--------------|----------|
| **Vertical Scaling** | Effective | Very effective | Limited by design | Good for historicals | HBase dependent |
| **Horizontal Scaling** | Enterprise only | Multi-node | Federation | Native distribution | HBase scaling |
| **Auto-scaling** | InfluxDB Cloud | Manual | Manual | Manual | Manual |
| **Query Parallelism** | Limited | PostgreSQL parallel | Single-threaded | Highly parallel | HBase scans |
| **Key Difference** | Commercial scaling | PostgreSQL methods | Federation only | Built for scale | HBase linear scale |

## Operational Considerations

| Aspect | InfluxDB | TimescaleDB | Prometheus | Apache Druid | OpenTSDB |
|--------|----------|-------------|-------------|--------------|----------|
| **Setup Complexity** | Low | Low-Medium | Very Low | High | High |
| **Management Overhead** | Low | Medium (PostgreSQL) | Very Low | High | High (HBase) |
| **Resource Usage** | Moderate | Higher (PostgreSQL) | Very efficient | High | High (JVM+HBase) |
| **Monitoring Tools** | Built-in UI | PostgreSQL tools | Built-in expression browser | Built-in console | Basic UI |
| **Key Difference** | Purpose-built simplicity | PostgreSQL ecosystem | Simplest operation | Complex but powerful | HBase complexity |

## Decision Matrix for Common Use Cases

| Use Case | Best Choice | Why | Avoid | Why Not |
|----------|-------------|-----|-------|---------|
| **Container Monitoring** | Prometheus | Native Kubernetes support | OpenTSDB | Operational overhead |
| **IoT Sensor Data** | InfluxDB | Purpose-built, compression | Prometheus | Not for event data |
| **Financial Time Series** | TimescaleDB | SQL analytics, ACID | Prometheus | No complex queries |
| **Real-time Analytics** | Apache Druid | Sub-second queries | OpenTSDB | Query performance |
| **Long-term Storage** | TimescaleDB/OpenTSDB | Compression/scale | Prometheus | Limited retention |
| **DevOps Metrics** | Prometheus | Alerting, ecosystem | Druid | Operational complexity |
| **Ad-hoc Analysis** | TimescaleDB | Full SQL | Prometheus | Limited query language |
| **High Cardinality** | InfluxDB | Designed for it | Prometheus | Memory issues |
| **Clickstream Analytics** | Apache Druid | Real-time OLAP | InfluxDB | Not optimized for OLAP |
| **Network Flow Data** | OpenTSDB/Druid | Scale requirements | Prometheus | Volume limitations |

## Key Differentiators Summary

### InfluxDB
- **Strengths**: Purpose-built for time series, great compression, high cardinality support
- **Weaknesses**: Limited query language, clustering is commercial, no joins
- **Choose when**: Need dedicated time series database, high cardinality metrics

### TimescaleDB
- **Strengths**: Full SQL, PostgreSQL ecosystem, ACID compliance, complex queries
- **Weaknesses**: Higher resource usage, PostgreSQL limitations at extreme scale
- **Choose when**: Need SQL analytics, complex queries, existing PostgreSQL investment

### Prometheus
- **Strengths**: Cloud-native standard, built-in alerting, pull model, simple operation
- **Weaknesses**: Limited storage, no distributed model, basic query language
- **Choose when**: Kubernetes monitoring, operational metrics, alerting focus

### Apache Druid
- **Strengths**: Real-time OLAP, sub-second queries, high concurrency, pre-aggregation
- **Weaknesses**: Complex operations, high resource usage, learning curve
- **Choose when**: Real-time analytics dashboards, user-facing analytics, high concurrency

### OpenTSDB
- **Strengths**: Massive scale via HBase, proven at scale, tag-based model
- **Weaknesses**: HBase complexity, slower queries, dated architecture
- **Choose when**: Petabyte scale needed, existing HBase infrastructure

## Architecture Decision Points

**Choose based on:**
1. **Query Complexity**: TimescaleDB > Druid > InfluxDB > OpenTSDB > Prometheus
2. **Operational Simplicity**: Prometheus > InfluxDB > TimescaleDB > OpenTSDB > Druid
3. **Ingestion Scale**: Druid = InfluxDB > Prometheus > OpenTSDB > TimescaleDB
4. **Analytics Performance**: Druid > TimescaleDB > InfluxDB > OpenTSDB > Prometheus
5. **Ecosystem/Standards**: Prometheus (cloud-native) > TimescaleDB (SQL) > Others

## Real-World Time Series Database Use Cases

### InfluxDB Real-World Implementations

| Company/Organization | Use Case | Why InfluxDB | Scale/Impact |
|---------------------|----------|--------------|--------------|
| **Tesla** | Vehicle telemetry, manufacturing metrics | High cardinality, real-time ingestion | 1M+ vehicles, billions of points/day |
| **Cisco** | Network device monitoring | Tag-based model, compression | 100K+ devices globally |
| **Hulu** | Streaming quality metrics, CDN monitoring | Real-time dashboards, alerting | 45M+ subscribers |
| **eBay** | Application performance monitoring | High ingestion rate, Telegraf integration | 1B+ listings monitoring |
| **IBM** | IoT platform metrics | Purpose-built for IoT, scalability | Enterprise IoT deployments |
| **PayPal** | Transaction metrics, system monitoring | Fast queries, downsampling | 400M+ users |

**Key Pattern**: InfluxDB dominates IoT, APM, and high-cardinality metrics use cases.

### TimescaleDB Real-World Implementations

| Company/Organization | Use Case | Why TimescaleDB | Scale/Impact |
|---------------------|----------|-----------------|--------------|
| **Aiven** | Database metrics platform | PostgreSQL features, compression | 1T+ data points/month |
| **Digital Ocean** | Infrastructure monitoring | SQL queries, PostgreSQL ecosystem | 600K+ customers |
| **Outbrain** | Content recommendation metrics | Complex analytics, joins | 1B+ recommendations/day |
| **Messari** | Cryptocurrency market data | Financial queries, ACID | Real-time crypto analytics |
| **Tempo** | Workforce analytics | Business intelligence queries | Enterprise scale |
| **Con Edison** | Smart meter data | Geospatial + time series | 3M+ customers NYC |

**Key Pattern**: TimescaleDB chosen when SQL analytics and complex queries are required.

### Prometheus Real-World Implementations

| Company/Organization | Use Case | Why Prometheus | Scale/Impact |
|---------------------|----------|----------------|--------------|
| **Kubernetes (all users)** | Container and cluster monitoring | Native integration, standard | Powers millions of clusters |
| **SoundCloud** | Microservices monitoring | Built Prometheus, pull model | 175M+ users |
| **Uber** | Infrastructure monitoring | Scalable federation, alerting | 25K+ microservices |
| **Spotify** | Service monitoring, SLOs | Cloud-native, reliable | 500M+ users |
| **GitLab** | CI/CD monitoring, GitLab.com | Kubernetes native, simple | 30M+ registered users |
| **Robinhood** | Trading platform monitoring | Real-time alerting | 22M+ funded accounts |

**Key Pattern**: Prometheus is the de facto standard for Kubernetes and cloud-native monitoring.

### Apache Druid Real-World Implementations

| Company/Organization | Use Case | Why Druid | Scale/Impact |
|---------------------|----------|-----------|--------------|
| **Netflix** | Real-time analytics, A/B testing | Sub-second queries, scale | 230M+ subscribers |
| **Airbnb** | User behavior analytics, metrics | Interactive dashboards | 150M+ users |
| **Walmart** | Real-time inventory analytics | High concurrency, fast queries | $600B+ annual revenue |
| **Yahoo** | Ad analytics, user analytics | Created Druid, massive scale | Billions of events/day |
| **Cisco** | Network flow analytics | Real-time analysis, rollups | Enterprise networks |
| **Pinterest** | User engagement metrics | Real-time dashboards | 450M+ monthly users |

**Key Pattern**: Druid excels at real-time analytics dashboards and user-facing analytics applications.

### OpenTSDB Real-World Implementations

| Company/Organization | Use Case | Why OpenTSDB | Scale/Impact |
|---------------------|----------|--------------|--------------|
| **Yahoo** | Infrastructure monitoring at scale | HBase scale, long retention | 100K+ servers |
| **Box** | Service metrics, monitoring | Tag-based flexibility | 100M+ users |
| **Arista Networks** | Network telemetry | High volume ingestion | Network infrastructure |
| **StumbleUpon** | User activity metrics | Created OpenTSDB | Historical (acquired) |
| **Ticketmaster** | Event platform monitoring | Scale for traffic spikes | Major events |
| **MapR** | Cluster monitoring | HBase integration | Big data clusters |

**Key Pattern**: OpenTSDB used for massive-scale infrastructure monitoring with HBase deployments.

## Industry-Specific Patterns

### Cloud Infrastructure
- **Container Monitoring**: Prometheus (industry standard)
- **VM/Server Metrics**: InfluxDB, Prometheus
- **Multi-cloud**: TimescaleDB (portable)
- **Massive Scale**: OpenTSDB

### IoT & Manufacturing
- **Sensor Data**: InfluxDB (purpose-built)
- **Industrial IoT**: TimescaleDB (SQL analytics)
- **Real-time Dashboards**: Druid
- **Long-term Storage**: OpenTSDB

### Financial Services
- **Market Data**: TimescaleDB (SQL, ACID)
- **Trading Metrics**: InfluxDB (low latency)
- **Risk Analytics**: Druid (real-time)
- **Compliance Storage**: TimescaleDB

### Digital Advertising
- **Ad Performance**: Druid (Yahoo, others)
- **Campaign Analytics**: Druid
- **Publisher Metrics**: InfluxDB
- **Long-term Analysis**: TimescaleDB

### DevOps/SRE
- **Kubernetes**: Prometheus (native)
- **Application Metrics**: Prometheus, InfluxDB
- **SLO/SLI Tracking**: Prometheus
- **Custom Metrics**: InfluxDB

## Performance Characteristics

### InfluxDB
- **Tesla**: Ingesting billions of points/day
- **Compression**: 10-100x typical
- **Query Speed**: 1-10ms for simple queries

### TimescaleDB
- **Compression**: 95%+ with columnar
- **Complex Queries**: Full SQL performance
- **Scale**: 100TB+ deployments

### Prometheus
- **Efficiency**: 1-2 bytes per sample
- **Scraping**: 1M+ samples/second
- **Query**: Optimized for operational queries

### Apache Druid
- **Netflix**: Sub-second on billions of rows
- **Concurrency**: 1000s of concurrent queries
- **Ingestion**: 1M+ events/second

### OpenTSDB
- **Yahoo**: 100K+ servers monitored
- **Retention**: Years of data
- **Scale**: Petabyte-scale possible

The choice depends on:
- **Kubernetes/Cloud-Native**: Prometheus
- **SQL Requirements**: TimescaleDB
- **IoT/High Cardinality**: InfluxDB
- **Real-time Analytics**: Apache Druid
- **Massive Scale**: OpenTSDB with HBase
