## 📊 Enhanced Feature Comparison Table

| Feature / Tool          | **Kafka**                                       | **RabbitMQ**                                                    | **ActiveMQ**                                 | **Amazon SQS**                                            | **Apache Pulsar**                                          |
|-------------------------|-------------------------------------------------|-----------------------------------------------------------------|----------------------------------------------|-----------------------------------------------------------|------------------------------------------------------------|
| **Type**                | Distributed log/event streaming platform        | Message broker (AMQP)                                           | Message broker (JMS/AMQP)                    | Fully-managed message queue                               | Distributed pub-sub messaging platform                     |
| **Push/Pull Model**     | **Pull-based** (consumer polls)                 | **Push-based** (to consumers)                                   | **Push-based**                               | **Pull-based** (long/short polling)                       | **Both** (push and pull supported)                         |
| **Message Model**       | Pub/Sub (log-based)                             | Queues and topics (Pub/Sub + point-to-point)                    | Queues and topics (Pub/Sub + point-to-point) | Queues (point-to-point)                                   | Unified model (streaming + queuing)                        |
| **Persistence**         | Durable by default (log retention)              | Optional (via persistence plugins)                              | Persistent (JMS store-based)                 | Persistent (cloud-managed)                                | Durable by default (BookKeeper)                            |
| **Granularity**         | Full control: offset, partition, replay         | Moderate: acknowledgments, routing                              | Moderate: durable subscriptions, ACKs        | Limited: poll-based, FIFO optional                        | Full control: cursor, subscription modes, replay           |
| **Delivery Semantics**  | At least once / Exactly once (configurable)     | At most / At least once                                         | At most / At least once                      | At least once (default), Exactly once (FIFO)              | At least once / Exactly once (via transactions)            |
| **Ordering**            | Strong per partition                            | Per queue or topic                                              | Per queue/topic                              | Strict FIFO with FIFO queues                              | Strong per partition/topic                                 |
| **Throughput**          | ⚡ Very high (millions/sec)                      | High                                                            | Medium                                       | Medium (scalable with batching)                           | ⚡ Very high (millions/sec)                                 |
| **Latency**             | 🟢 Low (1–10ms)                                 | 🟢 Low (~1–5ms)                                                 | 🟡 Medium (10–50ms)                          | 🔴 Higher (~10ms–seconds, depending)                      | 🟢 Low (5–10ms P99)                                        |
| **Scalability**         | Horizontal (brokers, partitions)                | Moderate (clustering, sharding) [Vertical & limited clustering] | Moderate (vertical, limited clustering)      | Auto-scaling via AWS infra                                | Horizontal (brokers, bookies, auto-scaling)                |
| **Retry / DLQ**         | Custom (consumer logic or Kafka Streams)        | Built-in (DLX, retry plugins)                                   | Built-in (DLQ, redelivery policies)          | Built-in (DLQ, visibility timeout, retries, delay queues) | Built-in (negative ACK, DLQ, retry topics)                 |
| **Storage**             | Retains messages (logs), configurable TTL       | Queued in memory/disk until ACK                                 | Persistent (file/db-backed)                  | Messages stored for up to 14 days                         | Segmented storage (BookKeeper), tiered storage supported   |
| **Storage Granularity** | Message logs, offsets, time-based GC            | Message-level ACK + TTL                                         | Message ACK + redelivery count               | Message retention duration (configurable)                 | Per-subscription cursors, time/size-based retention        |
| **Protocols**           | Kafka TCP, REST proxy                           | AMQP, MQTT, STOMP, HTTP                                         | JMS, AMQP, MQTT, STOMP, OpenWire             | HTTPS / AWS SDK / SQS API                                 | Pulsar binary protocol, WebSocket, Kafka protocol (proxy)  |
| **Multi-tenancy**       | Limited (requires custom solutions)             | Virtual hosts                                                   | Limited                                      | AWS account/IAM based                                     | ✅ Built-in (namespaces, isolation policies)                |
| **Geo-replication**     | MirrorMaker, Confluent Replicator               | Federation, shovel plugins                                      | Network of brokers                           | Cross-region via application logic                        | ✅ Built-in active-active geo-replication                   |
| **Management UI**       | Kafka Manager, Confluent, CLI                   | RabbitMQ UI (built-in plugin)                                   | Hawtio, Jolokia                              | AWS Console                                               | Pulsar Manager, CLI, REST API                              |
| **Typical Use Cases**   | Event streaming, analytics, CQRS                | Task queues, RPC, microservices                                 | Enterprise integration, legacy systems       | Cloud microservices, serverless                           | Multi-tenant SaaS, geo-distributed apps, unified messaging |
| **Best Use Cases**      | High-throughput analytics, logs, event sourcing | Background jobs, RPC, short messages                            | Legacy systems, enterprise messaging         | Cloud-native apps, decoupling microservices               | Multi-datacenter messaging, queue + stream hybrid needs    |
| **Cost**                | Infra + Ops costs, Confluent for managed        | Self-hosted infra costs                                         | Self-hosted infra costs                      | Pay per request, per GB stored, data transfer             | Infra + Ops costs, StreamNative for managed                |
| **Cloud-native**        | No (unless using Confluent Cloud)               | No (requires server management)                                 | No                                           | ✅ Yes (fully managed AWS service)                         | Partial (StreamNative Cloud, Kesque)                       |
| **License**             | Apache 2.0                                      | MPL-2.0                                                         | Apache 2.0                                   | Proprietary (AWS)                                         | Apache 2.0                                                 |

