# Multilingual Translation System: Database Design Breakdown

## Problem Understanding

### Core Requirements
- Store translations for multiple languages (100+ languages)
- Support website UI strings, user-generated content, help docs
- Handle millions of translation keys
- Serve translations with <50ms latency globally
- Support real-time updates
- Enable translator collaboration
- Track translation versions/history

### Scale Assumptions
- **Languages**: 100+ supported
- **Translation Keys**: 10M+ unique keys
- **Total Translations**: 1B+ (keys × languages)
- **Read QPS**: 1M+ (highly cacheable)
- **Write QPS**: 10K (translations + updates)
- **Data Size**: ~1-10TB depending on content

## Database Selection

### Primary Database Options

| Database Type | Recommendation | Why | Concerns |
|--------------|----------------|-----|----------|
| **PostgreSQL** | ✅ Primary Choice | JSONB support, full-text search, ACID, mature | Single master writes |
| **MongoDB** | ✅ Good Alternative | Flexible schema, horizontal scaling | Eventually consistent |
| **Cassandra** | ⚠️ Specific Cases | Massive scale, multi-region | Complex queries |
| **DynamoDB** | ⚠️ If on AWS | Managed, scalable | Vendor lock-in |
| **MySQL** | ❌ Not Ideal | Limited JSON, harder sharding | Less flexible |

### Hybrid Approach (Recommended)
```
PostgreSQL (primary) + Redis (cache) + Elasticsearch (search) + S3 (archives)
```

## Schema Design

### Option 1: Normalized Schema (Traditional)
```sql
-- Languages table
CREATE TABLE languages (
    id SERIAL PRIMARY KEY,
    code VARCHAR(10) UNIQUE NOT NULL,  -- 'en', 'es', 'zh-CN'
    name VARCHAR(100) NOT NULL,
    is_active BOOLEAN DEFAULT true,
    direction VARCHAR(3) DEFAULT 'ltr'  -- 'ltr' or 'rtl'
);

-- Translation keys (source content)
CREATE TABLE translation_keys (
    id BIGSERIAL PRIMARY KEY,
    key VARCHAR(500) UNIQUE NOT NULL,  -- 'homepage.welcome.title'
    description TEXT,
    category VARCHAR(100),
    max_length INTEGER,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Actual translations
CREATE TABLE translations (
    id BIGSERIAL PRIMARY KEY,
    key_id BIGINT REFERENCES translation_keys(id),
    language_id INTEGER REFERENCES languages(id),
    translated_text TEXT NOT NULL,
    status VARCHAR(20) DEFAULT 'draft',  -- draft, reviewed, approved
    translator_id INTEGER,
    reviewed_by INTEGER,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    version INTEGER DEFAULT 1,
    UNIQUE(key_id, language_id)
);

-- Translation history
CREATE TABLE translation_history (
    id BIGSERIAL PRIMARY KEY,
    translation_id BIGINT REFERENCES translations(id),
    translated_text TEXT NOT NULL,
    changed_by INTEGER,
    changed_at TIMESTAMP DEFAULT NOW(),
    version INTEGER
);
```

### Option 2: Document-Oriented Schema (PostgreSQL JSONB)
```sql
-- Single table with JSONB
CREATE TABLE translations_jsonb (
    id BIGSERIAL PRIMARY KEY,
    key VARCHAR(500) NOT NULL,
    category VARCHAR(100),
    translations JSONB NOT NULL,  -- {"en": "Hello", "es": "Hola", ...}
    metadata JSONB,  -- {"max_length": 50, "description": "..."}
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    UNIQUE(key)
);

-- Example JSONB structure
{
    "en": {
        "text": "Welcome to our website",
        "status": "approved",
        "translator_id": 123,
        "updated_at": "2024-01-15T10:00:00Z"
    },
    "es": {
        "text": "Bienvenido a nuestro sitio web",
        "status": "reviewed",
        "translator_id": 456,
        "updated_at": "2024-01-14T15:30:00Z"
    }
}
```

