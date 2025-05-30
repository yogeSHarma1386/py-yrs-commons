# Key-Value Store Database Comparison

## Table 1: Core Characteristics

| Database | Data Structures Used | Real-World Application | Why It's Used |
|----------|---------------------|------------------------|---------------|
| Redis | In-memory hashtables, sorted sets, lists, streams | Caching, session store, real-time analytics | Speed, rich data structures, pub/sub |
| Amazon DynamoDB | Hash/Range keys, B-tree indexes (GSI) | User sessions, gaming state, serverless backends | Managed service, predictable performance, scale |
| Memcached | Simple hash table, LRU eviction | Pure caching, session storage | Simplicity, raw speed, memory efficiency |
| etcd | B-tree (bbolt), Raft consensus | Kubernetes config, service discovery | Strong consistency, watch API, reliability |
| Apache Cassandra | LSM tree, consistent hashing | Time-series, recommendation engines, messaging | Linear scalability, no SPOF, tunable consistency |

## Use Cases Description

### Redis
- **Session Management**: User sessions with automatic expiration
- **Real-time Analytics**: Counters, HyperLogLog for unique counts
- **Message Queuing**: Pub/sub, streams for event processing
- **Gaming Leaderboards**: Sorted sets for ranking systems

### Amazon DynamoDB
- **Serverless Backends**: API state and configuration
- **Gaming State**: Player inventory, world state
- **IoT Device State**: Current status, last seen timestamps
- **Shopping Carts**: Temporary user data with TTL

### Memcached
- **Database Query Cache**: Expensive query results
- **API Response Cache**: Computed responses
- **Session Storage**: Simple session data
- **Fragment Caching**: HTML/JSON fragments

### etcd
- **Service Discovery**: Microservice endpoints and health
- **Configuration Management**: Distributed config with watches
- **Leader Election**: Distributed system coordination
- **Feature Flags**: Dynamic feature toggles

### Apache Cassandra
- **Time-Series Data**: Metrics, logs, IoT readings
- **User Activity**: Clickstreams, event tracking
- **Message History**: Chat, notifications, feeds
- **Product Catalogs**: Denormalized for fast reads

## Table 2: CA Systems (Consistency + Availability)

| Database | CAP Classification | Characteristics |
|----------|-------------------|-----------------|
| Redis | CA (single node) | Single-threaded consistency, Redis Sentinel for HA |
| DynamoDB | Configurable | Eventually consistent by default, strong consistency optional |
| Memcached | CA (single node) | No built-in replication, client-side sharding |
| etcd | CP (Raft-based) | Strong consistency always, sacrifices availability |
| Cassandra | AP (typically) | Eventually consistent default, tunable per query |

## Table 3: CP Systems (Consistency + Partition Tolerance)

| Database | Configuration | Trade-offs |
|----------|--------------|------------|
| Redis | Redis Cluster with WAIT | Synchronous replication possible, reduced availability |
| DynamoDB | Strong consistency reads | 2x cost, slightly higher latency |
| Memcached | Not supported | No native consistency guarantees |
| etcd | Default operation | Majority quorum required, may reject writes |
| Cassandra | QUORUM/ALL consistency | Higher latency, potential unavailability |

## Table 4: PA Systems (Partition Tolerance + Availability)

| Database | Configuration | Trade-offs |
|----------|--------------|------------|
| Redis | Redis Cluster async | Potential data loss on failover |
| DynamoDB | Eventually consistent | Default mode, lowest cost |
| Memcached | Consistent hashing | Cache misses on node failure |
| etcd | Not typical usage | Designed for consistency |
| Cassandra | ONE/ANY consistency | Conflicts possible, eventual consistency |

## Volume Considerations

