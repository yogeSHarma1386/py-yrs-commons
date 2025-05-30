# Column-Family Store Database Comparison

## Table 1: Core Characteristics

| Database | Data Structures Used | Real-World Application | Why It's Used |
|----------|---------------------|------------------------|---------------|
| Apache Cassandra | LSM tree, SSTables, Bloom filters | Time-series, IoT data, messaging | Linear scalability, no SPOF, multi-DC |
| HBase | LSM tree, HDFS storage, WAL | Analytics, data lakes, ML features | Hadoop integration, strong consistency, massive scale |
| Amazon DynamoDB | B-tree indexes, proprietary storage | IoT telemetry, user activity, gaming | Serverless, predictable performance, managed |
| ScyllaDB | LSM tree (C++ rewrite), shard-per-core | Real-time big data, AdTech, gaming | Cassandra-compatible, extreme performance |
| Apache Accumulo | LSM tree, HDFS, cell-level security | Government, intelligence, secure analytics | Cell-level security, iterators, NSA heritage |

## Use Cases Description

### Apache Cassandra
- **Time-Series Data**: Metrics, logs, IoT sensor readings
- **Message History**: Chat applications, activity feeds
- **Recommendation Data**: User interactions, product views
- **Session Storage**: Distributed session management

### HBase
- **Data Lake Storage**: Raw data for analytics pipelines
- **Machine Learning Features**: Feature stores for ML models
- **Graph Data**: Adjacency lists for large graphs
- **Content Management**: Large-scale content indexing

### Amazon DynamoDB
- **IoT Time-Series**: Device telemetry with TTL
- **User Activity Tracking**: Clickstreams, user events
- **Gaming Event Logs**: Player actions, achievements
- **Audit Trails**: Compliance logging with retention

### ScyllaDB
- **Real-time Analytics**: Fraud detection, monitoring
- **AdTech Platforms**: Bid streams, impression tracking
- **Cryptocurrency**: Transaction history, order books
- **Time-Series at Scale**: When Cassandra isn't fast enough

### Apache Accumulo
- **Intelligence Analytics**: Classified data processing
- **Healthcare Analytics**: HIPAA-compliant data lakes
- **Financial Compliance**: Audit trails with security labels
- **Genomics Research**: Secured research data

## Table 2: CA Systems (Consistency + Availability)

| Database | CAP Classification | Characteristics |
|----------|-------------------|-----------------|
| Cassandra | AP typically, tunable | Eventually consistent by default, QUORUM for CA-like behavior |
| HBase | CP (strong consistency) | Single master per region, consistent reads/writes |
| DynamoDB | Configurable | Eventually consistent default, strong consistency optional |
| ScyllaDB | AP typically, tunable | Same as Cassandra, optimized performance |
| Accumulo | CP (strong consistency) | HBase-like consistency model, HDFS-backed |

## Table 3: CP Systems (Consistency + Partition Tolerance)

| Database | Configuration | Trade-offs |
|----------|--------------|------------|
| Cassandra | LOCAL_QUORUM, EACH_QUORUM | May reject writes/reads during partition |
| HBase | Default operation | Region unavailable during splits/failures |
| DynamoDB | Strong consistency mode | Higher cost, increased latency |
| ScyllaDB | QUORUM consistency | Same as Cassandra, lower latency |
| Accumulo | Default operation | Similar to HBase, tablet server failures |

## Table 4: PA Systems (Partition Tolerance + Availability)

| Database | Configuration | Trade-offs |
|----------|--------------|------------|
| Cassandra | ONE, ANY consistency | May read stale data, high availability |
| HBase | Read replicas (timeline consistent) | Stale reads possible |
| DynamoDB | Eventually consistent reads | Default mode, lowest cost |
| ScyllaDB | ONE, ANY consistency | Same as Cassandra, better performance |
| Accumulo | Not typical configuration | Designed for consistency |

## Volume Considerations

