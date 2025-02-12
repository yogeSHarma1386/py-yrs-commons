## **Key Pointers for System Design Interviews** 🚀

---

### **1️⃣ Clarify Requirements First**

- **Functional Requirements:** What the system should do (e.g., user can upload images).
- **Non-Functional Requirements:** Performance, availability, scalability, consistency, latency, fault tolerance.
- **Constraints & Scale:**
  - How many users?
  - How much data per user?
    - Expected **QPS (Queries Per Second)**
    - **Storage requirements** (hot vs. cold storage, data lifecycle management)
    - **Read vs. write ratio** (eventually consistent vs. strongly consistent systems)
    - **Latency expectations** (low-latency caching vs. direct DB access)

✅ **Ask clarifying questions!** It shows structured thinking.

---

### **2️⃣ Define High-Level Architecture**

- **Monolith vs. Microservices vs. Serverless** (trade-offs: deployment complexity, scaling, maintainability)
- **Client-Server vs. Peer-to-Peer (P2P)**
- **Synchronous (REST, gRPC) vs. Asynchronous (Message Queues, WebSockets, Pub/Sub, Event Sourcing)**
- **Event-Driven Architecture vs. Request-Response Model**
- **Data Flow & Processing Pipelines** (Batch Processing vs. Stream Processing)

✅ **Draw a simple block diagram first** before deep-diving into components.

---

### **3️⃣ Break Down Components**

#### **Common System Components:**

- **Load Balancer (LB):** Distributes traffic across servers (e.g., Nginx, AWS ELB, HAProxy).
- **API Gateway:** Handles authentication, rate limiting (e.g., Kong, Apigee, AWS API Gateway).
- **Database Choice:** SQL (PostgreSQL, MySQL) vs. NoSQL (MongoDB, Cassandra, DynamoDB).
- **Caching Layer:** Redis, Memcached for faster reads, CDN caching (Cloudflare, Akamai).
- **Queueing System:** Kafka, RabbitMQ, SQS for async processing.
- **Search System:** ElasticSearch, Solr, OpenSearch.
- **Object Storage:** AWS S3, Google Cloud Storage, MinIO.
- **CDN (Content Delivery Network):** Cloudflare, Akamai for faster content delivery.
- **Container Orchestration:** Kubernetes, Docker Swarm.

✅ **Explain trade-offs!** Why choose Redis over Memcached? Why PostgreSQL over MongoDB?

---

### **4️⃣ Database Design & Scalability**

#### **Key DB Strategies:**

- **Normalization vs. Denormalization** (OLTP vs. OLAP)
- **Indexing for performance** (B-Tree, Hash Index, Bitmap Index)
- **Partitioning:** Vertical (column-based), Horizontal (sharding, consistent hashing)
- **Replication:** Master-Slave, Master-Master, Quorum-Based (Raft, Paxos, ZAB)
- **Consistency Models:**
  - **Strong Consistency:** ACID, 2PC (Two-Phase Commit), distributed transactions; good for banking systems.
    - **Eventual Consistency:** CAP theorem (e.g., DynamoDB, Cassandra, Amazon Aurora).

✅ **When to use SQL vs. NoSQL?** If you need transactions → SQL. If you need scale → NoSQL.

---

### **5️⃣ Caching Strategy (Boost Read Performance)**

#### **Common Cache Strategies**

- **Read-Through:** Data is fetched and stored in cache before returning to the user.
- **Write-Through:** Data is written to cache and database at the same time.
- **Write-Behind:** Delayed writing to the database for better performance.
- **Cache Eviction Policies:**
    - **LRU (Least Recently Used)**
    - **LFU (Least Frequently Used)**
    - **TTL (Time-to-Live Expiry)**

✅ **Cache invalidation is hard!** Explain cache consistency strategies.

---

### **6️⃣ Handling Scale & High Availability**

- **Load Balancing:** Round-robin, least connections, IP hash, consistent hashing.
- **Database Scaling:** Read replicas, leader-follower replication, sharded clusters.
- **CDN for static assets & edge computing**
- **Rate Limiting:** To prevent abuse (e.g., token bucket algorithm).
- **Failure Handling:** Circuit breaker pattern, retries with exponential backoff, graceful degradation.