### Option 3: Hybrid Schema (Recommended)
```sql
-- Core translations table
CREATE TABLE translations_hybrid (
    id BIGSERIAL PRIMARY KEY,
    key VARCHAR(500) NOT NULL,
    namespace VARCHAR(100) NOT NULL,  -- 'ui', 'content', 'help'
    translations JSONB NOT NULL,
    metadata JSONB,
    search_vector tsvector,  -- For full-text search
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    UNIQUE(namespace, key)
);

-- Indexes
CREATE INDEX idx_translations_key ON translations_hybrid(key);
CREATE INDEX idx_translations_namespace ON translations_hybrid(namespace);
CREATE INDEX idx_translations_jsonb ON translations_hybrid USING GIN(translations);
CREATE INDEX idx_translations_search ON translations_hybrid USING GIN(search_vector);

-- Language configuration
CREATE TABLE language_config (
    code VARCHAR(10) PRIMARY KEY,
    name VARCHAR(100),
    fallback_code VARCHAR(10),  -- Fallback language
    is_active BOOLEAN DEFAULT true,
    config JSONB  -- Pluralization rules, etc.
);
```

## Sharding Strategy

### Sharding Dimensions

| Dimension | Pros | Cons | Use When |
|-----------|------|------|----------|
| **By Language** | Clear boundaries, regional deployment | Uneven distribution, cross-language queries hard | Regional compliance required |
| **By Key Hash** | Even distribution, predictable | No locality, complex queries | Massive scale needed |
| **By Namespace** | Logical separation, different SLAs | May have hot shards | Clear domain boundaries |
| **By Key Range** | Ordered access, range queries | Hotspots possible | Sequential access patterns |

### Recommended: Namespace-Based Sharding
```
Shard 1: UI translations (high read, cached)
Shard 2: User content (high write)
Shard 3: Help docs (large content)
Shard 4: Marketing content (frequent updates)
```

### Implementation
```sql
-- Shard mapping table
CREATE TABLE shard_mapping (
    namespace VARCHAR(100) PRIMARY KEY,
    shard_id INTEGER NOT NULL,
    connection_string TEXT NOT NULL
);

-- Application-level sharding
class TranslationRepository:
    def get_shard(self, namespace):
        shard = db.query("SELECT shard_id FROM shard_mapping WHERE namespace = ?", namespace)
        return self.connections[shard.shard_id]
    
    def get_translation(self, namespace, key, language):
        shard = self.get_shard(namespace)
        return shard.query(
            "SELECT translations->? FROM translations_hybrid WHERE namespace = ? AND key = ?",
            language, namespace, key
        )
```

## Partitioning Strategy

### Partition Dimensions

| Strategy | Implementation | Benefits | Drawbacks |
|----------|---------------|----------|-----------|
| **By Time** | Monthly/yearly partitions | Easy archival, time-based queries | Not ideal for translations |
| **By Language** | One partition per language | Regional deployment | Cross-language queries slow |
| **By Namespace** | Partition per domain | Maintenance isolation | Limited partitions |
| **By Key Hash** | Hash partitioning | Even distribution | No query optimization |

### Recommended: Composite Partitioning
```sql
-- PostgreSQL 12+ declarative partitioning
CREATE TABLE translations_master (
    id BIGSERIAL,
    namespace VARCHAR(100) NOT NULL,
    key VARCHAR(500) NOT NULL,
    translations JSONB NOT NULL,
    metadata JSONB,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    PRIMARY KEY (id, namespace)
) PARTITION BY LIST (namespace);

-- Create partitions
CREATE TABLE translations_ui PARTITION OF translations_master
    FOR VALUES IN ('ui', 'buttons', 'navigation');

CREATE TABLE translations_content PARTITION OF translations_master
    FOR VALUES IN ('user_content', 'posts', 'comments');

CREATE TABLE translations_help PARTITION OF translations_master
    FOR VALUES IN ('help', 'docs', 'faq');

-- Sub-partition by key hash for large namespaces
CREATE TABLE translations_ui_0 PARTITION OF translations_ui
    FOR VALUES WITH (modulus 4, remainder 0);
```

## Complete Architecture

### 1. Write Path
```
API Request → Load Balancer → API Server
                                  ↓
                            Validation Layer
                                  ↓
                            PostgreSQL (Primary)
                                  ↓
                    ┌─────────────┴─────────────┐
                    ↓                           ↓
              Redis Cache                 Elasticsearch
              (Invalidate)                  (Index)
```