| Aspect | Cassandra | HBase | DynamoDB | ScyllaDB | Accumulo |
|--------|-----------|-------|----------|----------|----------|
| **Sweet Spot** | 100GB - 100TB/node | 1TB - 1PB total | Any size | 100GB - 100TB/node | 100GB - 10TB/node |
| **Max Column Family Size** | Billions of rows | Trillions of rows | 400KB item limit | Billions of rows | Billions of rows |
| **Column Limit** | 2 billion columns/row | Millions practical | 1000 attributes | 2 billion columns/row | Configurable |
| **Storage Model** | SSTables on disk | HDFS files | Managed service | SSTables (optimized) | HDFS files |
| **Key Difference** | Best general purpose | Hadoop ecosystem | Serverless scale | Fastest performance | Security features |

## Latency Requirements

| Aspect | Cassandra | HBase | DynamoDB | ScyllaDB | Accumulo |
|--------|-----------|-------|----------|----------|----------|
| **Read Latency** | 1-10ms typical | 1-100ms | <10ms SLA | <1ms possible | 10-100ms |
| **Write Latency** | 1-10ms typical | 1-50ms | <10ms SLA | <1ms possible | 10-50ms |
| **Scan Performance** | Good with proper design | Excellent (coprocessors) | Limited by design | Excellent | Very good |
| **Secondary Index** | Local indexes | Phoenix SQL layer | GSI separate cost | Local indexes | Accumulo iterators |
| **Key Difference** | Predictable performance | Batch-optimized | Guaranteed SLA | Lowest latency | Security overhead |

## Read/Write Workload Patterns

| Aspect | Cassandra | HBase | DynamoDB | ScyllaDB | Accumulo |
|--------|-----------|-------|----------|----------|----------|
| **Write Optimization** | Excellent (append-only) | Very good (WAL+MemStore) | Excellent (managed) | Best (C++ efficiency) | Good (similar to HBase) |
| **Read Patterns** | Partition key required | Row key or scan | Primary key or index | Same as Cassandra | Row key or scan |
| **Compaction Impact** | Tunable strategies | Major/minor compactions | Managed automatically | Incremental compaction | Similar to HBase |
| **Bulk Loading** | SSTableloader | BulkLoad API | Batch operations | SSTableloader | Bulk import tools |
| **Key Difference** | Write-optimized | Scan-optimized | Zero management | Performance-optimized | Security-aware ops |

## Data Structure Requirements

| Aspect | Cassandra | HBase | DynamoDB | ScyllaDB | Accumulo |
|--------|-----------|-------|----------|----------|----------|
| **Column Families** | Static and dynamic | Flexible columns | Attributes in items | Same as Cassandra | Column visibility labels |
| **Wide Rows** | Excellent support | Excellent support | Limited by 400KB | Excellent support | Excellent support |
| **Time-Series** | Time-based partitions | TTL support | TTL on items | Same as Cassandra | Version iterators |
| **Collections** | Sets, lists, maps | Qualifiers only | Lists, maps, sets | Same as Cassandra | Custom iterators |
| **Key Difference** | CQL abstraction | Raw column access | Document-like model | Cassandra-compatible | Cell-level security |

## Consistency & Availability Requirements

| Aspect | Cassandra | HBase | DynamoDB | ScyllaDB | Accumulo |
|--------|-----------|-------|----------|----------|----------|
| **Consistency Levels** | 9 levels (ANY to ALL) | Strong only | Eventually/Strong | Same as Cassandra | Strong consistency |
| **Multi-DC Support** | Built-in, excellent | Master/slave regions | Global Tables | Built-in, excellent | Similar to HBase |
| **Failover Time** | <30 seconds | 1-3 minutes | Automatic | <30 seconds | 1-3 minutes |
| **Repair Process** | Anti-entropy repair | HDFS handles it | Managed | Self-healing++ | HDFS-based |
| **Key Difference** | Most flexible | Hadoop reliability | Fully managed | Faster recovery | Government-grade |

## Replication & Distribution Techniques

| Aspect | Cassandra | HBase | DynamoDB | ScyllaDB | Accumulo |
|--------|-----------|-------|----------|----------|----------|
| **Partitioning** | Consistent hashing | Region splits | Hash/range keys | Same as Cassandra | Range partitioning |
| **Replication** | N replicas per DC | HDFS replication | Managed 3x | Same as Cassandra | HDFS replication |
| **Topology** | Peer-to-peer | Master/RegionServer | Managed service | Peer-to-peer | Master/TabletServer |
| **Cross-DC** | Multiple strategies | Active/passive | Global Tables | Same as Cassandra | Active/passive |
| **Key Difference** | True masterless | HDFS-dependent | Zero configuration | Better performance | Security-first design |