✅ **Scalability vs. Availability:** Horizontal scaling (more machines) vs. Vertical scaling (bigger machine).

---

### **7️⃣ Concurrency & Distributed Systems**

- **Locking Mechanisms:** Optimistic (compare-and-swap), Pessimistic (row locks, distributed locks with
  Redis/Zookeeper).
- **Event-Driven Systems:** Kafka, RabbitMQ, AWS SNS/SQS for async processing.
- **Leader Election:** Raft, Paxos, ZAB (Zookeeper Atomic Broadcast).
- **Idempotency:** Prevent duplicate transactions with unique request IDs.

✅ **Distributed Transactions:** Explain Saga pattern vs. Two-phase commit.

---

### **8️⃣ Security Considerations**

- **Authentication & Authorization:** OAuth 2.0, JWT tokens, OpenID Connect, SAML.
- **Rate Limiting & DDoS Protection:** API Gateway, Cloudflare, AWS WAF, rate limiting middleware.
- **Encryption:** At-rest (AES-256, KMS), In-transit (TLS 1.3, mutual TLS).
- **Zero Trust Security Model.**
- **Role-Based Access Control (RBAC) & Attribute-Based Access Control (ABAC).**
- **Audit Logging & SIEM (Security Information and Event Management).**

✅ **Security matters!** Always mention data protection measures.

---

### **9️⃣ API Design & Communication**

- **REST vs. gRPC vs. GraphQL vs. WebSockets.**
- **Versioning APIs (v1, v2, deprecation strategies).**
- **Throttling & Rate Limiting (Leaky Bucket, Token Bucket).**
- **API Gateway for aggregation (BFF - Backend for Frontend).**

✅ **Choosing the right API pattern is key!** REST for general use, gRPC for microservices, GraphQL for flexibility.

---

### **🔟 Monitoring & Logging**

- **Observability:** Logs, metrics, traces (ELK Stack, Prometheus, Grafana, OpenTelemetry).
  - ⚠️Give examples around granularity of: metric data, alarms captured
- **Failure Recovery:** Circuit breakers, retries, dead-letter queues, chaos engineering (Netflix Chaos Monkey).
- **Distributed Tracing:** Jaeger, Zipkin, Datadog.

✅ **How do you detect and recover failures?** Always have a logging and alerting strategy.

---

#### **Final Tip: Use the STAR Framework**

✅ **Situation:** What problem are we solving?  
✅ **Task:** What are the key challenges?  
✅ **Action:** What design decisions did we make?  
✅ **Result:** What’s the expected outcome?

---

#### **🔹 Quick Sample Question & Approach**

💡 **"Design a URL Shortener (like Bit.ly)"**

1. **Clarify Requirements:**

  - Users enter a long URL → Get a short URL
  - Redirect when accessing short URL
  - Optional expiry date for URLs
  - Expected QPS (queries per second)?

2. **High-Level Design:**

  - **Client → API Gateway → URL Service → Database (SQL/NoSQL)**
  - Use **hashing + Base62 encoding** for short URLs.
  - Store in **Redis (cache) + DB (persistent storage)**.

3. **Scale Considerations:**

  - **Read-heavy system** → Use **caching** (Redis).
  - **High availability** → Use **replication & load balancers**.

4. **Failure Handling & Security:**

  - **Rate limiting** to prevent abuse.
  - **Expire old URLs** using TTL in Redis.

✅ **Explain trade-offs!** SQL for ACID, NoSQL for scalability.

---

## **🚀 Final Checklist for System Design Success**

✅ Ask questions to clarify **scale & constraints**  
✅ Define a **high-level architecture** before going deep  
✅ Break the system into **core components**  
✅ Justify **DB choices** (SQL vs NoSQL)  
✅ Explain **scalability & availability** strategies  
✅ Consider **caching, load balancing, security**  
✅ Discuss **monitoring, logging, failure handling**

---
