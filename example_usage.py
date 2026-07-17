"""
example_usage.py -- Demonstrates NileMultiTenantDbClient usage.
"""
from client import NileMultiTenantDbClient

def main():
    client = NileMultiTenantDbClient()
    result = client.execute_query(
        tenant_id="tenant_org_99248",
        sql_query="SELECT * FROM products WHERE price < 100.0",
        vector_query_embedding=[0.12, 0.98, -0.45, 0.23]
    )
    print(f"[Nile Multi-Tenant DB Route: Authorized = {result['tenant_authorized']}]")
    print(f"Isolated Query: {result['isolated_sql_statement']}")
    print(f"Vector Matches under Tenant Context: {result['vector_matches_count']}")

if __name__ == "__main__":
    main()
