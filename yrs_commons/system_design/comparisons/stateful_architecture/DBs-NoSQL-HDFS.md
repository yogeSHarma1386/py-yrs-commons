# HDFS-Based Database Comparison

## Table 1: Core Characteristics

| Database | Data Structures Used | Real-World Application | Why It's Used |
|----------|---------------------|------------------------|---------------|
| Apache HBase | LSM tree, HDFS storage, MemStore + HFiles | Real-time big data, messaging apps, time-series | Random read/write on Hadoop, strong consistency |
| Apache Hive | HDFS files (ORC, Parquet), metastore | Data warehousing, ETL, batch analytics | SQL on Hadoop, batch processing, schema-on-read |
| Apache Phoenix | HBase tables, secondary indexes | OLTP on Hadoop, operational analytics | SQL interface to HBase, ACID transactions |
| Apache Kudu | Columnar storage, B-tree + LSM hybrid | Fast analytics, machine learning features | Mutable data on Hadoop, balanced read/write |
| Apache Impala | HDFS/Kudu/HBase, in-memory processing | Interactive BI, ad-hoc queries | MPP SQL engine, low latency queries |

## Use Cases Description

### Apache HBase
- **Messaging Applications**: Facebook Messenger, WhatsApp-scale systems
- **Time-Series Data**: IoT sensor data, metrics storage
- **User Profiles**: Large-scale user data storage
- **Content Management**: Large content repositories

### Apache Hive
- **Data Warehousing**: Enterprise DW on Hadoop
- **ETL Processing**: Large-scale data transformation
- **Log Analysis**: Batch processing of log files
- **Business Intelligence**: Historical analytics

### Apache Phoenix
- **Operational Analytics**: Real-time dashboards on HBase
- **OLTP Workloads**: Transaction processing on Hadoop
- **Secondary Indexing**: Fast lookups on HBase data
- **Migration from RDBMS**: SQL compatibility layer

### Apache Kudu
- **Machine Learning**: Feature stores for ML pipelines
- **Time-Series Analytics**: Mutable time-series data
- **Data Lake Updates**: Changeable data in data lakes
- **Real-Time Analytics**: Fast scans with updates

### Apache Impala
- **Interactive BI**: Tableau/PowerBI on Hadoop
- **Ad-hoc Analysis**: Data scientist exploration
- **Multi-Table Joins**: Complex SQL queries
- **Report Generation**: Low-latency reporting

## Table 2: CA Systems (Consistency + Availability)

| Database | CAP Classification | Characteristics |
|----------|-------------------|-----------------|
| HBase | CP (strong consistency) | Single master per region, consistent reads |
| Hive | Not real-time (batch) | HDFS consistency, not a real-time system |
| Phoenix | CP (via HBase) | Inherits HBase consistency model |
| Kudu | CP (Raft consensus) | Strong consistency via Raft, leader-based |
| Impala | Read-only consistency | Query consistency, catalog synchronization |

## Table 3: CP Systems (Consistency + Partition Tolerance)

| Database | Configuration | Trade-offs |
|----------|--------------|------------|
| HBase | Default operation | Region unavailable during splits |
| Hive | N/A (batch system) | Not applicable for batch |
| Phoenix | Default (HBase-based) | Same as HBase limitations |
| Kudu | Default (Raft-based) | May reject writes during leader election |
| Impala | Metadata consistency | Catalog updates may delay |

## Table 4: PA Systems (Partition Tolerance + Availability)

| Database | Configuration | Trade-offs |
|----------|--------------|------------|
| HBase | Timeline consistency | Read from replicas with lag |
| Hive | N/A | Batch processing system |
| Phoenix | Not supported | Built on CP system |
| Kudu | Read replicas | Eventual consistency for reads |
| Impala | Stale metadata | May query outdated metadata |

## Volume Considerations

| Aspect | HBase | Hive | Phoenix | Kudu | Impala |
|--------|-------|------|---------|------|--------|
| **Sweet Spot** | 1TB - 1PB | 10TB - 10PB | 100GB - 10TB | 100GB - 10TB | Query any size |
| **Row Size Limits** | 10MB recommended | No limit (files) | HBase limits | 64KB | Depends on storage |
| **Table Size** | Petabytes | Petabytes | Petabytes | Terabytes | Petabytes |
| **Compression** | Snappy, LZO, GZ | ORC/Parquet native | HBase compression | Built-in | Storage format |
| **Key Difference** | Random access scale | Massive batch scale | SQL on HBase | Balanced workloads | Query engine only |

## Latency Requirements