---

## 📘 Detailed Breakdown: Push vs Pull

| Tool         | Push / Pull    | Details                                                                                                                                                                                                                                                                        |
|--------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Kafka**    | **Pull-based** | Consumers control when to fetch (pull), where (partition), and from which offset. Allows **fine replay control**, **batching**, and **back-pressure handling**. Ideal for **analytics, batch pipelines, event sourcing**.                                                      |
| **RabbitMQ** | **Push-based** | Broker pushes messages to consumers automatically, following routing rules. Offers **fast delivery**, **prefetch control**, and **back-pressure** via ACKs/NACKs. Great for **task queues**, **low-latency jobs**, **RPC-style messaging**.                                    |
| **ActiveMQ** | **Push-based** | Similar to RabbitMQ. Supports **durable subscriptions**, **transactional queues**, and **JMS semantics**. Suited for **enterprise middleware and legacy enterprise apps**.                                                                                                     |
| **SQS**      | **Pull-based** | Consumers must **poll** the queue (long or short polling). FIFO queues guarantee **exactly-once delivery**, with optional **visibility timeout** and **DLQs**. Suited for **serverless, microservices, and loosely coupled cloud apps**.                                       |
| **Pulsar**   | **Both**       | Supports both **push** (via managed subscriptions) and **pull** consumption models. Offers **multiple subscription modes**: Exclusive, Shared, Failover, Key_Shared. Built-in **flow control** and **back-pressure**. Perfect for **unified streaming and queuing workloads**. |

---

## 💰 Cost & Storage Considerations

| Tool         | Cost Model                                                                       | Storage Behavior                                                                                                                     |
|--------------|----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| **Kafka**    | Self-managed infra, or Confluent Cloud (expensive for high-throughput workloads) | Message logs stored on disk; consumers can replay from offsets; **retention configurable** by time or size                           |
| **RabbitMQ** | Open-source; self-hosted; plugins may add overhead                               | Messages kept until **acknowledged**, optionally persisted to disk; TTL + DLQ supported                                              |
| **ActiveMQ** | Open-source; may require tuning/monitoring                                       | Messages stored persistently (file/db); supports redelivery policies                                                                 |
| **SQS**      | **Pay-per-request** + storage fees ($0.40/million requests + $0.09/GB-month)     | Messages retained up to **14 days**; FIFO and delay queues supported                                                                 |
| **Pulsar**   | Self-managed or StreamNative Cloud; separate compute/storage scaling             | **Tiered storage**: hot data in BookKeeper, cold data in object storage (S3/GCS); **infinite retention** possible; cursor-based ACKs |

---

## 🏁 When to Use Which?