## Conflict Resolution Strategies

| Aspect | Cassandra | HBase | DynamoDB | ScyllaDB | Accumulo |
|--------|-----------|-------|----------|----------|----------|
| **Write Conflicts** | Last-write-wins | No conflicts (consistent) | Last-write-wins | Last-write-wins | No conflicts |
| **Timestamp Handling** | Client or server | Server-assigned | Server-managed | Same as Cassandra | Server-assigned |
| **Custom Resolution** | Application-level | Not needed | Limited options | Application-level | Not needed |
| **Multi-DC Conflicts** | LWW or custom | Active/passive only | Managed by service | LWW or custom | Active/passive |
| **Key Difference** | Requires planning | Avoids conflicts | Simple approach | Same as Cassandra | Consistency model |

## Scaling Approaches

| Aspect | Cassandra | HBase | DynamoDB | ScyllaDB | Accumulo |
|--------|-----------|-------|----------|----------|----------|
| **Adding Nodes** | Stream data automatically | Add RegionServers | Automatic | Stream data (faster) | Add TabletServers |
| **Linear Scalability** | Excellent proven | Very good | Perfect (managed) | Better than Cassandra | Good |
| **Auto-scaling** | No (manual) | No (manual) | Yes | No (manual) | No |
| **Data Rebalancing** | Automatic (vnodes) | Automatic splits | Automatic | Automatic (faster) | Automatic splits |
| **Key Difference** | Easiest to scale | HDFS complexity | Truly elastic | Fastest rebalancing | Security considerations |

## Operational Considerations

| Aspect | Cassandra | HBase | DynamoDB | ScyllaDB | Accumulo |
|--------|-----------|-------|----------|----------|----------|
| **Complexity** | Medium-High | High | None | Medium | High |
| **JVM Tuning** | Critical | Critical | N/A | Not needed (C++) | Critical |
| **Compaction Tuning** | Important | Important | Automatic | Self-tuning | Important |
| **Monitoring Tools** | DataStax, OSS tools | Ambari, Cloudera | CloudWatch | ScyllaDB Monitoring | Similar to HBase |
| **Key Difference** | Well-documented | Hadoop expertise | Zero operations | Better defaults | Security complexity |

## Decision Matrix for Common Use Cases

| Use Case | Best Choice | Why | Avoid | Why Not |
|----------|-------------|-----|-------|---------|
| **Time-Series Data** | Cassandra/ScyllaDB | Designed for it, TTL support | HBase | More complex for time-series |
| **IoT at Scale** | DynamoDB | Auto-scaling, serverless | Accumulo | Operational overhead |
| **Analytics Pipeline** | HBase | Hadoop integration | DynamoDB | Cost at scale |
| **Real-time AdTech** | ScyllaDB | Lowest latency, high throughput | HBase | Latency requirements |
| **Secure Analytics** | Accumulo | Cell-level security | DynamoDB | Limited security model |
| **Chat History** | Cassandra | Wide rows, global scale | HBase | Complexity for use case |
| **ML Feature Store** | HBase | Spark/Hadoop integration | DynamoDB | Analytics limitations |
| **Gaming Leaderboards** | ScyllaDB/DynamoDB | Performance/serverless | Accumulo | Overkill |
| **Audit Logs** | Accumulo/Cassandra | Security/scale | ScyllaDB | Less mature |
| **Multi-DC Active-Active** | Cassandra | Best multi-DC story | HBase | Active/passive only |

## Key Differentiators Summary

### Apache Cassandra
- **Strengths**: True peer-to-peer, multi-DC excellence, time-series optimized, mature
- **Weaknesses**: JVM tuning complexity, repair overhead, eventual consistency
- **Choose when**: Need multi-DC, time-series data, proven scale

