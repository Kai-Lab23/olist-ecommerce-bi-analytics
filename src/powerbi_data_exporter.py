import sqlite3
from pathlib import Path

import pandas as pd

from src.config import SQLITE_DB_PATH, SQL_DIR, POWERBI_OUTPUTS_DIR


POWERBI_SQL_FILES = {
    "07_powerbi_fact_sales.sql": "fact_sales.csv",
    "08_powerbi_dim_date.sql": "dim_date.csv",
    "09_powerbi_dim_products.sql": "dim_products.csv",
    "10_powerbi_dim_customers.sql": "dim_customers.csv",
    "11_powerbi_dim_sellers.sql": "dim_sellers.csv",
}


def read_sql_file(sql_file_path: Path) -> str:
    """
    Read SQL query from a SQL file.
    """
    return sql_file_path.read_text(encoding="utf-8")


def run_query(query: str) -> pd.DataFrame:
    """
    Run SQL query against SQLite database.
    """
    with sqlite3.connect(SQLITE_DB_PATH) as connection:
        result = pd.read_sql_query(query, connection)

    return result


def export_powerbi_data() -> None:
    """
    Export Power BI-ready datasets from SQLite database to CSV files.
    """
    POWERBI_OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)

    for sql_file_name, output_file_name in POWERBI_SQL_FILES.items():
        sql_file_path = SQL_DIR / sql_file_name
        output_file_path = POWERBI_OUTPUTS_DIR / output_file_name

        query = read_sql_file(sql_file_path)
        result = run_query(query)

        result.to_csv(output_file_path, index=False)

        print(f"Exported {output_file_name} with {len(result):,} rows.")

    print("Power BI-ready datasets exported successfully.")
    print(f"Saved to: {POWERBI_OUTPUTS_DIR}")


if __name__ == "__main__":
    export_powerbi_data()