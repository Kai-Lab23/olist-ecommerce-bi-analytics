import sqlite3
from pathlib import Path

import pandas as pd

from src.config import SQLITE_DB_PATH, SQL_DIR, SQL_OUTPUTS_DIR


SQL_FILES = [
    "01_kpi_overview.sql",
    "02_monthly_revenue_trend.sql",
    "03_product_category_performance.sql",
    "04_customer_location_analysis.sql",
    "05_payment_analysis.sql",
    "06_delivery_review_analysis.sql",
]


def read_sql_file(sql_file_path: Path) -> str:
    """
    Read SQL query from a .sql file.
    """
    return sql_file_path.read_text(encoding="utf-8")


def run_sql_query(query: str) -> pd.DataFrame:
    """
    Run a SQL query against the SQLite database and return the result as a DataFrame.
    """
    with sqlite3.connect(SQLITE_DB_PATH) as connection:
        result = pd.read_sql_query(query, connection)

    return result


def export_sql_results() -> None:
    """
    Run all SQL files and export the query results to CSV files.
    """
    SQL_OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)

    for sql_file_name in SQL_FILES:
        sql_file_path = SQL_DIR / sql_file_name
        output_file_name = sql_file_name.replace(".sql", ".csv")
        output_file_path = SQL_OUTPUTS_DIR / output_file_name

        query = read_sql_file(sql_file_path)
        result = run_sql_query(query)

        result.to_csv(output_file_path, index=False)

        print(f"Exported: {output_file_name}")


if __name__ == "__main__":
    export_sql_results()