### 2. Read Path
```
API Request → Load Balancer → API Server
                                  ↓
                            Redis Cache
                           (99% hit rate)
                                  ↓ (miss)
                            PostgreSQL
                             (Sharded)
```

### 3. Global Distribution
```
Users → CloudFlare/CDN → Regional API Clusters
                              ↓
                    Regional Redis Clusters
                              ↓
                    Regional Read Replicas
                              ↓
                    Primary PostgreSQL Cluster
                         (Write master)
```

## Optimization Strategies

### 1. Caching Strategy
```python
class TranslationCache:
    def get_translations(self, namespace, keys, language):
        # Try Redis first
        cache_keys = [f"{namespace}:{key}:{language}" for key in keys]
        cached = redis.mget(cache_keys)
        
        # Fetch missing from DB
        missing = [k for k, v in zip(keys, cached) if v is None]
        if missing:
            db_results = self.fetch_from_db(namespace, missing, language)
            # Cache with 24h TTL
            for key, value in db_results.items():
                redis.setex(f"{namespace}:{key}:{language}", 86400, value)
        
        return merge_results(cached, db_results)
```

### 2. Bulk Loading
```sql
-- Efficient bulk loading for initial translations
COPY translations_hybrid (key, namespace, translations) FROM STDIN WITH (FORMAT csv);

-- Or using INSERT with JSONB
INSERT INTO translations_hybrid (key, namespace, translations)
SELECT 
    t.key,
    t.namespace,
    jsonb_object_agg(t.language, jsonb_build_object(
        'text', t.text,
        'status', t.status
    ))
FROM temp_translations t
GROUP BY t.key, t.namespace
ON CONFLICT (namespace, key) 
DO UPDATE SET translations = EXCLUDED.translations;
```

### 3. Query Optimization
```sql
-- Get all translations for a namespace/language
SELECT 
    key,
    translations->>'en' as text
FROM translations_hybrid
WHERE 
    namespace = 'ui' AND
    translations ? 'en' AND
    (translations->'en'->>'status') = 'approved';

-- Full-text search across translations
SELECT 
    key,
    translations
FROM translations_hybrid
WHERE 
    search_vector @@ plainto_tsquery('spanish', 'bienvenido');
```

## Scaling Considerations

### Horizontal Scaling Path
```
Stage 1: Single PostgreSQL + Redis Cache
         ↓ (10M translations)
Stage 2: Read replicas + Regional caches  
         ↓ (100M translations)
Stage 3: Namespace sharding
         ↓ (1B translations)
Stage 4: Geographic sharding + Edge caching
         ↓ (10B+ translations)
Stage 5: Move to Cassandra/DynamoDB for specific namespaces
```

### Performance Targets
- **Read Latency**: <10ms from cache, <50ms from DB
- **Write Latency**: <100ms for single update
- **Bulk Import**: 100K translations/minute
- **Cache Hit Rate**: >95%
- **Global Availability**: 99.99%

## Migration Strategy

### From Existing System
```python
# ETL pipeline for migration
def migrate_translations():
    # 1. Extract from old system
    old_translations = fetch_legacy_translations()
    
    # 2. Transform to new format
    for batch in chunk(old_translations, 1000):
        new_format = transform_batch(batch)
        
        # 3. Load into new system
        bulk_insert_translations(new_format)
        
        # 4. Verify
        verify_batch(batch)
```

## Best Practices

1. **Version Control**: Track all translation changes
2. **Fallback Chain**: en-US → en → default language
3. **Cache Warming**: Pre-load popular translations
4. **Lazy Loading**: Load translations on demand
5. **Compression**: Compress large translation sets
6. **CDN Integration**: Serve static translation files
7. **A/B Testing**: Support multiple translation versions

## Final Recommendation

For most websites, start with:
- **Database**: PostgreSQL with JSONB
- **Schema**: Hybrid approach (normalized + JSONB)
- **Sharding**: By namespace when needed
- **Partitioning**: By namespace for large datasets
- **Caching**: Redis with CDN for static content
- **Search**: Elasticsearch for translation memory

This provides the best balance of:
- ✅ Flexibility for schema evolution
- ✅ Performance for common queries  
- ✅ Scalability when needed
- ✅ Operational simplicity
- ✅ Cost effectiveness