| Aspect | HBase | Hive | Phoenix | Kudu | Impala |
|--------|-------|------|---------|------|--------|
| **Read Latency** | 1-100ms | Minutes-hours | 10-1000ms | 1-10ms | 100ms-10s |
| **Write Latency** | 1-50ms | Batch only | 10-100ms | 1-10ms | Read-only |
| **Scan Performance** | Good with filters | Optimized for full scan | Depends on index | Excellent | Very fast |
| **Query Complexity** | Simple K/V | Complex SQL | Full SQL | Simple predicates | Complex SQL |
| **Key Difference** | Low latency R/W | Batch analytics | SQL on HBase | Fastest scans | Interactive queries |

## Read/Write Workload Patterns

| Aspect | HBase | Hive | Phoenix | Kudu | Impala |
|--------|-------|------|---------|------|--------|
| **Write Pattern** | Real-time writes | Batch inserts | Through HBase | Real-time updates | Query only |
| **Read Pattern** | Point queries, scans | Full table scans | SQL queries | Fast scans | Analytical queries |
| **Update Support** | Native | INSERT OVERWRITE | Via HBase | Native updates | Read-only |
| **Consistency** | Strong | Eventual (batch) | Strong (HBase) | Strong | Read consistency |
| **Key Difference** | Real-time R/W | Batch oriented | OLTP on HBase | Mutable analytics | Pure query engine |

## Data Structure Requirements

| Aspect | HBase | Hive | Phoenix | Kudu | Impala |
|--------|-------|------|---------|------|--------|
| **Schema Model** | Column families | Tables with schemas | Relational schema | Relational tables | Query various formats |
| **Data Types** | Bytes (app interprets) | Rich SQL types | SQL types | SQL types | SQL types |
| **Secondary Indexes** | No (use Phoenix) | Limited | Yes, multiple types | Primary key only | Depends on storage |
| **Partitioning** | Row key based | Directory based | HBase regions | Hash/range | Storage dependent |
| **Key Difference** | Schema-less | Schema-on-read | Full SQL schema | Strongly typed | Schema agnostic |

## Consistency & Availability Requirements

| Aspect | HBase | Hive | Phoenix | Kudu | Impala |
|--------|-------|------|---------|------|--------|
| **ACID Support** | Row-level | Limited (Hive 3+) | Yes | Row-level | Read-only |
| **Replication** | HDFS replication | HDFS replication | Via HBase | Raft replication | N/A |
| **Failover** | Automatic master | N/A (batch) | Via HBase | Automatic (Raft) | Coordinator HA |
| **Backup** | Snapshots, Export | HDFS backups | HBase snapshots | Snapshots | N/A |
| **Key Difference** | Strong consistency | Batch consistency | ACID on HBase | Raft consensus | Query HA only |

## Replication & Distribution Techniques

| Aspect | HBase | Hive | Phoenix | Kudu | Impala |
|--------|-------|------|---------|------|--------|
| **Data Distribution** | Region splits | Partitions | HBase regions | Tablets | N/A |
| **Replication Type** | Master-slave | HDFS 3x | Via HBase | Raft consensus | N/A |
| **Load Balancing** | Region balancing | Partition pruning | HBase balancing | Tablet balancing | Query planning |
| **Cross-DC** | Asynchronous | Distcp | HBase replication | Not native | Multi-cluster |
| **Key Difference** | Region-based | File-based | Leverages HBase | Tablet-based | Query distribution |

## Conflict Resolution Strategies

| Aspect | HBase | Hive | Phoenix | Kudu | Impala |
|--------|-------|------|---------|------|--------|
| **Write Conflicts** | Last-write-wins | Overwrite | Via HBase | Version-based | N/A |
| **Concurrent Access** | Row locks | File locks | Optimistic concurrency | MVCC | Read-only |
| **Conflict Detection** | Version numbers | None | Version check | Timestamps | N/A |
| **Resolution** | Application level | Replace | Transaction rollback | Automatic | N/A |
| **Key Difference** | Row-level locks | File replacement | ACID transactions | MVCC | No conflicts |

## Scaling Approaches

| Aspect | HBase | Hive | Phoenix | Kudu | Impala |
|--------|-------|------|---------|------|--------|
| **Vertical Scaling** | Limited benefit | More mappers | Via HBase | Effective | Memory helps |
| **Horizontal Scaling** | Add RegionServers | Add nodes | Add HBase nodes | Add tablet servers | Add executors |
| **Auto-splitting** | Yes | No | Via HBase | Yes | N/A |
| **Rebalancing** | Automatic | Manual | HBase handles | Automatic | Query planning |
| **Key Difference** | Automatic scaling | Manual partitioning | Follows HBase | Well-balanced | Query parallelism |

## Operational Considerations

