import pandas as pd

from src.config import PROCESSED_DATA_DIR
from src.data_loader import load_all_raw_data


def clean_orders(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean orders dataset and create date-based business columns.
    """
    orders = df.copy()

    date_columns = [
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date",
        "order_estimated_delivery_date",
    ]

    for column in date_columns:
        orders[column] = pd.to_datetime(orders[column], errors="coerce")

    orders = orders.drop_duplicates()

    orders["order_purchase_date"] = orders["order_purchase_timestamp"].dt.date
    orders["order_purchase_year"] = orders["order_purchase_timestamp"].dt.year
    orders["order_purchase_month"] = orders["order_purchase_timestamp"].dt.month
    orders["order_purchase_year_month"] = orders["order_purchase_timestamp"].dt.to_period("M").astype(str)

    orders["delivery_days"] = (
        orders["order_delivered_customer_date"] - orders["order_purchase_timestamp"]
    ).dt.days

    orders["estimated_delivery_days"] = (
        orders["order_estimated_delivery_date"] - orders["order_purchase_timestamp"]
    ).dt.days

    orders["delivery_delay_days"] = (
        orders["order_delivered_customer_date"] - orders["order_estimated_delivery_date"]
    ).dt.days

    orders["is_late_delivery"] = orders["delivery_delay_days"].apply(
        lambda value: True if pd.notna(value) and value > 0 else False
    )

    return orders


def clean_order_items(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean order items dataset and create item-level revenue columns.
    """
    order_items = df.copy()

    order_items["shipping_limit_date"] = pd.to_datetime(
        order_items["shipping_limit_date"],
        errors="coerce"
    )

    order_items = order_items.drop_duplicates()

    order_items["price"] = pd.to_numeric(order_items["price"], errors="coerce")
    order_items["freight_value"] = pd.to_numeric(order_items["freight_value"], errors="coerce")

    order_items["total_item_value"] = order_items["price"] + order_items["freight_value"]

    return order_items


def clean_order_payments(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean order payments dataset.
    """
    payments = df.copy()

    payments = payments.drop_duplicates()

    payments["payment_sequential"] = pd.to_numeric(
        payments["payment_sequential"],
        errors="coerce"
    )

    payments["payment_installments"] = pd.to_numeric(
        payments["payment_installments"],
        errors="coerce"
    )

    payments["payment_value"] = pd.to_numeric(
        payments["payment_value"],
        errors="coerce"
    )

    payments["payment_type"] = payments["payment_type"].str.strip().str.lower()

    return payments


def clean_order_reviews(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean order reviews dataset.
    """
    reviews = df.copy()

    reviews["review_creation_date"] = pd.to_datetime(
        reviews["review_creation_date"],
        errors="coerce"
    )

    reviews["review_answer_timestamp"] = pd.to_datetime(
        reviews["review_answer_timestamp"],
        errors="coerce"
    )

    reviews = reviews.drop_duplicates()

    reviews["review_score"] = pd.to_numeric(
        reviews["review_score"],
        errors="coerce"
    )

    reviews["has_review_comment"] = reviews["review_comment_message"].notna()

    return reviews


def clean_customers(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean customers dataset.
    """
    customers = df.copy()

    customers = customers.drop_duplicates()

    customers["customer_city"] = customers["customer_city"].str.strip().str.lower()
    customers["customer_state"] = customers["customer_state"].str.strip().str.upper()

    return customers


def clean_sellers(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean sellers dataset.
    """
    sellers = df.copy()

    sellers = sellers.drop_duplicates()

    sellers["seller_city"] = sellers["seller_city"].str.strip().str.lower()
    sellers["seller_state"] = sellers["seller_state"].str.strip().str.upper()

    return sellers


def clean_product_category_translation(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean product category translation dataset.
    """
    category_translation = df.copy()

    category_translation = category_translation.drop_duplicates()

    category_translation["product_category_name"] = (
        category_translation["product_category_name"]
        .str.strip()
        .str.lower()
    )

    category_translation["product_category_name_english"] = (
        category_translation["product_category_name_english"]
        .str.strip()
        .str.lower()
    )

    return category_translation


def clean_products(
    products_df: pd.DataFrame,
    category_translation_df: pd.DataFrame
) -> pd.DataFrame:
    """
    Clean products dataset and add English product category names.
    """
    products = products_df.copy()

    products = products.drop_duplicates()

    products["product_category_name"] = (
        products["product_category_name"]
        .str.strip()
        .str.lower()
    )

    products = products.merge(
        category_translation_df,
        on="product_category_name",
        how="left"
    )

    products["product_category_name_english"] = products[
        "product_category_name_english"
    ].fillna("unknown")

    numeric_columns = [
        "product_name_lenght",
        "product_description_lenght",
        "product_photos_qty",
        "product_weight_g",
        "product_length_cm",
        "product_height_cm",
        "product_width_cm",
    ]

    for column in numeric_columns:
        products[column] = pd.to_numeric(products[column], errors="coerce")

    return products


def save_cleaned_data() -> None:
    """
    Load raw datasets, clean them, and save cleaned datasets to processed folder.
    """
    PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)

    dataframes = load_all_raw_data()

    cleaned_category_translation = clean_product_category_translation(
        dataframes["product_category_name_translation"]
    )

    cleaned_orders = clean_orders(dataframes["olist_orders_dataset"])
    cleaned_order_items = clean_order_items(dataframes["olist_order_items_dataset"])
    cleaned_order_payments = clean_order_payments(dataframes["olist_order_payments_dataset"])
    cleaned_order_reviews = clean_order_reviews(dataframes["olist_order_reviews_dataset"])
    cleaned_customers = clean_customers(dataframes["olist_customers_dataset"])
    cleaned_sellers = clean_sellers(dataframes["olist_sellers_dataset"])
    cleaned_products = clean_products(
        dataframes["olist_products_dataset"],
        cleaned_category_translation
    )

    cleaned_orders.to_csv(PROCESSED_DATA_DIR / "cleaned_orders.csv", index=False)
    cleaned_order_items.to_csv(PROCESSED_DATA_DIR / "cleaned_order_items.csv", index=False)
    cleaned_order_payments.to_csv(PROCESSED_DATA_DIR / "cleaned_order_payments.csv", index=False)
    cleaned_order_reviews.to_csv(PROCESSED_DATA_DIR / "cleaned_order_reviews.csv", index=False)
    cleaned_customers.to_csv(PROCESSED_DATA_DIR / "cleaned_customers.csv", index=False)
    cleaned_sellers.to_csv(PROCESSED_DATA_DIR / "cleaned_sellers.csv", index=False)
    cleaned_products.to_csv(PROCESSED_DATA_DIR / "cleaned_products.csv", index=False)
    cleaned_category_translation.to_csv(
        PROCESSED_DATA_DIR / "cleaned_product_category_translation.csv",
        index=False
    )

    print("Cleaned datasets saved successfully.")
    print(f"Saved to: {PROCESSED_DATA_DIR}")


if __name__ == "__main__":
    save_cleaned_data()