Scale horizontally only when you hit actual bottlenecks, not prematurely.

# Sample Data for Hybrid Schema

## Table: `translations_hybrid`

| id | key | namespace | translations | metadata | search_vector | created_at | updated_at |
|----|-----|-----------|--------------|----------|---------------|------------|------------|
| 1 | welcome.title | ui | `{"en": {"text": "Welcome", "status": "approved", "translator_id": 101, "updated_at": "2024-01-15T10:00:00Z"}, "es": {"text": "Bienvenido", "status": "approved", "translator_id": 102, "updated_at": "2024-01-15T11:00:00Z"}, "fr": {"text": "Bienvenue", "status": "reviewed", "translator_id": 103, "updated_at": "2024-01-14T09:00:00Z"}, "ja": {"text": "ようこそ", "status": "approved", "translator_id": 104, "updated_at": "2024-01-15T12:00:00Z"}}` | `{"max_length": 50, "description": "Main welcome message", "context": "Homepage header", "variables": []}` | 'welcome':1A 'bienvenu':3C 'bienvenido':2B 'ようこそ':4D | 2024-01-10 08:00:00 | 2024-01-15 12:00:00 |
| 2 | welcome.subtitle | ui | `{"en": {"text": "Start your journey today", "status": "approved", "translator_id": 101, "updated_at": "2024-01-15T10:00:00Z"}, "es": {"text": "Comienza tu viaje hoy", "status": "approved", "translator_id": 102, "updated_at": "2024-01-15T11:00:00Z"}, "fr": {"text": "Commencez votre voyage aujourd'hui", "status": "draft", "translator_id": 103, "updated_at": "2024-01-16T14:00:00Z"}}` | `{"max_length": 100, "description": "Welcome page subtitle", "context": "Below main title", "variables": []}` | 'journey':2A 'viaje':4B 'voyage':6C 'today':3A 'hoy':5B | 2024-01-10 08:00:00 | 2024-01-16 14:00:00 |
| 3 | button.submit | ui | `{"en": {"text": "Submit", "status": "approved", "translator_id": 101, "updated_at": "2024-01-10T08:00:00Z"}, "es": {"text": "Enviar", "status": "approved", "translator_id": 102, "updated_at": "2024-01-10T08:00:00Z"}, "fr": {"text": "Soumettre", "status": "approved", "translator_id": 103, "updated_at": "2024-01-10T08:00:00Z"}, "de": {"text": "Einreichen", "status": "approved", "translator_id": 105, "updated_at": "2024-01-10T08:00:00Z"}, "zh-CN": {"text": "提交", "status": "approved", "translator_id": 106, "updated_at": "2024-01-10T08:00:00Z"}}` | `{"max_length": 20, "description": "Generic submit button", "context": "Form submission", "variables": []}` | 'submit':1A 'enviar':2B 'soumettre':3C 'einreichen':4D '提交':5E | 2024-01-10 08:00:00 | 2024-01-10 08:00:00 |
| 4 | error.network | ui | `{"en": {"text": "Network error. Please try again.", "status": "approved", "translator_id": 101, "updated_at": "2024-01-12T10:00:00Z"}, "es": {"text": "Error de red. Por favor, inténtelo de nuevo.", "status": "approved", "translator_id": 102, "updated_at": "2024-01-12T11:00:00Z"}, "fr": {"text": "Erreur réseau. Veuillez réessayer.", "status": "reviewed", "translator_id": 103, "updated_at": "2024-01-12T12:00:00Z"}}` | `{"max_length": 200, "description": "Network error message", "context": "Error dialog", "severity": "error", "variables": []}` | 'network':1A 'error':2A 'red':4B 'réseau':6C | 2024-01-12 10:00:00 | 2024-01-12 12:00:00 |
| 5 | greeting.user | ui | `{"en": {"text": "Hello, {name}!", "status": "approved", "translator_id": 101, "updated_at": "2024-01-13T09:00:00Z"}, "es": {"text": "¡Hola, {name}!", "status": "approved", "translator_id": 102, "updated_at": "2024-01-13T09:30:00Z"}, "fr": {"text": "Bonjour, {name}!", "status": "approved", "translator_id": 103, "updated_at": "2024-01-13T10:00:00Z"}, "ja": {"text": "こんにちは、{name}さん！", "status": "approved", "translator_id": 104, "updated_at": "2024-01-13T11:00:00Z"}}` | `{"max_length": 50, "description": "Personalized greeting", "context": "User dashboard", "variables": ["name"]}` | 'hello':1A 'hola':2B 'bonjour':3C 'こんにちは':4D | 2024-01-13 09:00:00 | 2024-01-13 11:00:00 |
| 6 | article.privacy.title | content | `{"en": {"text": "Privacy Policy", "status": "approved", "translator_id": 201, "updated_at": "2024-01-01T10:00:00Z"}, "es": {"text": "Política de Privacidad", "status": "approved", "translator_id": 202, "updated_at": "2024-01-02T10:00:00Z"}, "fr": {"text": "Politique de Confidentialité", "status": "approved", "translator_id": 203, "updated_at": "2024-01-03T10:00:00Z"}}` | `{"max_length": null, "description": "Privacy policy title", "context": "Legal pages", "content_type": "legal", "last_legal_review": "2024-01-01"}` | 'privacy':1A 'policy':2A 'privacidad':4B 'confidentialité':6C | 2024-01-01 10:00:00 | 2024-01-03 10:00:00 |
| 7 | help.search.placeholder | help | `{"en": {"text": "Search for help articles...", "status": "approved", "translator_id": 301, "updated_at": "2024-01-14T08:00:00Z"}, "es": {"text": "Buscar artículos de ayuda...", "status": "approved", "translator_id": 302, "updated_at": "2024-01-14T09:00:00Z"}, "de": {"text": "Nach Hilfeartikeln suchen...", "status": "draft", "translator_id": 305, "updated_at": "2024-01-15T10:00:00Z"}}` | `{"max_length": 100, "description": "Search box placeholder", "context": "Help center", "variables": []}` | 'search':1A 'help':3A 'buscar':4B 'ayuda':6B | 2024-01-14 08:00:00 | 2024-01-15 10:00:00 |
| 8 | notification.items_count | ui | `{"en": {"text": {"one": "You have 1 new item", "other": "You have {count} new items"}, "status": "approved", "translator_id": 101, "updated_at": "2024-01-16T10:00:00Z"}, "es": {"text": {"one": "Tienes 1 artículo nuevo", "other": "Tienes {count} artículos nuevos"}, "status": "approved", "translator_id": 102, "updated_at": "2024-01-16T11:00:00Z"}, "fr": {"text": {"one": "Vous avez 1 nouvel article", "other": "Vous avez {count} nouveaux articles"}, "status": "approved", "translator_id": 103, "updated_at": "2024-01-16T12:00:00Z"}}` | `{"max_length": 100, "description": "Item count notification", "context": "Notification bar", "variables": ["count"], "pluralization": true}` | 'item':3A 'new':2A 'artículo':5B 'article':7C | 2024-01-16 10:00:00 | 2024-01-16 12:00:00 |
| 9 | marketing.sale.banner | marketing | `{"en": {"text": "Limited Time: {discount}% OFF Everything!", "status": "approved", "translator_id": 401, "updated_at": "2024-01-17T08:00:00Z"}, "es": {"text": "Tiempo Limitado: ¡{discount}% DE DESCUENTO en Todo!", "status": "approved", "translator_id": 402, "updated_at": "2024-01-17T09:00:00Z"}, "zh-CN": {"text": "限时优惠：全场{discount}折！", "status": "reviewed", "translator_id": 406, "updated_at": "2024-01-17T10:00:00Z"}}` | `{"max_length": 150, "description": "Sale banner text", "context": "Homepage banner", "variables": ["discount"], "expires": "2024-02-01T00:00:00Z"}` | 'limited':1A 'time':2A 'sale':3A 'descuento':6B '优惠':8E | 2024-01-17 08:00:00 | 2024-01-17 10:00:00 |
| 10 | form.validation.email | ui | `{"en": {"text": "Please enter a valid email address", "status": "approved", "translator_id": 101, "updated_at": "2024-01-11T10:00:00Z"}, "es": {"text": "Por favor, introduce una dirección de correo electrónico válida", "status": "approved", "translator_id": 102, "updated_at": "2024-01-11T11:00:00Z"}, "ar": {"text": "يرجى إدخال عنوان بريد إلكتروني صالح", "status": "approved", "translator_id": 107, "updated_at": "2024-01-11T12:00:00Z"}}` | `{"max_length": 200, "description": "Email validation error", "context": "Form validation", "severity": "warning", "rtl_languages": ["ar"]}` | 'email':3A 'valid':4A 'correo':7B 'electrónico':8B | 2024-01-11 10:00:00 | 2024-01-11 12:00:00 |