| Use Case                                          | Recommended Tool  |
|---------------------------------------------------|-------------------|
| Real-time analytics, logs, event streams          | **Kafka**         |
| Lightweight async jobs, RPC queues                | **RabbitMQ**      |
| Legacy systems with JMS/Java EE                   | **ActiveMQ**      |
| Fully managed messaging for cloud apps            | **Amazon SQS**    |
| Multi-tenant SaaS, geo-distributed, unified model | **Apache Pulsar** |

---

## 📝 Detailed Description

### **1. Apache Kafka**

* **Core Concept**: Distributed log-based pub/sub system designed for high throughput and fault tolerance.
* **Key Strengths**: Efficient at handling huge volumes of real-time data. Ideal for **data pipelines**, **stream processing**, and **event sourcing**.
* **Storage**: Messages are persisted in logs, and consumers can rewind/read from any point.
* **Scalability**: Partitioning across brokers allows for horizontal scalability.
* **Drawbacks**: Requires more setup and tuning. Does not have built-in message routing logic (like topics/queues in RabbitMQ). Limited multi-tenancy support.

---

### **2. RabbitMQ**

* **Core Concept**: Traditional message broker implementing the **AMQP** protocol.
* **Use Case**: Excellent for **job queues**, **RPC**, **task offloading**, and scenarios needing complex **routing patterns** (via exchanges).
* **Features**: Built-in support for **dead letter queues**, **retry**, **acknowledgments**, and **multiple protocols**.
* **Management**: Comes with an excellent management UI and plugins.
* **Drawbacks**: Limited throughput compared to Kafka. Performance decreases with larger queues.

---

### **3. ActiveMQ**

* **Core Concept**: Mature message broker from Apache, often used with **JMS (Java Message Service)**.
* **Strengths**: Enterprise-ready, supports multiple wire protocols (OpenWire, MQTT, AMQP).
* **Flexibility**: Supports both queues and topics, transactions, and various delivery modes.
* **Use Case**: Often used in **legacy enterprise apps** or **Java EE ecosystems**.
* **Drawbacks**: Aging architecture compared to Kafka. Performance is lower and not ideal for massive data streams.

---

### **4. Amazon SQS**

* **Core Concept**: Fully managed, highly available, and scalable queueing service from AWS.
* **Strengths**: Zero operational overhead. Built-in support for **dead-letter queues**, **delay queues**, and **message timers**.
* **Types**: Offers **Standard queues** (at-least-once, best-effort order) and **FIFO queues** (guaranteed order, exactly-once).
* **Use Case**: Great for **microservices**, **serverless**, **autoscaling systems**.
* **Drawbacks**: Higher latency. Vendor lock-in. FIFO queues have limited throughput.

---

### **5. Apache Pulsar**

* **Core Concept**: Cloud-native distributed messaging and streaming platform with **separated compute and storage**.
* **Architecture**: Built on **Apache BookKeeper** for durable storage, enabling independent scaling of brokers and storage.
* **Key Strengths**: 
  - **Multi-tenancy**: Built-in namespace isolation, resource quotas, and authentication/authorization
  - **Geo-replication**: Native support for active-active replication across regions
  - **Unified messaging**: Supports both streaming (like Kafka) and queuing (like RabbitMQ) patterns
  - **Tiered storage**: Automatic offloading of old data to cheaper storage (S3, GCS)
* **Subscription Types**: 
  - **Exclusive**: Single consumer
  - **Shared**: Multiple consumers, round-robin delivery
  - **Failover**: Active/standby consumers
  - **Key_Shared**: Key-based routing to consumers
* **Use Cases**: Multi-tenant SaaS platforms, geo-distributed applications, unified streaming/queuing workloads, long-term message retention
* **Drawbacks**: Newer ecosystem, more complex architecture (brokers + bookies + ZooKeeper), smaller community than Kafka

---

## 🔌 Protocol Comparison