| Aspect | Redis | DynamoDB | Memcached | etcd | Cassandra |
|--------|-------|----------|-----------|------|-----------|
| **Sweet Spot** | 1GB - 100GB RAM | Unlimited | 1GB - 100GB RAM | 1MB - 2GB | 100GB - 100TB |
| **Max Key Size** | 512MB | 2KB | 250 bytes | 1.5MB | 64KB |
| **Max Value Size** | 512MB | 400KB | 1MB | 1.5MB | 2GB theoretical |
| **Storage Type** | Memory (optional disk) | Managed service | Memory only | Disk with cache | Disk (memtables in RAM) |
| **Key Difference** | All data in RAM | Infinite scale | Simplest cache | Small consistent data | Massive scale on disk |

## Latency Requirements

| Aspect | Redis | DynamoDB | Memcached | etcd | Cassandra |
|--------|-------|----------|-----------|------|-----------|
| **Read Latency** | <1ms (microseconds) | <10ms guaranteed | <1ms | 1-10ms | 1-10ms |
| **Write Latency** | <1ms | <10ms guaranteed | <1ms | 10-100ms (consensus) | 1-10ms |
| **Network RTT Impact** | Critical | Managed by AWS | Critical | Less critical | Regional impact |
| **Persistence Impact** | 2x with AOF | Not applicable | None | Always persistent | Minimal (async) |
| **Key Difference** | Fastest possible | Predictable SLA | Raw speed | Consistency overhead | Consistent performance |

## Read/Write Workload Patterns

| Aspect | Redis | DynamoDB | Memcached | etcd | Cassandra |
|--------|-------|----------|-----------|------|-----------|
| **Write Throughput** | 100k+ ops/sec/node | Auto-scaling | 100k+ ops/sec/node | 10k ops/sec cluster | 50k+ ops/sec/node |
| **Read Throughput** | 100k+ ops/sec/node | Auto-scaling | 500k+ ops/sec/node | 100k ops/sec cluster | 100k+ ops/sec/node |
| **Batch Operations** | Pipeline, MGET/MSET | BatchGet/Write (25) | Multi-get | Transactions | Batch statements |
| **Concurrent Access** | Single-threaded | Fully concurrent | Thread-per-core | Serialized writes | Fully concurrent |
| **Key Difference** | Single-threaded simple | Managed scaling | Minimal features | Consistency first | Write-optimized |

## Data Structure Requirements

| Aspect | Redis | DynamoDB | Memcached | etcd | Cassandra |
|--------|-------|----------|-----------|------|-----------|
| **Basic Operations** | GET/SET/DEL | GetItem/PutItem | get/set/delete | Get/Put/Delete | SELECT/INSERT/DELETE |
| **Advanced Types** | Lists, sets, hashes, streams | Lists, sets, maps | None | None | Collections, UDTs |
| **Secondary Access** | Pattern matching, indices | GSI/LSI | None | Prefix, range | Secondary indexes |
| **TTL Support** | Per-key expiration | Per-item TTL | Per-key expiration | Lease-based | Per-column TTL |
| **Key Difference** | Richest data types | Document features | Pure K/V only | Simple K/V + watch | Column families |

## Consistency & Availability Requirements

| Aspect | Redis | DynamoDB | Memcached | etcd | Cassandra |
|--------|-------|----------|-----------|------|-----------|
| **Consistency Model** | Strong (single-threaded) | Configurable | None (cache) | Strong (Raft) | Tunable per-op |
| **Replication** | Async (Redis Cluster) | Managed multi-AZ | None built-in | Raft consensus | Configurable RF |
| **Failover Time** | 10-30 seconds | Automatic | N/A (cache) | <10 seconds | <30 seconds |
| **Data Durability** | Optional (RDB/AOF) | 99.999999999% | None | Guaranteed | Configurable |
| **Key Difference** | Memory-first design | Fully managed | Ephemeral only | Consistency-first | Availability-first |

## Replication & Distribution Techniques

