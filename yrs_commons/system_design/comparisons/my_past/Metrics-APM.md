# 🎯🎯🎯 APM Metrics

| Company/ µ-service | Throughput | Availability | Size             | Why     |
|--------------------|------------|--------------|------------------|---------|
| **Locus.sh [EKS]** | AWS        |              |                  |         |
| oms-aws-prod       | 868rpm     | B-tree       | 4.5Gi            | Strong  |
| api-aws-prod       | 17 krpm    | R-tree       | 7Gi              | PostGIS |
| lqs-aws-prod       | 45K rpm    | R-tree       | 3.5Gi            | PostGIS |
| iam-aws-prod       | 40.8 krpm  | R-tree       | 3.5Gi            | PostGIS |
| platform-aws-prod  | 17.9 krpm  | R-tree       | 4.5Gi            | PostGIS |
| **Locus.sh [DB]**  | AWS        |              |                  |         |
| oms-aws-prod       | MySQL      | B-tree       | db.r6g.large     | Strong  |
| api-aws-prod       | MySQL      | R-tree       | db.r6g.4xlarge   | PostGIS |
| iam-aws-prod       | MySQL      | R-tree       | db.t4g.medium    | PostGIS |
| platform-aws-prod  | MySQL      | R-tree       | db.r6g.large     | PostGIS |