| Aspect | HBase | Hive | Phoenix | Kudu | Impala |
|--------|-------|------|---------|------|--------|
| **Setup Complexity** | High | Medium | Medium | Medium | Medium |
| **Hadoop Integration** | Native | Native | Via HBase | Good | Excellent |
| **Management Tools** | HBase shell, UI | Beeline, Hue | sqlline | CLI tools | Impala shell |
| **Resource Usage** | Memory + HDFS | HDFS heavy | HBase resources | Memory + disk | Memory intensive |
| **Key Difference** | Complex operations | Simpler batch ops | SQL simplifies | Balanced ops | Query tuning focus |

## Decision Matrix for Common Use Cases

| Use Case | Best Choice | Why | Avoid | Why Not |
|----------|-------------|-----|-------|---------|
| **Real-time Analytics** | Kudu/Phoenix | Fast updates + queries | Hive | Too slow |
| **Message Storage** | HBase | Proven at scale | Impala | Not a storage system |
| **Data Warehousing** | Hive | Built for it | HBase | Wrong access pattern |
| **Interactive BI** | Impala | Low latency SQL | Hive | Too slow |
| **Time-Series Data** | HBase/Kudu | Designed for it | Hive | Batch only |
| **ETL Processing** | Hive | Batch optimization | Impala | Not for ETL |
| **OLTP on Hadoop** | Phoenix | ACID support | Hive | Not OLTP |
| **ML Feature Store** | Kudu | Mutable + fast reads | Hive | Too slow for serving |
| **Log Analysis** | Hive | Batch processing | Phoenix | Overkill |
| **Ad-hoc Queries** | Impala | Interactive speed | Hive | Too slow |

## Key Differentiators Summary

### Apache HBase
- **Strengths**: Random access at scale, strong consistency, proven reliability, real-time
- **Weaknesses**: Complex operations, no SQL, no secondary indexes, Java API
- **Choose when**: Need random access on Hadoop, building messaging apps, time-series

### Apache Hive
- **Strengths**: SQL on Hadoop, massive scale batch, cost-effective, mature ecosystem
- **Weaknesses**: High latency, batch-only, not for real-time, limited updates
- **Choose when**: Data warehousing, ETL, batch analytics, log processing

### Apache Phoenix
- **Strengths**: SQL on HBase, secondary indexes, ACID transactions, JDBC driver
- **Weaknesses**: Adds complexity to HBase, performance overhead, limited to HBase
- **Choose when**: Need SQL interface to HBase, migrating from RDBMS, OLTP on Hadoop

### Apache Kudu
- **Strengths**: Fast analytics on mutable data, balanced read/write, columnar storage
- **Weaknesses**: Not as mature, limited ecosystem, memory intensive
- **Choose when**: ML feature stores, mutable analytics, time-series with updates

### Apache Impala
- **Strengths**: MPP SQL engine, low latency, BI tool integration, interactive queries
- **Weaknesses**: Memory intensive, read-only, requires careful tuning
- **Choose when**: Interactive BI, ad-hoc analysis, need sub-second queries

## Architecture Decision Points

**Choose based on:**
1. **Query Latency**: Impala > Kudu > Phoenix > HBase > Hive
2. **Write Performance**: HBase > Kudu > Phoenix > Hive > Impala (read-only)
3. **SQL Completeness**: Impala = Hive > Phoenix > Kudu > HBase (no SQL)
4. **Operational Simplicity**: Hive > Impala > Kudu > Phoenix > HBase
5. **Update Capability**: Kudu > HBase > Phoenix > Hive > Impala

## Real-World HDFS-Based Database Use Cases

### Apache HBase Real-World Implementations

| Company/Organization | Use Case | Why HBase | Scale/Impact |
|---------------------|----------|-----------|--------------|
| **Facebook Messenger** | Message storage | Consistency, scale, real-time | 1B+ users, trillions of messages |
| **Yahoo** | User profiles, content serving | Random access, proven scale | Billions of records |
| **Adobe** | Experience Cloud data | HBase + Phoenix, analytics | 8 trillion transactions/year |
| **Pinterest** | User data, follower graphs | Real-time access, scale | 450M+ users |
| **Salesforce** | Multi-tenant data storage | Isolation, scale | 150K+ customers |
| **Xiaomi** | User behavior, device data | Real-time big data | 500M+ users |

**Key Pattern**: HBase dominates real-time big data applications requiring random access.

### Apache Hive Real-World Implementations

| Company/Organization | Use Case | Why Hive | Scale/Impact |
|---------------------|----------|----------|--------------|
| **Facebook** | Data warehouse (created Hive) | SQL on Hadoop, scale | 300PB+ data warehouse |
| **Netflix** | ETL and data processing | Batch analytics, cost | 500B+ events/day |
| **Airbnb** | Data warehouse, analytics | SQL simplicity, scale | Analytics on all data |
| **Uber** | Historical analytics | Large-scale batch | Petabytes of trip data |
| **Twitter** | Analytics and reporting | Batch processing | Billions of tweets |
| **LinkedIn** | Offline analytics | ETL pipelines | 800M+ members |

