import sqlite3
from pathlib import Path

import pandas as pd

from src.config import PROCESSED_DATA_DIR, DATABASE_DIR, SQLITE_DB_PATH, OUTPUTS_DIR


PROCESSED_TABLES = {
    "cleaned_orders.csv": "orders",
    "cleaned_order_items.csv": "order_items",
    "cleaned_order_payments.csv": "order_payments",
    "cleaned_order_reviews.csv": "order_reviews",
    "cleaned_customers.csv": "customers",
    "cleaned_products.csv": "products",
    "cleaned_sellers.csv": "sellers",
    "cleaned_product_category_translation.csv": "product_category_translation",
}


def validate_processed_files(processed_data_dir: Path = PROCESSED_DATA_DIR) -> None:
    """
    Validate that all required processed CSV files exist.
    """
    missing_files = []

    for file_name in PROCESSED_TABLES.keys():
        file_path = processed_data_dir / file_name

        if not file_path.exists():
            missing_files.append(file_name)

    if missing_files:
        missing_files_text = "\n".join(missing_files)
        raise FileNotFoundError(
            f"The following processed files are missing:\n{missing_files_text}"
        )

    print("All required processed CSV files are available.")


def load_processed_csv(file_name: str, processed_data_dir: Path = PROCESSED_DATA_DIR) -> pd.DataFrame:
    """
    Load one processed CSV file.
    """
    file_path = processed_data_dir / file_name
    return pd.read_csv(file_path)


def create_sqlite_database() -> None:
    """
    Create SQLite database and load processed CSV files into database tables.
    """
    DATABASE_DIR.mkdir(parents=True, exist_ok=True)

    validate_processed_files()

    with sqlite3.connect(SQLITE_DB_PATH) as connection:
        for file_name, table_name in PROCESSED_TABLES.items():
            df = load_processed_csv(file_name)

            df.to_sql(
                name=table_name,
                con=connection,
                if_exists="replace",
                index=False,
            )

            print(f"Loaded {file_name} into table: {table_name}")

    print("SQLite database created successfully.")
    print(f"Database saved to: {SQLITE_DB_PATH}")


def create_database_table_summary() -> pd.DataFrame:
    """
    Create a summary of all tables inside the SQLite database.
    """
    table_summary = []

    with sqlite3.connect(SQLITE_DB_PATH) as connection:
        tables_query = """
        SELECT name
        FROM sqlite_master
        WHERE type = 'table'
        ORDER BY name;
        """

        tables = pd.read_sql_query(tables_query, connection)

        for table_name in tables["name"]:
            count_query = f"SELECT COUNT(*) AS row_count FROM {table_name};"
            row_count = pd.read_sql_query(count_query, connection)["row_count"].iloc[0]

            table_summary.append(
                {
                    "table_name": table_name,
                    "row_count": row_count,
                }
            )

    return pd.DataFrame(table_summary)


def save_database_table_summary() -> None:
    """
    Save database table summary to outputs folder.
    """
    OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)

    table_summary = create_database_table_summary()
    table_summary.to_csv(OUTPUTS_DIR / "database_table_summary.csv", index=False)

    print("Database table summary saved successfully.")
    print(f"Saved to: {OUTPUTS_DIR / 'database_table_summary.csv'}")


def main() -> None:
    """
    Run the full database loading process.
    """
    create_sqlite_database()
    save_database_table_summary()


if __name__ == "__main__":
    main()