| Feature / Protocol          | **JMS**                                   | **AMQP**                            | **MQTT**                           | **STOMP**                                  | **OpenWire**                      | **Pulsar Protocol**                 |
|-----------------------------|-------------------------------------------|-------------------------------------|------------------------------------|--------------------------------------------|-----------------------------------|-------------------------------------|
| **Full Form**               | Java Message Service                      | Advanced Message Queuing Protocol   | MQ Telemetry Transport             | Streaming Text-Oriented Messaging Protocol | —                                 | —                                   |
| **Standard / Spec**         | Java EE API standard (not a protocol)     | Open standard (1.0)                 | OASIS Standard                     | Simple text-based protocol                 | Binary protocol by ActiveMQ       | Binary protocol by Pulsar           |
| **Designed For**            | Enterprise Java apps (JMS clients)        | Interoperability, reliability       | Low-bandwidth IoT devices          | Easy messaging over WebSockets             | Fast, optimized transport for JMS | High-throughput distributed systems |
| **Transport**               | Typically uses TCP (with broker)          | TCP                                 | TCP (default), SSL/TLS             | TCP, WebSocket                             | TCP                               | TCP, TLS                            |
| **Message Format**          | Java objects (Message, TextMessage)       | Binary with structured frames       | Binary with topic/payload          | Text-based                                 | Binary frames                     | Protobuf-based binary               |
| **Delivery Modes**          | At-most-once, at-least-once, exactly-once | At-most, at-least, exactly-once     | At-most or at-least once (QoS 0-2) | At-most or at-least once                   | At-most, at-least once            | At-least-once, exactly-once         |
| **Routing Logic**           | Implemented in broker (e.g., topics)      | Built-in routing, exchange types    | Simple pub/sub                     | Simple destination model                   | Supports JMS-style topics/queues  | Topic-based with subscriptions      |
| **Header Support**          | Rich headers                              | Rich headers, properties            | Minimal (for lightweight clients)  | Simple headers                             | Full JMS header support           | Message properties, metadata        |
| **Durability**              | Yes (with persistent delivery)            | Yes (durable queues/exchanges)      | Yes (persistent sessions)          | Limited                                    | Yes                               | Yes (BookKeeper backed)             |
| **Security**                | TLS, JAAS, broker-dependent               | SASL, TLS                           | Username/password, TLS             | Limited                                    | Broker-configured (JAAS, TLS)     | TLS, JWT, OAuth2, Athenz            |
| **Use Cases**               | Enterprise Java apps, legacy systems      | Cross-platform enterprise messaging | IoT, embedded systems              | Web-based messaging, debugging             | High-speed transport for JMS apps | Cloud-native distributed messaging  |
| **Broker Support**          | ActiveMQ, HornetQ, etc.                   | RabbitMQ, ActiveMQ, Qpid, Azure SB  | Mosquitto, HiveMQ, EMQX            | ActiveMQ, RabbitMQ                         | ActiveMQ only                     | Pulsar only                         |
| **Client Language Support** | Java only                                 | Multi-language                      | Multi-language                     | Multi-language                             | Java (JMS)                        | Java, Python, Go, C++, .NET, Node   |
| **Pub/Sub Support**         | Yes (topics, durable subscribers)         | Yes                                 | Yes                                | Yes                                        | Yes                               | Yes (with subscription types)       |

---

## 🎯 Key Differentiators Summary

| Feature                         | Kafka | RabbitMQ | ActiveMQ | SQS | Pulsar |
|---------------------------------|-------|----------|----------|-----|--------|
| **Best for throughput**         | ✅     | ❌        | ❌        | ❌   | ✅      |
| **Best for low latency**        | ✅     | ✅        | ❌        | ❌   | ✅      |
| **Built-in multi-tenancy**      | ❌     | 🟡       | ❌        | 🟡  | ✅      |
| **Built-in geo-replication**    | ❌     | 🟡       | ❌        | ❌   | ✅      |
| **Tiered storage**              | ❌     | ❌        | ❌        | ❌   | ✅      |
| **Unified streaming + queuing** | ❌     | ❌        | ❌        | ❌   | ✅      |
| **Zero ops (managed)**          | ❌     | ❌        | ❌        | ✅   | 🟡     |
| **Protocol diversity**          | ❌     | ✅        | ✅        | ❌   | 🟡     |

Legend: ✅ Excellent | 🟡 Good/Partial | ❌ Limited/None

## 🚀 Stream Processing Alternatives to Apache Flink

## 📊 Quick Comparison Matrix