| Aspect | Redis | DynamoDB | Memcached | etcd | Cassandra |
|--------|-------|----------|-----------|------|-----------|
| **Sharding Method** | Hash slots (16384) | Automatic | Client-side | Not sharded | Consistent hashing |
| **Replication Type** | Primary-replica | Managed | None | Raft consensus | Peer-to-peer |
| **Cross-DC Support** | Redis Enterprise | Global Tables | None | Multi-region | Built-in |
| **Topology** | Master-slave | Managed | Independent nodes | Leader-followers | Masterless |
| **Key Difference** | Manual clustering | Zero-config | DIY everything | Small clusters only | True peer-to-peer |

## Conflict Resolution Strategies

| Aspect | Redis | DynamoDB | Memcached | etcd | Cassandra |
|--------|-------|----------|-----------|------|-----------|
| **Write Conflicts** | No conflicts (single master) | Last-writer-wins | No replication | No conflicts (Raft) | Last-write-wins |
| **Resolution Method** | N/A | Timestamp-based | N/A | Consensus | Timestamp/custom |
| **Clock Sync** | Not required | Managed | Not required | Not required | Critical (NTP) |
| **Custom Resolution** | Not needed | Limited | Not applicable | Not needed | Application-level |
| **Key Difference** | Avoids conflicts | Simple timestamp | No conflicts | Consensus prevents | Requires planning |

## Scaling Approaches

| Aspect | Redis | DynamoDB | Memcached | etcd | Cassandra |
|--------|-------|----------|-----------|------|-----------|
| **Vertical Scaling** | Limited by RAM | Not applicable | Limited by RAM | Not recommended | Effective |
| **Horizontal Scaling** | Redis Cluster | Automatic | Client sharding | Read replicas only | Linear scaling |
| **Auto-scaling** | Redis Enterprise | Built-in | No | No | No (manual) |
| **Scale Unit** | Shard (hash slot range) | Partition | Single node | Cluster member | Node |
| **Key Difference** | Memory-bound | Serverless | Manual everything | Not for big data | Best linear scale |

## Operational Considerations

| Aspect | Redis | DynamoDB | Memcached | etcd | Cassandra |
|--------|-------|----------|-----------|------|-----------|
| **Management Complexity** | Medium | None | Low | Medium | High |
| **Monitoring** | INFO command, Redis Insight | CloudWatch | Stats command | Metrics endpoint | JMX, nodetool |
| **Backup Strategy** | RDB snapshots, AOF | Continuous, automatic | Not applicable | Snapshots | Snapshots, repairs |
| **Memory Management** | Eviction policies | Not applicable | LRU only | Bounded size | JVM heap tuning |
| **Key Difference** | Rich tooling | Fully managed | Minimal features | K8s integrated | Most complex |

## Decision Matrix for Common Use Cases

| Use Case | Best Choice | Why | Avoid | Why Not |
|----------|-------------|-----|-------|---------|
| **Simple Caching** | Memcached | Fastest, simplest, proven | etcd | Overkill for cache |
| **Session Store** | Redis | TTL, data structures | Cassandra | Too heavy |
| **Rate Limiting** | Redis | Atomic counters, Lua scripts | DynamoDB | Latency overhead |
| **Service Discovery** | etcd | Watches, consistency | Memcached | No persistence |
| **Time-Series Data** | Cassandra | Built for it, compression | etcd | Size limitations |
| **Serverless State** | DynamoDB | Zero ops, auto-scale | Redis | Requires infrastructure |
| **Gaming Leaderboards** | Redis | Sorted sets perfect fit | Memcached | No data structures |
| **Configuration Store** | etcd | Version history, watches | Memcached | No persistence |
| **Message History** | Cassandra | Time-based partitioning | Memcached | No persistence |
| **Feature Flags** | Redis | Fast, pub/sub for updates | Cassandra | Overkill |

## Key Differentiators Summary

### Redis
- **Strengths**: Fastest, rich data structures, Lua scripting, pub/sub
- **Weaknesses**: Memory cost, persistence complexity, clustering complexity
- **Choose when**: Need speed, complex operations, real-time features

### DynamoDB
- **Strengths**: Serverless, infinite scale, predictable performance, managed
- **Weaknesses**: AWS lock-in, limited operations, cost at scale
- **Choose when**: Building on AWS, want zero operations, need auto-scale