### HBase
- **Strengths**: Hadoop ecosystem, strong consistency, massive scale, coprocessors
- **Weaknesses**: Operational complexity, HDFS dependency, master SPOF
- **Choose when**: Already using Hadoop, need consistency, batch analytics

### Amazon DynamoDB
- **Strengths**: Serverless, auto-scaling, predictable performance, zero ops
- **Weaknesses**: Vendor lock-in, limited queries, cost at scale
- **Choose when**: Want managed service, unpredictable load, AWS native

### ScyllaDB
- **Strengths**: C++ performance, Cassandra compatible, self-tuning, lowest latency
- **Weaknesses**: Smaller community, fewer tools, less mature
- **Choose when**: Need maximum performance, migrating from Cassandra

### Apache Accumulo
- **Strengths**: Cell-level security, iterators, government proven, fine-grained access
- **Weaknesses**: Smaller community, complex operations, HDFS dependency
- **Choose when**: Security requirements, compliance needs, intelligence workloads

## Architecture Decision Points

**Choose based on:**
1. **Performance Needs**: ScyllaDB > Cassandra > DynamoDB > Accumulo > HBase
2. **Operational Simplicity**: DynamoDB > Cassandra > ScyllaDB > HBase = Accumulo
3. **Security Requirements**: Accumulo > HBase > Cassandra > ScyllaDB > DynamoDB
4. **Ecosystem Integration**: HBase > Cassandra > Accumulo > ScyllaDB > DynamoDB
5. **Multi-DC Requirements**: Cassandra = ScyllaDB > DynamoDB > HBase = Accumulo

## Real-World Column-Family Store Use Cases

### Apache Cassandra Real-World Implementations

| Company/Organization | Use Case | Why Cassandra | Scale/Impact |
|---------------------|----------|---------------|--------------|
| **Netflix** | Viewing history, recommendations | Multi-DC, scale, availability | 1B+ hours viewing/day |
| **Instagram** | User feeds, activities, messages | Linear scaling, write throughput | 500M+ daily users |
| **Apple** | iMessage infrastructure | Scale, reliability, multi-DC | 1B+ devices |
| **Spotify** | User playlists, listening history | Time-series, global distribution | 500M+ users |
| **Discord** | Message history, presence | Time-series, fast writes | 150M+ monthly users |
| **Uber** | Driver locations, trip data | Geo-distributed, high write volume | 130M+ monthly users |

**Key Pattern**: Cassandra dominates time-series workloads, globally distributed systems, and write-heavy applications.

### HBase Real-World Implementations

| Company/Organization | Use Case | Why HBase | Scale/Impact |
|---------------------|----------|-----------|--------------|
| **Facebook Messenger** | Message storage, inbox | Consistency, scale, HBase modifications | 1B+ users |
| **Yahoo** | Content storage, serving layer | Hadoop integration, batch processing | Billions of objects |
| **Adobe** | Experience Platform, user profiles | Analytics integration, ML pipelines | 100B+ events/day |
| **Pinterest** | User boards, pin storage | Hadoop ecosystem, analytics | 450M+ users |
| **Salesforce** | Phoenix SQL layer usage | SQL on HBase, analytics | Enterprise scale |
| **Xiaomi** | User data, device telemetry | Scale, consistency, cost | 500M+ users |

**Key Pattern**: HBase chosen when Hadoop ecosystem integration is critical or strong consistency is required.

### DynamoDB Real-World Implementations (Column-Family Specific)

| Company/Organization | Use Case | Why DynamoDB | Scale/Impact |
|---------------------|----------|---------------|--------------|
| **Lyft** | Ride history, driver activity logs | Auto-scaling, time-series with TTL | 2M+ drivers |
| **BMW** | Connected car telemetry | IoT scale, global low latency | 14M+ connected cars |
| **GE Healthcare** | Medical device telemetry | Compliance, auto-scaling | Thousands of devices |
| **Zoom** | Meeting metadata, participant info | Burst scaling, global | 300M+ daily participants |
| **Peloton** | Workout history, user metrics | Time-series, serverless | 6M+ members |
| **Coinbase** | Transaction history, audit logs | Compliance, durability | 100M+ users |