| Framework             | Latency  | State Management | SQL Support | Managed Option | Best Use Case            |
|-----------------------|----------|------------------|-------------|----------------|--------------------------|
| **Flink**             | Very Low | Excellent        | ✅           | AWS/Alibaba    | Complex event processing |
| **Spark Streaming**   | Medium   | Good             | ✅           | Databricks     | Unified batch/stream     |
| **Kafka Streams**     | Low      | Excellent        | ❌           | Confluent      | Kafka-centric apps       |
| **Storm**             | Very Low | Basic            | ❌           | ❌              | Simple event processing  |
| **Dataflow**          | Low      | Excellent        | ✅           | GCP            | Serverless on GCP        |
| **Kinesis Analytics** | Low      | Good             | ✅           | AWS            | Serverless on AWS        |
| **ksqlDB**            | Low      | Good             | ✅           | Confluent      | SQL streaming            |
| **Pulsar Functions**  | Low      | Basic            | ❌           | StreamNative   | Pulsar processing        |

## 🎯 Decision Guide

**Choose based on your priorities:**

- **Lowest Latency**: Storm, Hazelcast Jet, Flink
- **Easiest to Use**: ksqlDB, Kinesis Analytics, Dataflow
- **Best State Management**: Flink, Kafka Streams, Spark
- **Serverless/Managed**: Dataflow, Kinesis Analytics, Confluent Cloud
- **Python-First**: Bytewax, Beam (Python SDK), Spark
- **SQL-Based**: ksqlDB, Spark SQL, Kinesis Analytics SQL
- **Unified Batch+Stream**: Spark, Beam, Flink
- **Kubernetes-Native**: Flink, Spark, Spring Cloud Data Flow


## 🔍 Hazelcast Jet vs Hazelcast: Complete Comparison

### **Hazelcast**

* **Core Concept**: In-Memory Data Grid (IMDG) with distributed pub/sub capabilities as a secondary feature.
* **Architecture**: Peer-to-peer cluster with no master node, all members are equal.
* **Messaging Features**: 
  - **Topics**: Distributed publish/subscribe messaging (ITopic)
  - **Queues**: Distributed queues (IQueue) for work distribution
  - **Event System**: Listeners for entry events, map events, member events
* **Key Characteristics**:
  - **Ultra-low latency**: Sub-millisecond message delivery
  - **Fire-and-forget**: No acknowledgments or delivery guarantees
  - **No persistence**: Messages lost if no active listeners
  - **No replay**: Once delivered, messages cannot be retrieved
* **Best For**:
  - **Cache invalidation**: Notify cluster members of cache changes
  - **Cluster coordination**: Member discovery, distributed locks
  - **Real-time dashboards**: Live metrics that can afford loss
  - **In-memory processing**: When messaging is secondary to data grid
* **Limitations**:
  - Not a true message broker - messaging is a feature, not the focus
  - No message persistence or durability
  - No complex routing or filtering
  - Limited to Java ecosystem (though clients exist for other languages)
* **Drawbacks**: Not suitable for reliable messaging, no message history, no acknowledgments

### **Overview**

**Hazelcast (IMDG - In-Memory Data Grid)**
- Distributed in-memory computing platform
- Focus: Caching, data storage, distributed computing
- Released: 2008
- Core purpose: Fast data access and distributed data structures

**Hazelcast Jet**
- Distributed stream processing engine
- Focus: Real-time data processing, streaming analytics
- Released: 2017
- Core purpose: Low-latency stream and batch processing

> **📢 Important Update**: As of Hazelcast 5.0 (2021), Jet has been merged into the main Hazelcast platform as the "Hazelcast Platform". However, understanding their distinct capabilities remains valuable.

### **Core Differences**

| Aspect               | Hazelcast (IMDG)                   | Hazelcast Jet                        |
|----------------------|------------------------------------|--------------------------------------|
| **Primary Use**      | In-memory caching & storage        | Stream processing & analytics        |
| **Data Model**       | Key-value, distributed collections | Event streams, pipelines             |
| **Processing Model** | Request/response, entry processors | Continuous data flow, DAG-based      |
| **API Style**        | Map-like operations, SQL           | Pipeline API, stream transformations |
| **State**            | Distributed data structures        | Processing state + checkpoints       |
| **Typical Workload** | OLTP, caching, session storage     | ETL, real-time analytics, CEP        |

### **Architecture Comparison**