### Memcached
- **Strengths**: Simplest, fastest, memory efficient, battle-tested
- **Weaknesses**: No persistence, no data structures, no replication
- **Choose when**: Pure caching, maximum simplicity, proven solution

### etcd
- **Strengths**: Strong consistency, watches, Kubernetes native, reliable
- **Weaknesses**: Small data only, slower writes, limited scale
- **Choose when**: Service discovery, configuration, distributed coordination

### Cassandra
- **Strengths**: Linear scaling, no SPOF, time-series optimized, multi-DC
- **Weaknesses**: Complexity, eventual consistency, JVM tuning
- **Choose when**: Massive scale, time-series data, multi-datacenter

## Architecture Decision Points

**Choose based on:**
1. **Speed Requirements**: Redis = Memcached > DynamoDB = Cassandra > etcd
2. **Scale Requirements**: DynamoDB = Cassandra > Redis > Memcached > etcd
3. **Operational Simplicity**: DynamoDB > Memcached > Redis > etcd > Cassandra
4. **Feature Richness**: Redis > Cassandra > DynamoDB > etcd > Memcached
5. **Consistency Needs**: etcd > Redis > Cassandra (tunable) > DynamoDB > Memcached

## Real-World Key-Value Store Use Cases

### Redis Real-World Implementations

| Company/Organization | Use Case | Why Redis | Scale/Impact |
|---------------------|----------|-----------|--------------|
| **Twitter** | Timeline caching, social graph | Speed, sorted sets for timelines | 500M tweets/day cached |
| **GitHub** | Repository metadata, background jobs | Sidekiq queues, caching layer | 100M+ repositories |
| **Stack Overflow** | Real-time statistics, caching | Pub/sub for updates, speed | 100M+ monthly visitors |
| **Uber** | Geospatial driver matching | Geospatial commands, speed | 15M+ rides daily |
| **Pinterest** | Feed generation, follower lists | Sorted sets, high throughput | 450M+ monthly users |
| **Snapchat** | Story views, friend activity | Expiring keys, counters | 375M+ daily users |

**Key Pattern**: Redis dominates real-time features, caching layers, and anywhere rich data structures provide value.

### DynamoDB Real-World Implementations (Key-Value Specific)

| Company/Organization | Use Case | Why DynamoDB | Scale/Impact |
|---------------------|----------|---------------|--------------|
| **Airbnb** | User sessions, search sessions | Auto-scaling, low latency | 150M+ users |
| **Capital One** | Customer sessions, API tokens | Serverless, compliance | 65M+ customers |
| **Tinder** | User swipes, match state | Global low latency | 75M+ monthly users |
| **Samsung** | IoT device state, SmartThings | Scale, global distribution | 100M+ devices |
| **Expedia** | Search cache, pricing cache | Predictable performance | 750M+ searches/day |
| **MLB (Major League Baseball)** | Real-time game stats | Burst scaling | 10M+ concurrent viewers |

**Key Pattern**: DynamoDB excels for serverless architectures, unpredictable scale, and global state management.

### Memcached Real-World Implementations

| Company/Organization | Use Case | Why Memcached | Scale/Impact |
|---------------------|----------|---------------|--------------|
| **Facebook** | MySQL query cache, object cache | Simplicity at scale, mcrouter | Billions of objects |
| **YouTube** | Video metadata cache | Simple and fast | 2B+ users |
| **Reddit** | Comment trees, listing cache | Drop-in caching | 52M+ daily users |
| **Slack** | Message cache, user presence | Simple caching needs | 20M+ daily users |
| **Box** | File metadata cache | Standard caching | 100M+ users |
| **Zynga** | Game state caching | Facebook games era | 100M+ monthly players |

**Key Pattern**: Memcached remains the choice for simple, high-volume caching without fancy features.

### etcd Real-World Implementations

