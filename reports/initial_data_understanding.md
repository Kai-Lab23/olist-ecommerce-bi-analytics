# Initial Data Understanding

## Project

Olist E-Commerce BI Analytics

## Dataset Overview

- Total tables loaded: 9
- Total raw rows across all tables: 1,550,922
- Largest table: olist_geolocation_dataset
- Largest table row count: 1,000,163

## Main Tables

The main analytical tables are:

- `olist_orders_dataset`
- `olist_order_items_dataset`
- `olist_order_payments_dataset`
- `olist_order_reviews_dataset`
- `olist_customers_dataset`
- `olist_products_dataset`
- `olist_sellers_dataset`
- `product_category_name_translation`

## Initial Notes

- `olist_orders_dataset` will be the main transaction table.
- `olist_order_items_dataset` will be used to calculate revenue from product price and freight value.
- `olist_customers_dataset` will support customer location analysis.
- `olist_products_dataset` and `product_category_name_translation` will support product category analysis.
- `olist_order_reviews_dataset` will support customer satisfaction analysis.
- `olist_order_payments_dataset` will support payment behavior analysis.

## Next Step

The next step is to clean and transform raw data before loading it into SQLite.