**Hazelcast IMDG Architecture:**
```
┌─────────────────────────────────────┐
│         Application Layer           │
├─────────────────────────────────────┤
│      Hazelcast Client/Member        │
├─────────────────────────────────────┤
│   Distributed Data Structures       │
│   - IMap, IQueue, ITopic            │
│   - Near Cache, Entry Processors    │
├─────────────────────────────────────┤
│     Partitioning & Replication      │
└─────────────────────────────────────┘
```

**Hazelcast Jet Architecture:**
```
┌─────────────────────────────────────┐
│      Stream Sources/Sinks           │
├─────────────────────────────────────┤
│      Job Submission & DAG           │
├─────────────────────────────────────┤
│    Processing Vertices (Operators)  │
│    - Map, Filter, Aggregate         │
├─────────────────────────────────────┤
│    Execution Engine & Threading     │
├─────────────────────────────────────┤
│    State Management & Snapshots     │
└─────────────────────────────────────┘
```

### **Feature Comparison**

| Feature               | Hazelcast IMDG      | Hazelcast Jet                 |
|-----------------------|---------------------|-------------------------------|
| **Distributed Maps**  | ✅ Core feature      | ✅ For state storage           |
| **Stream Processing** | ❌ Limited           | ✅ Core feature                |
| **SQL Support**       | ✅ SQL on maps       | ✅ Streaming SQL               |
| **Event Processing**  | ✅ Topic/Queue based | ✅ Complex event processing    |
| **Fault Tolerance**   | ✅ Data replication  | ✅ Checkpointing               |
| **Batch Processing**  | ❌ Not designed for  | ✅ Unified with streaming      |
| **Connectors**        | Limited             | Kafka, JMS, JDBC, Files, etc. |
| **Windowing**         | ❌                   | ✅ Tumbling, sliding, session  |
| **Back Pressure**     | N/A                 | ✅ Built-in flow control       |

### **Performance Characteristics**

**Hazelcast IMDG:**
- **Latency**: Sub-millisecond for cache hits
- **Throughput**: Millions of ops/sec for reads
- **Scalability**: Linear with cluster size
- **Memory**: All data in RAM

**Hazelcast Jet:**
- **Latency**: Low milliseconds (5-50ms)
- **Throughput**: Millions of events/sec
- **Scalability**: Horizontal via parallelism
- **Memory**: Configurable state backend

### **When to Use Which?**

**Use Hazelcast IMDG when you need:**
- ✅ High-speed caching layer
- ✅ Session replication
- ✅ Distributed data structures
- ✅ In-memory compute grid
- ✅ Pub/sub messaging
- ✅ Web application scaling

**Use Hazelcast Jet when you need:**
- ✅ Real-time stream processing
- ✅ Complex event processing (CEP)
- ✅ ETL pipelines
- ✅ Streaming analytics
- ✅ Time-windowed aggregations
- ✅ Continuous data enrichment

### **Decision Matrix**

| Requirement              | Recommended Choice      |
|--------------------------|-------------------------|
| Pure caching needs       | Hazelcast IMDG features |
| Stream processing        | Hazelcast Jet features  |
| Both caching + streaming | Hazelcast Platform 5.0+ |
| Existing IMDG user       | Upgrade to Platform     |
| New project              | Start with Platform     |
| Need just simple cache   | Consider Redis instead  |
| Complex streaming only   | Consider Apache Flink   |

## 📊 Enhanced Feature Comparison Table