**Key Pattern**: Hive remains the standard for SQL-based batch processing on Hadoop.

### Apache Phoenix Real-World Implementations

| Company/Organization | Use Case | Why Phoenix | Scale/Impact |
|---------------------|----------|-------------|--------------|
| **Salesforce** | Multi-tenant OLTP | SQL on HBase, indexes | Enterprise scale |
| **Bloomberg** | Financial data platform | Fast lookups, SQL | Market data |
| **eBay** | Search infrastructure | Secondary indexes | Billions of items |
| **TransUnion** | Credit data queries | ACID, SQL interface | Credit reports |
| **Argus Information** | Risk analytics | Real-time queries | Financial services |
| **TubeMogul** (Adobe) | Ad platform analytics | OLTP + analytics | Billions of ad events |

**Key Pattern**: Phoenix chosen when SQL and secondary indexes on HBase are required.

### Apache Kudu Real-World Implementations

| Company/Organization | Use Case | Why Kudu | Scale/Impact |
|---------------------|----------|----------|--------------|
| **Xiaomi** | Real-time analytics | Fast scans + updates | IoT device analytics |
| **Cloudera customers** | ML feature stores | Mutable data, fast reads | ML pipelines |
| **Financial firms** | Risk calculations | Fast updates, analytics | Trading analytics |
| **Retail analytics** | Inventory tracking | Real-time updates | Store operations |
| **IoT platforms** | Sensor data analytics | Time-series + updates | Industrial IoT |
| **Gaming companies** | Player analytics | Real-time + historical | Game analytics |

**Key Pattern**: Kudu fills the gap for fast analytics on frequently updated data.

### Apache Impala Real-World Implementations

| Company/Organization | Use Case | Why Impala | Scale/Impact |
|---------------------|----------|------------|--------------|
| **Quest Diagnostics** | Healthcare analytics | Interactive BI | Patient data analysis |
| **New York Stock Exchange** | Market surveillance | Low latency queries | Trading analysis |
| **Allstate** | Insurance analytics | BI tool integration | Claims analysis |
| **Cox Automotive** | Dealer analytics | Real-time dashboards | Vehicle data |
| **Major banks** | Risk analytics dashboards | Interactive queries | Financial analysis |
| **Government agencies** | Intelligence analysis | Fast ad-hoc queries | Security analytics |

**Key Pattern**: Impala dominates interactive BI and ad-hoc analysis on Hadoop.

## Industry-Specific Patterns

### Financial Services
- **Risk Analytics**: Impala (interactive dashboards)
- **Transaction History**: HBase (random access)
- **Regulatory Reporting**: Hive (batch processing)
- **Real-time Scoring**: Phoenix (OLTP)

### Telecommunications
- **CDR Storage**: HBase (call detail records)
- **Network Analytics**: Hive (batch analysis)
- **Real-time Monitoring**: Kudu (updates)
- **Customer 360**: Phoenix (SQL access)

### Retail & E-commerce
- **Inventory**: Kudu (real-time updates)
- **Order History**: HBase (random access)
- **Analytics**: Hive (batch) + Impala (interactive)
- **Recommendations**: Phoenix (fast lookups)

### Healthcare
- **Patient Records**: HBase (large records)
- **Analytics**: Impala (interactive)
- **Compliance Reports**: Hive (batch)
- **Real-time Monitoring**: Phoenix

### IoT & Manufacturing
- **Sensor Data**: HBase (time-series)
- **Analytics**: Kudu (mutable)
- **Batch Processing**: Hive
- **Dashboards**: Impala

## Performance Characteristics

### HBase
- **Facebook**: Trillions of messages
- **Throughput**: 1M+ ops/second possible
- **Latency**: 1-10ms typical reads

### Hive
- **Facebook**: 300PB+ warehouse
- **Batch**: Hours for PB scans
- **Optimization**: ORC/Parquet crucial

### Phoenix
- **Salesforce**: Multi-billion row tables
- **Indexes**: 10-100x faster lookups
- **SQL**: Near real-time OLTP

### Kudu
- **Scans**: 10x faster than HBase
- **Updates**: Millions/second
- **Analytics**: Columnar performance

### Impala
- **Latency**: Sub-second to minutes
- **Concurrency**: 100s of queries
- **Memory**: 128GB+ nodes common

The choice depends on:
- **Random Access**: HBase or Phoenix
- **Batch Analytics**: Hive
- **Interactive BI**: Impala
- **Mutable Analytics**: Kudu
- **SQL on HBase**: Phoenix

