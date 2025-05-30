# Industry-Specific Database Patterns - Complete Compilation

## Database Selection Guide - Which DB to Choose When and Why

### By Use Case Type

| Use Case | Recommended Database | Why | Industry Examples (Section 1 Reference) |
|----------|---------------------|-----|----------------------------------------|
| **E-commerce Product Catalog** | MongoDB, Elasticsearch | Flexible schema, fast search | [Document Store: E-commerce](#from-document-store-databases), [Search: E-commerce](#from-search-databases) |
| **Shopping Cart/Session** | Redis, DynamoDB | Fast access, TTL support | [Key-Value: E-commerce](#from-key-value-stores), [Document Store: E-commerce](#from-document-store-databases) |
| **Financial Transactions** | Oracle, PostgreSQL, VoltDB | ACID compliance, consistency | [RDBMS: Financial Services](#from-relational-databases-rdbms), [In-Memory: Financial Services](#from-in-memory-databases) |
| **Fraud Detection** | Neo4j + Redis | Graph patterns + real-time cache | [Graph: Financial Services](#from-graph-databases), [Key-Value: Financial Services](#from-key-value-stores) |
| **User Authentication** | Redis, DynamoDB | Low latency, session management | [Key-Value: Social Media](#from-key-value-stores), [Document Store: Gaming](#from-document-store-databases) |
| **Real-time Analytics** | Druid, SAP HANA, Impala | Sub-second queries, OLAP | [Time Series: Digital Advertising](#from-time-series-databases), [In-Memory: E-commerce](#from-in-memory-databases), [HDFS: Financial Services](#from-hdfs-based-databases) |
| **Log Analysis** | Elasticsearch, Splunk | Full-text search, time-based | [Search: Security & Compliance](#from-search-databases), [Time Series: DevOps](#from-time-series-databases) |
| **Time-Series Data** | InfluxDB, Cassandra, HBase | Optimized for time-based data | [Time Series: IoT](#from-time-series-databases), [Column-Family: Time-Series & IoT](#from-column-family-stores), [HDFS: IoT](#from-hdfs-based-databases) |
| **Social Network** | Neo4j, ArangoDB | Graph relationships | [Graph: Media & Entertainment](#from-graph-databases), [Multi-Model: Telecommunications](#from-multi-model-databases) |
| **Content Management** | MongoDB, MarkLogic | Documents, search capabilities | [Document Store: Media](#from-document-store-databases), [Multi-Model: Media & Publishing](#from-multi-model-databases) |
| **IoT Device Data** | InfluxDB, DynamoDB, Cassandra | High ingestion, time-series | [Time Series: IoT](#from-time-series-databases), [Document Store: IoT](#from-document-store-databases), [Column-Family: Time-Series](#from-column-family-stores) |
| **Recommendation Engine** | Neo4j + Redis, ArangoDB | Graph algorithms + caching | [Graph: Retail](#from-graph-databases), [In-Memory: E-commerce](#from-in-memory-databases), [Multi-Model: Retail](#from-multi-model-databases) |
| **Messaging/Chat** | HBase, Cassandra | Write-heavy, time-ordered | [Column-Family: Messaging](#from-column-family-stores), [HDFS: Telecommunications](#from-hdfs-based-databases) |
| **Gaming Leaderboards** | Redis, ScyllaDB | Sorted sets, low latency | [In-Memory: Gaming](#from-in-memory-databases), [Column-Family: Gaming](#from-column-family-stores) |
| **Compliance/Audit** | MarkLogic, Splunk | Immutable logs, search | [Multi-Model: Financial Services](#from-multi-model-databases), [Search: Security & Compliance](#from-search-databases) |

### By Industry Vertical

| Industry | Primary Use Case | Best Database Choice | Fallback Option | Section 1 Reference |
|----------|-----------------|---------------------|-----------------|-------------------|
| **Financial Services** | Trading Systems | VoltDB, Oracle | PostgreSQL | [In-Memory: Financial](#from-in-memory-databases), [RDBMS: Financial](#from-relational-databases-rdbms) |
| **Financial Services** | Risk Analytics | SAP HANA, Neo4j | Apache Ignite | [In-Memory: Financial](#from-in-memory-databases), [Graph: Financial](#from-graph-databases) |
| **Financial Services** | Fraud Detection | Neo4j + Splunk | Elasticsearch | [Graph: Financial](#from-graph-databases), [Search: Financial](#from-search-databases) |
| **E-commerce** | Product Catalog | MongoDB + Elasticsearch | PostgreSQL | [Document Store: E-commerce](#from-document-store-databases), [Search: E-commerce](#from-search-databases) |
| **E-commerce** | Shopping Cart | Redis, DynamoDB | Memcached | [Key-Value: E-commerce](#from-key-value-stores), [In-Memory: E-commerce](#from-in-memory-databases) |
| **E-commerce** | Order History | PostgreSQL, HBase | MySQL | [RDBMS: E-commerce](#from-relational-databases-rdbms), [HDFS: Retail](#from-hdfs-based-databases) |
| **Healthcare** | Patient Records | MarkLogic, PostgreSQL | MongoDB | [Multi-Model: Healthcare](#from-multi-model-databases), [RDBMS: Healthcare](#from-relational-databases-rdbms) |
| **Healthcare** | Medical Analytics | Impala, TimescaleDB | SAP HANA | [HDFS: Healthcare](#from-hdfs-based-databases), [Time Series: Financial](#from-time-series-databases) |
| **Gaming** | Player State | Redis, DynamoDB | MongoDB | [In-Memory: Gaming](#from-in-memory-databases), [Document Store: Gaming](#from-document-store-databases) |
| **Gaming** | Leaderboards | Redis, ScyllaDB | Cassandra | [In-Memory: Gaming](#from-in-memory-databases), [Column-Family: Gaming](#from-column-family-stores) |
| **Gaming** | Analytics | MongoDB, Druid | HBase | [Document Store: Gaming](#from-document-store-databases), [HDFS: IoT](#from-hdfs-based-databases) |
| **Telecommunications** | CDR Storage | HBase, Cassandra | MongoDB | [HDFS: Telecommunications](#from-hdfs-based-databases), [Column-Family: Messaging](#from-column-family-stores) |
| **Telecommunications** | Network Monitoring | InfluxDB, Prometheus | OpenTSDB | [Time Series: Cloud Infrastructure](#from-time-series-databases) |
| **Social Media** | User Feeds | Cassandra, Redis | MongoDB | [Column-Family: Messaging](#from-column-family-stores), [Key-Value: Social Media](#from-key-value-stores) |
| **Social Media** | Social Graph | Neo4j, ArangoDB | OrientDB | [Graph: Media](#from-graph-databases), [Multi-Model: Telecommunications](#from-multi-model-databases) |
| **IoT** | Sensor Data | InfluxDB, Cassandra | HBase | [Time Series: IoT](#from-time-series-databases), [Column-Family: Time-Series](#from-column-family-stores) |
| **IoT** | Device Management | DynamoDB, MongoDB | Cosmos DB | [Document Store: IoT](#from-document-store-databases), [Multi-Model: Telecommunications](#from-multi-model-databases) |
| **Media/Publishing** | Content Search | Elasticsearch, MarkLogic | Solr | [Search: Media](#from-search-databases), [Multi-Model: Media](#from-multi-model-databases) |
| **Media/Publishing** | User Preferences | DynamoDB, Redis | MongoDB | [Document Store: Media](#from-document-store-databases), [Key-Value: Social Media](#from-key-value-stores) |

### By Technical Requirements

| Requirement | Best Database Type | Specific Recommendations | Why | Section 1 Reference |
|------------|-------------------|-------------------------|-----|-------------------|
| **ACID Transactions** | RDBMS, VoltDB | PostgreSQL, Oracle, VoltDB | Full transaction support | [RDBMS: Financial](#from-relational-databases-rdbms), [In-Memory: Financial](#from-in-memory-databases) |
| **Global Distribution** | Multi-Model, Document | Cosmos DB, DynamoDB, FaunaDB | Built-in global replication | [Multi-Model: Retail](#from-multi-model-databases), [Document Store: E-commerce](#from-document-store-databases) |
| **Sub-second Queries** | In-Memory, Search | Redis, Elasticsearch, Algolia | Optimized for speed | [In-Memory: All industries](#from-in-memory-databases), [Search: Technology](#from-search-databases) |
| **Complex Relationships** | Graph | Neo4j, JanusGraph | Native graph processing | [Graph: All industries](#from-graph-databases) |
| **Time-Series Data** | Time-Series, Column | InfluxDB, Cassandra, Druid | Time-based optimization | [Time Series: IoT](#from-time-series-databases), [Column-Family: Time-Series](#from-column-family-stores) |
| **Full-Text Search** | Search | Elasticsearch, Solr, MarkLogic | Inverted indexes | [Search: All industries](#from-search-databases) |
| **Massive Scale (PB+)** | Column-Family, HDFS | Cassandra, HBase, Hive | Distributed architecture | [Column-Family: Messaging](#from-column-family-stores), [HDFS: Financial](#from-hdfs-based-databases) |
| **Real-time Analytics** | In-Memory, Time-Series | SAP HANA, Druid, Impala | Fast aggregations | [In-Memory: Retail](#from-in-memory-databases), [Time Series: Digital Advertising](#from-time-series-databases) |
| **Schema Flexibility** | Document, Key-Value | MongoDB, DynamoDB | JSON/schema-less | [Document Store: All industries](#from-document-store-databases) |
| **SQL Required** | RDBMS, SQL-on-Hadoop | PostgreSQL, Phoenix, Impala | SQL compatibility | [RDBMS: All industries](#from-relational-databases-rdbms), [HDFS: All industries](#from-hdfs-based-databases) |

### By Scale and Performance Needs

| Scale/Performance Need | Database Recommendation | Alternative | Reasoning | Section 1 Reference |
|----------------------|------------------------|-------------|-----------|-------------------|
| **< 1GB, Simple Cache** | Memcached, Redis | - | Simple, fast, proven | [Key-Value: E-commerce](#from-key-value-stores), [In-Memory: Social Media](#from-in-memory-databases) |
| **1GB-100GB, OLTP** | PostgreSQL, MySQL | MariaDB | ACID, mature, cost-effective | [RDBMS: SaaS Platforms](#from-relational-databases-rdbms) |
| **100GB-1TB, Mixed** | MongoDB, PostgreSQL | Cassandra | Flexible, good tooling | [Document Store: Gaming](#from-document-store-databases), [RDBMS: E-commerce](#from-relational-databases-rdbms) |
| **1TB-10TB, Analytics** | Cassandra, ClickHouse | Druid | Distributed, columnar | [Column-Family: Analytics](#from-column-family-stores), [Time Series: Financial](#from-time-series-databases) |
| **10TB-100TB, Batch** | Hive, Spark SQL | Presto | Hadoop ecosystem | [HDFS: Retail & E-commerce](#from-hdfs-based-databases) |
| **100TB+, Mixed** | Cassandra, HBase | - | Proven at scale | [Column-Family: Time-Series](#from-column-family-stores), [HDFS: Financial](#from-hdfs-based-databases) |
| **Real-time + Scale** | ScyllaDB, Druid | Kudu | Low latency at scale | [Column-Family: Gaming](#from-column-family-stores), [HDFS: Retail](#from-hdfs-based-databases) |
| **Global + Consistent** | FaunaDB, Cosmos DB | Spanner | Global ACID | [Multi-Model: Financial](#from-multi-model-databases), [Multi-Model: Retail](#from-multi-model-databases) |

### By Consistency and Availability Trade-offs

| CAP Priority | Use Case | Database Choice | Why | Section 1 Reference |
|-------------|----------|-----------------|-----|-------------------|
| **CP (Consistency)** | Financial Transactions | PostgreSQL, VoltDB | ACID critical | [RDBMS: Financial](#from-relational-databases-rdbms), [In-Memory: Financial](#from-in-memory-databases) |
| **CP (Consistency)** | Inventory Management | FaunaDB, Oracle | Accurate counts | [Multi-Model: Retail](#from-multi-model-databases), [RDBMS: E-commerce](#from-relational-databases-rdbms) |
| **AP (Availability)** | Social Media Feeds | Cassandra, DynamoDB | Always available | [Column-Family: Messaging](#from-column-family-stores), [Document Store: Media](#from-document-store-databases) |
| **AP (Availability)** | Content Delivery | CouchDB, Cassandra | Offline-capable | [Document Store: Media](#from-document-store-databases), [Column-Family: Messaging](#from-column-family-stores) |
| **CA (Single Region)** | Local Systems | PostgreSQL, MongoDB | Simple consistency | [RDBMS: Healthcare](#from-relational-databases-rdbms), [Document Store: Gaming](#from-document-store-databases) |
| **Tunable** | Mixed Workloads | Cassandra, Cosmos DB | Flexible consistency | [Column-Family: All](#from-column-family-stores), [Multi-Model: All](#from-multi-model-databases) |

### Special Considerations

| Special Need | Database Choice | Why | Use Case Examples | Section 1 Reference |
|-------------|-----------------|-----|-------------------|-------------------|
| **Offline-First** | CouchDB, SQLite | Sync capabilities | Mobile apps, field work | [Document Store: Healthcare](#from-document-store-databases) |
| **Serverless** | DynamoDB, FaunaDB | No ops, auto-scale | Modern web apps | [Document Store: Gaming](#from-document-store-databases), [Multi-Model: Financial](#from-multi-model-databases) |
| **Compliance/Audit** | MarkLogic, Splunk | Security features | Healthcare, Finance | [Multi-Model: Healthcare](#from-multi-model-databases), [Search: Security](#from-search-databases) |
| **Multi-Model** | ArangoDB, Cosmos DB | Flexibility | Complex apps | [Multi-Model: All industries](#from-multi-model-databases) |
| **Open Source Only** | PostgreSQL, Cassandra | No vendor lock | Startups, Government | [RDBMS: Government](#from-relational-databases-rdbms), [Column-Family: All](#from-column-family-stores) |
| **Windows/Microsoft** | SQL Server, Cosmos DB | Ecosystem integration | Enterprise | [RDBMS: Healthcare](#from-relational-databases-rdbms), [Multi-Model: Retail](#from-multi-model-databases) |
| **Real-time ML** | Redis, Kudu | Fast feature serving | ML applications | [In-Memory: All](#from-in-memory-databases), [HDFS: Retail](#from-hdfs-based-databases) |

## Industry-Specific Patterns from All Database Types

### From Relational Databases (RDBMS)

#### Financial Services
- **High-Value Transactions**: Oracle (JPMorgan, Bank of America)
- **Web/Mobile Banking**: MySQL/MariaDB (Revolut, N26)
- **Risk Analytics**: PostgreSQL (some hedge funds)
- **Windows-based**: SQL Server (regional banks)

#### E-commerce
- **Large Scale**: MySQL with sharding (Amazon formerly, Shopify)
- **Enterprise**: Oracle (Walmart, Home Depot)
- **Modern Stack**: PostgreSQL (Zalando)

#### Healthcare
- **Hospital Systems**: Oracle or SQL Server (Epic, Cerner deployments)
- **Health Tech Startups**: PostgreSQL (Oscar Health, Zocdoc)
- **Medical Devices**: MariaDB (distributed systems)

#### Government
- **Federal**: Oracle (defense, intelligence)
- **Modern Services**: PostgreSQL (UK Gov.uk, USAspending.gov)
- **State/Local**: SQL Server (Windows infrastructure)

#### SaaS Platforms
- **Multi-tenant**: Oracle (Salesforce) or PostgreSQL (Heroku)
- **Analytics**: PostgreSQL (Datadog uses it heavily)
- **Simple/Fast**: MySQL (Zendesk, Freshworks)

### From Document Store Databases

#### Gaming Industry
- **Real-time State**: DynamoDB (Fortnite, Pokemon Go)
- **Player Profiles**: MongoDB (EA Games, Riot Games)
- **Global Leaderboards**: Cosmos DB (Xbox Live)
- **Game Analytics**: MongoDB (mobile gaming companies)

#### E-commerce
- **Product Catalogs**: MongoDB (eBay, Alibaba subsidiaries)
- **Shopping Carts**: DynamoDB (Amazon, Zalando)
- **Global Inventory**: Cosmos DB (ASOS, Marks & Spencer)
- **Order Management**: RavenDB (enterprise retail)

#### Media & Entertainment
- **Content Management**: MongoDB (Forbes, Hearst)
- **User Preferences**: DynamoDB (Netflix, Disney+)
- **Content Distribution**: CouchDB (BBC)
- **Global Streaming**: Cosmos DB (Microsoft Stream)

#### IoT & Telemetry
- **Device Data**: DynamoDB (Philips Hue, Ring)
- **Time-series**: MongoDB (Bosch, Siemens)
- **Global IoT**: Cosmos DB (Johnson Controls)
- **Offline Sensors**: CouchDB (agricultural IoT)

#### Healthcare
- **Patient Records**: RavenDB (hospitals using Epic/Cerner)
- **Medical Devices**: MongoDB (Philips medical)
- **Claims Processing**: RavenDB (insurance companies)
- **Field Medicine**: CouchDB (MSF, Red Cross)

#### Financial Services
- **Trading Data**: MongoDB (hedge funds, crypto exchanges)
- **Transaction Records**: DynamoDB (fintech startups)
- **Global Banking**: Cosmos DB (international banks)
- **Compliance**: RavenDB (regulatory reporting)

### From Key-Value Stores

#### Gaming Industry
- **Session State**: Redis (Epic Games, Riot)
- **Player Inventory**: DynamoDB (Zynga, Supercell)
- **Match History**: Cassandra (Discord, gaming platforms)
- **Game Servers**: etcd (service discovery)

#### Financial Services  
- **Trading Cache**: Redis (high-frequency trading)
- **Session Tokens**: DynamoDB (Capital One, fintech)
- **Transaction History**: Cassandra (payment processors)
- **API Rate Limiting**: Redis (all major banks)

#### Social Media
- **Feed Caching**: Redis (Twitter, Pinterest)
- **User Sessions**: DynamoDB (social apps)
- **Activity Streams**: Cassandra (Instagram, Discord)
- **Simple Caching**: Memcached (Facebook, Reddit)

#### E-commerce
- **Cart Storage**: Redis (Shopify stores)
- **Session Management**: DynamoDB (Amazon, Airbnb)
- **Product Views**: Cassandra (recommendation engines)
- **Page Caching**: Memcached (traditional stores)

#### Infrastructure/DevOps
- **Service Discovery**: etcd (Kubernetes everywhere)
- **Circuit Breakers**: Redis (Netflix Hystrix)
- **Metrics Storage**: Cassandra (DataDog uses it)
- **Build Cache**: Memcached (CI/CD systems)

### From Column-Family Stores

#### Time-Series & IoT
- **General Purpose**: Cassandra (Netflix, Uber)
- **Serverless/AWS**: DynamoDB (BMW, GE)
- **Maximum Performance**: ScyllaDB (real-time systems)
- **Hadoop Analytics**: HBase (Yahoo, Adobe)

#### Messaging & Social
- **Message History**: Cassandra (Discord, Instagram)
- **Consistent Messaging**: HBase (Facebook Messenger)
- **Global Scale**: Cassandra (WhatsApp reportedly)
- **Performance Critical**: ScyllaDB (Discord migration)

#### Analytics & ML
- **Feature Stores**: HBase (Adobe, Pinterest)
- **Time-Series Analytics**: Cassandra (Spotify, Netflix)
- **Secure Analytics**: Accumulo (government)
- **Real-time Analytics**: ScyllaDB (AdTech)

#### Financial Services
- **Audit Trails**: DynamoDB (Coinbase)
- **Fraud Detection**: Accumulo (banks)
- **Transaction History**: Cassandra (payment processors)
- **Risk Analytics**: HBase (investment banks)

#### Gaming
- **Player Activity**: Cassandra (online games)
- **Leaderboards**: ScyllaDB (competitive gaming)
- **Game Analytics**: HBase (mobile gaming)
- **Serverless Games**: DynamoDB (cloud gaming)

### From Graph Databases

#### Financial Services
- **Fraud Detection**: Neo4j (PayPal, banks)
- **Risk Analysis**: Neo4j (UBS, investment firms)
- **Compliance**: Neptune (regulatory reporting)
- **Trade Analysis**: JanusGraph (FINRA)

#### Retail & E-commerce
- **Recommendations**: Neo4j (eBay, retail)
- **Supply Chain**: Neo4j (Walmart)
- **Customer 360**: Neptune (identity graphs)
- **Logistics**: ArangoDB (routing)

#### Technology & Telecom
- **Network Management**: OrientDB (Telenor)
- **Service Dependencies**: ArangoDB (Cisco)
- **Knowledge Management**: Neptune (Siemens)
- **Infrastructure**: JanusGraph (large scale)

#### Life Sciences & Healthcare
- **Drug Discovery**: Neptune (AstraZeneca)
- **Clinical Trials**: Neptune (pharmaceuticals)
- **Research Networks**: Neo4j (genomics)
- **Medical Knowledge**: Neptune (RDF models)

#### Media & Entertainment
- **Content Recommendations**: Neo4j/Neptune (Netflix uses both)
- **Social Features**: Neo4j (social networks)
- **Content Knowledge**: Neptune (Pearson)
- **User Journeys**: ArangoDB (education)

### From Time Series Databases

#### Cloud Infrastructure
- **Container Monitoring**: Prometheus (industry standard)
- **VM/Server Metrics**: InfluxDB, Prometheus
- **Multi-cloud**: TimescaleDB (portable)
- **Massive Scale**: OpenTSDB

#### IoT & Manufacturing
- **Sensor Data**: InfluxDB (purpose-built)
- **Industrial IoT**: TimescaleDB (SQL analytics)
- **Real-time Dashboards**: Druid
- **Long-term Storage**: OpenTSDB

#### Financial Services
- **Market Data**: TimescaleDB (SQL, ACID)
- **Trading Metrics**: InfluxDB (low latency)
- **Risk Analytics**: Druid (real-time)
- **Compliance Storage**: TimescaleDB

#### Digital Advertising
- **Ad Performance**: Druid (Yahoo, others)
- **Campaign Analytics**: Druid
- **Publisher Metrics**: InfluxDB
- **Long-term Analysis**: TimescaleDB

#### DevOps/SRE
- **Kubernetes**: Prometheus (native)
- **Application Metrics**: Prometheus, InfluxDB
- **SLO/SLI Tracking**: Prometheus
- **Custom Metrics**: InfluxDB

### From In-Memory Databases

#### Financial Services
- **Trading Systems**: VoltDB (ACID required)
- **Risk Calculations**: Apache Ignite (distributed compute)
- **Market Data Cache**: Redis (low latency)
- **Core Banking**: SAP HANA (with SAP)

#### E-commerce & Retail
- **Session Storage**: Redis (data structures)
- **Product Cache**: Memcached (simple)
- **Inventory Systems**: SAP HANA (real-time)
- **Recommendation Cache**: Redis (sorted sets)

#### Gaming
- **Leaderboards**: Redis (sorted sets)
- **Session State**: Redis/Memcached
- **Virtual Economies**: VoltDB (ACID)
- **Matchmaking**: Redis (geospatial)

#### Telecommunications
- **Billing Systems**: VoltDB (consistency)
- **Network State**: Apache Ignite
- **Subscriber Cache**: Memcached
- **Real-time Analytics**: SAP HANA

#### Social Media
- **Timeline Cache**: Redis (sorted sets)
- **User Sessions**: Redis/Memcached
- **Social Graph**: Redis (sets)
- **Content Cache**: Memcached

### From Multi-Model Databases

#### Financial Services
- **Compliance Platforms**: MarkLogic (audit trails)
- **Global Trading**: FaunaDB (consistency)
- **Risk Analysis**: ArangoDB (graph + docs)
- **Customer 360**: Cosmos DB (scale)

#### Healthcare
- **Patient Records**: MarkLogic (HL7, FHIR)
- **Research Platforms**: ArangoDB (flexible)
- **Medical Devices**: Cosmos DB (IoT scale)
- **Clinical Trials**: MarkLogic (compliance)

#### Retail & E-commerce
- **Global Catalogs**: Cosmos DB (ASOS)
- **Recommendation Engines**: ArangoDB
- **Inventory Systems**: FaunaDB (consistency)
- **Content Management**: OrientDB

#### Telecommunications
- **Network Management**: OrientDB/ArangoDB
- **Service Catalogs**: ArangoDB
- **Billing Systems**: MarkLogic
- **IoT Platforms**: Cosmos DB

#### Media & Publishing
- **Content Platforms**: MarkLogic (search)
- **Recommendation Systems**: ArangoDB
- **Rights Management**: MarkLogic
- **User Profiles**: Cosmos DB

### From Search Databases

#### E-commerce
- **Large Catalogs**: Elasticsearch (eBay)
- **Instant Product Search**: Algolia (Lacoste)
- **Traditional Retail**: Solr (Best Buy)
- **AWS-based**: CloudSearch

#### Security & Compliance
- **SIEM**: Splunk (ING, Domino's)
- **Log Analytics**: Elasticsearch (Netflix)
- **Compliance Reporting**: Splunk
- **Threat Hunting**: Splunk/Elasticsearch

#### Media & Publishing
- **Content Discovery**: Algolia (Medium)
- **Digital Libraries**: Solr (HathiTrust)
- **Video Search**: CloudSearch (PBS)
- **News Archives**: Elasticsearch

#### Technology/SaaS
- **Documentation**: Algolia (Stripe, Vue.js)
- **Code Search**: Elasticsearch (GitHub)
- **Support Portals**: Solr (AT&T)
- **Analytics**: Elasticsearch

#### Financial Services
- **Trading Monitoring**: Splunk (Nasdaq)
- **Fraud Detection**: Splunk (Domino's)
- **Customer Portal**: Solr/Elasticsearch
- **Compliance**: Splunk

### From HDFS-Based Databases

#### Financial Services
- **Risk Analytics**: Impala (interactive dashboards)
- **Transaction History**: HBase (random access)
- **Regulatory Reporting**: Hive (batch processing)
- **Real-time Scoring**: Phoenix (OLTP)

#### Telecommunications
- **CDR Storage**: HBase (call detail records)
- **Network Analytics**: Hive (batch analysis)
- **Real-time Monitoring**: Kudu (updates)
- **Customer 360**: Phoenix (SQL access)

#### Retail & E-commerce
- **Inventory**: Kudu (real-time updates)
- **Order History**: HBase (random access)
- **Analytics**: Hive (batch) + Impala (interactive)
- **Recommendations**: Phoenix (fast lookups)

#### Healthcare
- **Patient Records**: HBase (large records)
- **Analytics**: Impala (interactive)
- **Compliance Reports**: Hive (batch)
- **Real-time Monitoring**: Phoenix

#### IoT & Manufacturing
- **Sensor Data**: HBase (time-series)
- **Analytics**: Kudu (mutable)
- **Batch Processing**: Hive
- **Dashboards**: Impala