| Feature / Tool          | **Kafka**                                       | **RabbitMQ**                                                    | **ActiveMQ**                                 | **Amazon SQS**                                            | **Apache Pulsar**                                          | **Hazelcast**                                              |
|-------------------------|-------------------------------------------------|-----------------------------------------------------------------|----------------------------------------------|-----------------------------------------------------------|------------------------------------------------------------|-------------------------------------------------------------|
| **Type**                | Distributed log/event streaming platform        | Message broker (AMQP)                                           | Message broker (JMS/AMQP)                    | Fully-managed message queue                               | Distributed pub-sub messaging platform                     | In-Memory Data Grid with pub/sub                            |
| **Push/Pull Model**     | **Pull-based** (consumer polls)                 | **Push-based** (to consumers)                                   | **Push-based**                               | **Pull-based** (long/short polling)                       | **Both** (push and pull supported)                         |
| **Message Model**       | Pub/Sub (log-based)                             | Queues and topics (Pub/Sub + point-to-point)                    | Queues and topics (Pub/Sub + point-to-point) | Queues (point-to-point)                                   | Unified model (streaming + queuing)                        |
| **Persistence**         | Durable by default (log retention)              | Optional (via persistence plugins)                              | Persistent (JMS store-based)                 | Persistent (cloud-managed)                                | Durable by default (BookKeeper)                            |
| **Granularity**         | Full control: offset, partition, replay         | Moderate: acknowledgments, routing                              | Moderate: durable subscriptions, ACKs        | Limited: poll-based, FIFO optional                        | Full control: cursor, subscription modes, replay           |
| **Delivery Semantics**  | At least once / Exactly once (configurable)     | At most / At least once                                         | At most / At least once                      | At least once (default), Exactly once (FIFO)              | At least once / Exactly once (via transactions)           |
| **Ordering**            | Strong per partition                            | Per queue or topic                                              | Per queue/topic                              | Strict FIFO with FIFO queues                              | Strong per partition/topic                                 |
| **Throughput**          | ⚡ Very high (millions/sec)                      | High                                                            | Medium                                       | Medium (scalable with batching)                           | ⚡ Very high (millions/sec)                                |
| **Latency**             | 🟢 Low (1–10ms)                                 | 🟢 Low (~1–5ms)                                                | 🟡 Medium (10–50ms)                          | 🔴 Higher (~10ms–seconds, depending)                     | 🟢 Low (5–10ms P99)                                        |
| **Scalability**         | Horizontal (brokers, partitions)                | Moderate (clustering, sharding) [Vertical & limited clustering] | Moderate (vertical, limited clustering)      | Auto-scaling via AWS infra                                | Horizontal (brokers, bookies, auto-scaling)               |
| **Retry / DLQ**         | Custom (consumer logic or Kafka Streams)        | Built-in (DLX, retry plugins)                                   | Built-in (DLQ, redelivery policies)          | Built-in (DLQ, visibility timeout, retries, delay queues) | Built-in (negative ACK, DLQ, retry topics)                |
| **Storage**             | Retains messages (logs), configurable TTL       | Queued in memory/disk until ACK                                 | Persistent (file/db-backed)                  | Messages stored for up to 14 days                         | Segmented storage (BookKeeper), tiered storage supported   |
| **Storage Granularity** | Message logs, offsets, time-based GC            | Message-level ACK + TTL                                         | Message ACK + redelivery count               | Message retention duration (configurable)                 | Per-subscription cursors, time/size-based retention        |
| **Protocols**           | Kafka TCP, REST proxy                           | AMQP, MQTT, STOMP, HTTP                                         | JMS, AMQP, MQTT, STOMP, OpenWire             | HTTPS / AWS SDK / SQS API                                 | Pulsar binary protocol, WebSocket, Kafka protocol (proxy)  |
| **Multi-tenancy**       | Limited (requires custom solutions)             | Virtual hosts                                                   | Limited                                      | AWS account/IAM based                                     | ✅ Built-in (namespaces, isolation policies)               |
| **Geo-replication**     | MirrorMaker, Confluent Replicator               | Federation, shovel plugins                                      | Network of brokers                           | Cross-region via application logic                        | ✅ Built-in active-active geo-replication                  |
| **Management UI**       | Kafka Manager, Confluent, CLI                   | RabbitMQ UI (built-in plugin)                                   | Hawtio, Jolokia                              | AWS Console                                               | Pulsar Manager, CLI, REST API                              |
| **Typical Use Cases**   | Event streaming, analytics, CQRS                | Task queues, RPC, microservices                                 | Enterprise integration, legacy systems       | Cloud microservices, serverless                           | Multi-tenant SaaS, geo-distributed apps, unified messaging |
| **Best Use Cases**      | High-throughput analytics, logs, event sourcing | Background jobs, RPC, short messages                            | Legacy systems, enterprise messaging         | Cloud-native apps, decoupling microservices               | Multi-datacenter messaging, queue + stream hybrid needs    |
| **Cost**                | Infra + Ops costs, Confluent for managed        | Self-hosted infra costs                                         | Self-hosted infra costs                      | Pay per request, per GB stored, data transfer             | Infra + Ops costs, StreamNative for managed               |
| **Cloud-native**        | No (unless using Confluent Cloud)               | No (requires server management)                                 | No                                           | ✅ Yes (fully managed AWS service)                         | Partial (StreamNative Cloud, Kesque)                       |
| **License**             | Apache 2.0                                      | MPL-2.0                                                         | Apache 2.0                                   | Proprietary (AWS)                                         | Apache 2.0                                                 |