## Table: `language_config`

| code | name | fallback_code | is_active | config |
|------|------|---------------|-----------|--------|
| en | English | NULL | true | `{"pluralization_rules": {"one": "n == 1", "other": "true"}, "decimal_separator": ".", "thousands_separator": ",", "currency_position": "before", "date_format": "MM/DD/YYYY", "direction": "ltr"}` |
| es | Español | en | true | `{"pluralization_rules": {"one": "n == 1", "other": "true"}, "decimal_separator": ",", "thousands_separator": ".", "currency_position": "before", "date_format": "DD/MM/YYYY", "direction": "ltr"}` |
| fr | Français | en | true | `{"pluralization_rules": {"one": "n <= 1", "other": "true"}, "decimal_separator": ",", "thousands_separator": " ", "currency_position": "after", "date_format": "DD/MM/YYYY", "direction": "ltr"}` |
| de | Deutsch | en | true | `{"pluralization_rules": {"one": "n == 1", "other": "true"}, "decimal_separator": ",", "thousands_separator": ".", "currency_position": "after", "date_format": "DD.MM.YYYY", "direction": "ltr"}` |
| ja | 日本語 | en | true | `{"pluralization_rules": {"other": "true"}, "decimal_separator": ".", "thousands_separator": ",", "currency_position": "before", "date_format": "YYYY/MM/DD", "direction": "ltr", "no_spaces": true}` |
| zh-CN | 简体中文 | en | true | `{"pluralization_rules": {"other": "true"}, "decimal_separator": ".", "thousands_separator": ",", "currency_position": "before", "date_format": "YYYY-MM-DD", "direction": "ltr", "no_spaces": true}` |
| ar | العربية | en | true | `{"pluralization_rules": {"zero": "n == 0", "one": "n == 1", "two": "n == 2", "few": "n % 100 >= 3 && n % 100 <= 10", "many": "n % 100 >= 11", "other": "true"}, "decimal_separator": "٫", "thousands_separator": "٬", "currency_position": "after", "date_format": "DD/MM/YYYY", "direction": "rtl"}` |
| pt-BR | Português (Brasil) | pt | true | `{"pluralization_rules": {"one": "n >= 0 && n <= 2 && n != 2", "other": "true"}, "decimal_separator": ",", "thousands_separator": ".", "currency_position": "before", "date_format": "DD/MM/YYYY", "direction": "ltr"}` |
| pt | Português | en | false | `{"pluralization_rules": {"one": "n == 1", "other": "true"}, "decimal_separator": ",", "thousands_separator": " ", "currency_position": "after", "date_format": "DD/MM/YYYY", "direction": "ltr"}` |
| ko | 한국어 | en | true | `{"pluralization_rules": {"other": "true"}, "decimal_separator": ".", "thousands_separator": ",", "currency_position": "before", "date_format": "YYYY-MM-DD", "direction": "ltr", "no_spaces": true}` |

## Key Observations from Sample Data:

1. **Translation Structure**: Each language in the JSONB includes text, status, translator_id, and updated_at
2. **Status Workflow**: draft → reviewed → approved
3. **Variable Support**: Translations can include placeholders like {name}, {count}, {discount}
4. **Pluralization**: Some translations (like notification.items_count) include plural forms
5. **RTL Support**: Arabic (ar) is configured with direction: "rtl"
6. **Fallback Chain**: Most languages fall back to English (en)
7. **Metadata Variety**: Different types of content have different metadata (max_length, variables, context, etc.)
8. **Search Vectors**: Automatically generated for full-text search across translations
9. **Namespaces**: Clear separation between ui, content, help, and marketing translations
