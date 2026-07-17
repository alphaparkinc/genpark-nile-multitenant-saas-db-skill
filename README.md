# genpark-nile-multitenant-saas-db-skill

> **GenPark AI Agent Skill** -- Nile-like serverless PostgreSQL virtual tenant and RAG isolator.

## Quick Start

```python
from client import NileMultiTenantDbClient
client = NileMultiTenantDbClient()
res = client.execute_query("org_123", "SELECT * FROM orders")
print(res["isolated_sql_statement"])
```