| Company/Organization | Use Case | Why etcd | Scale/Impact |
|---------------------|----------|----------|--------------|
| **Kubernetes (All Users)** | Cluster state, configuration | Built for Kubernetes | Powers millions of clusters |
| **CoreOS/Red Hat** | Container Linux updates | Distributed coordination | Fleet management |
| **Salesforce** | Service discovery, configuration | Strong consistency | Multi-tenant services |
| **Baidu** | Service mesh configuration | Consistency, watches | China's largest search |
| **SoundCloud** | Microservice discovery | Reliable coordination | 175M+ users |
| **Ticketmaster** | Distributed locking, config | Consistency guarantees | High-traffic events |

**Key Pattern**: etcd dominates Kubernetes ecosystems and distributed system coordination needs.

### Cassandra Real-World Implementations (Key-Value Focus)

| Company/Organization | Use Case | Why Cassandra | Scale/Impact |
|---------------------|----------|---------------|--------------|
| **Discord** | Message history, user presence | Time-series, scale | 150M+ monthly users |
| **Instagram** | User feeds, activity | Linear scaling | 2B+ monthly users |
| **Spotify** | User playlists, play history | Multi-DC, scale | 500M+ users |
| **Uber** | Trip history, driver locations | Time-series, global | 130M+ monthly users |
| **Apple** | iMessage (reported) | Scale, reliability | 1B+ Apple devices |
| **eBay** | User activity, recommendations | Write throughput | 190M+ buyers |

**Key Pattern**: Cassandra chosen for time-series data, activity feeds, and multi-datacenter requirements.

## Industry-Specific Patterns

### Gaming Industry
- **Session State**: Redis (Epic Games, Riot)
- **Player Inventory**: DynamoDB (Zynga, Supercell)
- **Match History**: Cassandra (Discord, gaming platforms)
- **Game Servers**: etcd (service discovery)

### Financial Services  
- **Trading Cache**: Redis (high-frequency trading)
- **Session Tokens**: DynamoDB (Capital One, fintech)
- **Transaction History**: Cassandra (payment processors)
- **API Rate Limiting**: Redis (all major banks)

### Social Media
- **Feed Caching**: Redis (Twitter, Pinterest)
- **User Sessions**: DynamoDB (social apps)
- **Activity Streams**: Cassandra (Instagram, Discord)
- **Simple Caching**: Memcached (Facebook, Reddit)

### E-commerce
- **Cart Storage**: Redis (Shopify stores)
- **Session Management**: DynamoDB (Amazon, Airbnb)
- **Product Views**: Cassandra (recommendation engines)
- **Page Caching**: Memcached (traditional stores)

### Infrastructure/DevOps
- **Service Discovery**: etcd (Kubernetes everywhere)
- **Circuit Breakers**: Redis (Netflix Hystrix)
- **Metrics Storage**: Cassandra (DataDog uses it)
- **Build Cache**: Memcached (CI/CD systems)

## Performance at Scale

### Redis
- **GitHub**: 8TB+ of Redis, microsecond responses
- **Twitter**: Handles 300k+ requests/second per instance
- **Uber**: Processes millions of geospatial queries/minute

### DynamoDB
- **Amazon Prime Day**: 45.5M requests/second
- **Pokemon Go**: Handled 5x expected load automatically
- **Duolingo**: 24B+ items stored

### Memcached
- **Facebook**: 10s of millions of requests/second
- **YouTube**: Terabytes of cache, sub-millisecond

### etcd
- **Large Kubernetes**: 8,000 node clusters
- **CoreOS**: Millions of configuration watches

### Cassandra
- **Apple**: 160,000+ Cassandra instances
- **Netflix**: 1M+ writes/second sustained
- **Discord**: 1T+ messages stored

The choice depends on:
- **Speed Critical**: Redis or Memcached
- **Scale Critical**: DynamoDB or Cassandra  
- **Consistency Critical**: etcd
- **Feature Requirements**: Redis for complex operations
- **Operational Model**: DynamoDB for serverless, Memcached for simple