**Key Pattern**: DynamoDB excels for IoT time-series, audit trails, and serverless column-family needs.

### ScyllaDB Real-World Implementations

| Company/Organization | Use Case | Why ScyllaDB | Scale/Impact |
|---------------------|----------|--------------|--------------|
| **Discord** | Migrated from Cassandra | 10x performance improvement | Billions of messages |
| **Comcast** | XFinity platform, user activity | Low latency, high throughput | 30M+ subscribers |
| **Grab** | Driver tracking, ride history | Real-time performance | 200M+ users |
| **Fanatics** | Inventory tracking, user sessions | Black Friday scale | E-commerce spikes |
| **Zillow** | Property views, user activity | Performance, compatibility | 200M+ monthly users |
| **ShareChat** | User feeds, content delivery | India scale, performance | 180M+ users |

**Key Pattern**: ScyllaDB chosen by companies hitting Cassandra performance limits or needing lowest possible latency.

### Apache Accumulo Real-World Implementations

| Company/Organization | Use Case | Why Accumulo | Scale/Impact |
|---------------------|----------|--------------|--------------|
| **NSA** | Intelligence data platform | Created for security needs | Classified scale |
| **US Government Agencies** | Classified analytics | Cell-level security | National security |
| **Healthcare Systems** | Patient data analytics | HIPAA compliance, security | Protected health info |
| **Financial Institutions** | Fraud detection, compliance | Fine-grained access control | Regulatory compliance |
| **Research Institutions** | Genomics data | Secure collaboration | Sensitive research |
| **Defense Contractors** | Sensor data analysis | Security clearance levels | Classified systems |

**Key Pattern**: Accumulo dominates where cell-level security and compliance requirements are paramount.

## Industry-Specific Patterns

### Time-Series & IoT
- **General Purpose**: Cassandra (Netflix, Uber)
- **Serverless/AWS**: DynamoDB (BMW, GE)
- **Maximum Performance**: ScyllaDB (real-time systems)
- **Hadoop Analytics**: HBase (Yahoo, Adobe)

### Messaging & Social
- **Message History**: Cassandra (Discord, Instagram)
- **Consistent Messaging**: HBase (Facebook Messenger)
- **Global Scale**: Cassandra (WhatsApp reportedly)
- **Performance Critical**: ScyllaDB (Discord migration)

### Analytics & ML
- **Feature Stores**: HBase (Adobe, Pinterest)
- **Time-Series Analytics**: Cassandra (Spotify, Netflix)
- **Secure Analytics**: Accumulo (government)
- **Real-time Analytics**: ScyllaDB (AdTech)

### Financial Services
- **Audit Trails**: DynamoDB (Coinbase)
- **Fraud Detection**: Accumulo (banks)
- **Transaction History**: Cassandra (payment processors)
- **Risk Analytics**: HBase (investment banks)

### Gaming
- **Player Activity**: Cassandra (online games)
- **Leaderboards**: ScyllaDB (competitive gaming)
- **Game Analytics**: HBase (mobile gaming)
- **Serverless Games**: DynamoDB (cloud gaming)

## Performance Benchmarks

### Cassandra
- **Netflix**: 1M+ writes/second per cluster
- **Apple**: 160,000+ Cassandra nodes
- **Discord**: Storing trillions of messages

### HBase
- **Facebook**: 600TB+ clusters
- **Yahoo**: 50+ PB stored
- **Xiaomi**: 100+ billion rows

### DynamoDB
- **Peak**: 89.2M requests/second (Prime Day)
- **Lyft**: 40x traffic spikes handled
- **BMW**: Sub-10ms globally

### ScyllaDB
- **Discord**: 10x Cassandra performance
- **Comcast**: 1M+ ops/second/node
- **ShareChat**: 5ms p99 latency

### Accumulo
- **Classified**: Petabyte-scale deployments
- **Performance**: Similar to HBase with security overhead

The choice depends on:
- **Time-Series Focus**: Cassandra or ScyllaDB
- **Hadoop Integration**: HBase
- **Serverless Needs**: DynamoDB
- **Performance Critical**: ScyllaDB
- **Security Critical**: Accumulo