---

## 📘 Detailed Breakdown: Push vs Pull

| Tool           | Push / Pull      | Details                                                                                                                                                                                                                                                                           |
|----------------|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Kafka**      | **Pull-based**   | Consumers control when to fetch (pull), where (partition), and from which offset. Allows **fine replay control**, **batching**, and **back-pressure handling**. Ideal for **analytics, batch pipelines, event sourcing**.                                                         |
| **RabbitMQ**   | **Push-based**   | Broker pushes messages to consumers automatically, following routing rules. Offers **fast delivery**, **prefetch control**, and **back-pressure** via ACKs/NACKs. Great for **task queues**, **low-latency jobs**, **RPC-style messaging**.                                       |
| **ActiveMQ**   | **Push-based**   | Similar to RabbitMQ. Supports **durable subscriptions**, **transactional queues**, and **JMS semantics**. Suited for **enterprise middleware and legacy enterprise apps**.                                                                                                        |
| **SQS**        | **Pull-based**   | Consumers must **poll** the queue (long or short polling). FIFO queues guarantee **exactly-once delivery**, with optional **visibility timeout** and **DLQs**. Suited for **serverless, microservices, and loosely coupled cloud apps**.                                          |
| **Pulsar**     | **Both**         | Supports both **push** (via managed subscriptions) and **pull** consumption models. Offers **multiple subscription modes**: Exclusive, Shared, Failover, Key_Shared. Built-in **flow control** and **back-pressure**. Perfect for **unified streaming and queuing workloads**. |
| **Hazelcast**  | **Push-based**   | Event-driven via **listeners** on distributed topics. **Fire-and-forget** model with no acknowledgments. Messages delivered to all active listeners only. Best for **cache invalidation**, **cluster coordination**, and **ephemeral real-time events**.                       |

---

## 💰 Cost & Storage Considerations

| Tool           | Cost Model                                                                       | Storage Behavior                                                                                                                     |
|----------------|----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| **Kafka**      | Self-managed infra, or Confluent Cloud (expensive for high-throughput workloads) | Message logs stored on disk; consumers can replay from offsets; **retention configurable** by time or size                           |
| **RabbitMQ**   | Open-source; self-hosted; plugins may add overhead                               | Messages kept until **acknowledged**, optionally persisted to disk; TTL + DLQ supported                                              |
| **ActiveMQ**   | Open-source; may require tuning/monitoring                                       | Messages stored persistently (file/db); supports redelivery policies                                                                 |
| **SQS**        | **Pay-per-request** + storage fees ($0.40/million requests + $0.09/GB-month)     | Messages retained up to **14 days**; FIFO and delay queues supported                                                                 |
| **Pulsar**     | Self-managed or StreamNative Cloud; separate compute/storage scaling             | **Tiered storage**: hot data in BookKeeper, cold data in object storage (S3/GCS); **infinite retention** possible; cursor-based ACKs |
| **Hazelcast**  | Self-managed or Hazelcast Cloud; memory-based pricing                            | **No storage** - messages exist only during delivery; **no persistence**, **no replay**; purely ephemeral messaging                  |

---

## 🏁 When to Use Which?

| Use Case                                          | Recommended Tool   |
|---------------------------------------------------|-------------------|
| Real-time analytics, logs, event streams          | **Kafka**         |
| Lightweight async jobs, RPC queues                | **RabbitMQ**      |
| Legacy systems with JMS/Java EE                   | **ActiveMQ**      |
| Fully managed messaging for cloud apps            | **Amazon SQS**    |
| Multi-tenant SaaS, geo-distributed, unified model | **Apache Pulsar** |
