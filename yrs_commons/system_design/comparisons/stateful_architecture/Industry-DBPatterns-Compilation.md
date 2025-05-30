# Industry-Specific Database Patterns - Complete Compilation

## Section 1: Industry-Specific Patterns from All Database Types

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