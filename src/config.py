from pathlib import Path

# Project root directory
ROOT_DIR = Path(__file__).resolve().parents[1]

# Data directories
DATA_DIR = ROOT_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

# Database directory
DATABASE_DIR = ROOT_DIR / "database"
SQLITE_DB_PATH = DATABASE_DIR / "olist_ecommerce.db"

# SQL directory
SQL_DIR = ROOT_DIR / "sql"

# Output directory
OUTPUTS_DIR = ROOT_DIR / "outputs"
SQL_OUTPUTS_DIR = OUTPUTS_DIR / "sql_results"
POWERBI_OUTPUTS_DIR = OUTPUTS_DIR / "powerbi_data"

# Expected raw CSV files from Olist dataset
EXPECTED_RAW_FILES = [
    "olist_customers_dataset.csv",
    "olist_geolocation_dataset.csv",
    "olist_order_items_dataset.csv",
    "olist_order_payments_dataset.csv",
    "olist_order_reviews_dataset.csv",
    "olist_orders_dataset.csv",
    "olist_products_dataset.csv",
    "olist_sellers_dataset.csv",
    "product_category_name_translation.csv",
]