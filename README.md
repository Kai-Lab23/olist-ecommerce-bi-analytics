# Olist E-Commerce BI Analytics

## Project Overview

This project is an end-to-end Business Intelligence analytics project using the Brazilian E-Commerce Public Dataset by Olist.

The goal of this project is to analyze e-commerce sales performance, customer behavior, product category performance, seller performance, delivery performance, and customer satisfaction using Python, SQL, SQLite, and Power BI.

This project was built as a portfolio project for Data Analyst / BI Analyst roles.

---

## Business Objectives

This project aims to answer the following business questions:

1. What are the overall sales, order, customer, and delivery performance?
2. How does revenue change over time?
3. Which product categories generate the highest revenue?
4. Which customer locations contribute the most to revenue?
5. Which seller locations contribute the most to revenue?
6. How does delivery performance affect customer review score?
7. Which product and seller segments should be prioritized?

---

## Tools Used

* Python
* Pandas
* SQLite
* SQL
* Power BI
* Jupyter Notebook
* Git / GitHub

---

## Project Workflow

```text
Raw CSV Files
      ↓
Data Quality Check
      ↓
Data Cleaning & Transformation
      ↓
SQLite Database Creation
      ↓
SQL Business Analysis
      ↓
Power BI Analytical Tables
      ↓
Power BI Dashboard
      ↓
Business Case Study Report
```

---

## Project Structure

```text
olist-ecommerce-bi-analytics/
├── data/
│   ├── raw/
│   ├── processed/
│   └── README.md
├── database/
├── notebooks/
├── sql/
├── src/
├── dashboard/
├── reports/
├── outputs/
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Dataset

Dataset used:

**Brazilian E-Commerce Public Dataset by Olist from Kaggle**

The dataset contains multiple relational tables, including:

* Orders
* Order items
* Payments
* Reviews
* Customers
* Products
* Sellers
* Product category translation
* Geolocation

Raw data is not uploaded to this repository due to file size and reproducibility reasons.

To reproduce this project, download the dataset from Kaggle and place all CSV files inside:

```text
data/raw/
```

---

## Main Tables Used

| Table            | Description                             |
| ---------------- | --------------------------------------- |
| `orders`         | Order status and order timeline         |
| `order_items`    | Product-level transaction data          |
| `order_payments` | Payment method and payment value        |
| `order_reviews`  | Customer review score and comments      |
| `customers`      | Customer location data                  |
| `products`       | Product category and product attributes |
| `sellers`        | Seller location data                    |

---

## Data Processing Steps

### 1. Data Loading

Raw CSV files were loaded using Python and Pandas.

Main script:

```text
src/data_loader.py
```

---

### 2. Data Quality Check

Initial data quality checks included:

* Row count
* Column count
* Missing values
* Duplicate rows
* Primary key checks
* Relationship checks

Main script:

```text
src/data_quality_check.py
```

Outputs:

```text
outputs/raw_tables_summary.csv
outputs/missing_values_summary.csv
outputs/duplicate_rows_summary.csv
outputs/table_columns_summary.csv
outputs/key_relationship_checks.csv
```

---

### 3. Data Cleaning

Cleaning steps included:

* Converting date columns to datetime format
* Removing exact duplicate rows
* Standardizing city and state values
* Creating delivery performance columns
* Creating item-level revenue columns
* Adding English product category names

Main script:

```text
src/data_cleaning.py
```

Important generated columns:

| Column                          | Description                                            |
| ------------------------------- | ------------------------------------------------------ |
| `delivery_days`                 | Days between purchase date and customer delivery date  |
| `estimated_delivery_days`       | Days between purchase date and estimated delivery date |
| `delivery_delay_days`           | Difference between actual and estimated delivery date  |
| `is_late_delivery`              | Flag for late delivery                                 |
| `total_item_value`              | Product price plus freight value                       |
| `product_category_name_english` | Product category translated into English               |

---

### 4. SQLite Database Creation

Cleaned datasets were loaded into a SQLite database.

Main script:

```text
src/database_loader.py
```

Database output:

```text
database/olist_ecommerce.db
```

---

### 5. SQL Business Analysis

SQL queries were created to analyze:

* KPI overview
* Monthly revenue trend
* Product category performance
* Customer location performance
* Payment analysis
* Delivery and review analysis

SQL files:

```text
sql/01_kpi_overview.sql
sql/02_monthly_revenue_trend.sql
sql/03_product_category_performance.sql
sql/04_customer_location_analysis.sql
sql/05_payment_analysis.sql
sql/06_delivery_review_analysis.sql
```

---

### 6. Power BI Analytical Tables

Power BI-ready fact and dimension tables were created from SQLite using SQL.

Tables exported:

```text
fact_sales.csv
dim_date.csv
dim_products.csv
dim_customers.csv
dim_sellers.csv
```

Main script:

```text
src/powerbi_data_exporter.py
```

---

## Power BI Data Model

The dashboard uses a star schema model.

```text
             dim_date
                |
dim_products — fact_sales — dim_customers
                |
            dim_sellers
```

Relationships:

| Dimension Table              | Fact Table                |
| ---------------------------- | ------------------------- |
| `dim_date[order_date]`       | `fact_sales[order_date]`  |
| `dim_products[product_id]`   | `fact_sales[product_id]`  |
| `dim_customers[customer_id]` | `fact_sales[customer_id]` |
| `dim_sellers[seller_id]`     | `fact_sales[seller_id]`   |

---

## Key Metrics

| Metric                | Description                                                  |
| --------------------- | ------------------------------------------------------------ |
| Total Product Revenue | Total product sales revenue excluding freight                |
| Total Freight Value   | Total freight or shipping value                              |
| Total Sales Value     | Product revenue plus freight value                           |
| Total Orders          | Number of unique delivered orders                            |
| Total Customers       | Number of unique customers                                   |
| Total Sellers         | Number of unique sellers                                     |
| Total Items Sold      | Total number of sold order items                             |
| Average Order Value   | Product revenue divided by total orders                      |
| Average Delivery Days | Average number of days from purchase to delivery             |
| Late Delivery Rate    | Percentage of orders delivered after estimated delivery date |
| Positive Review Rate  | Percentage of orders with review score 4 or 5                |
| Average Review Score  | Average customer review score                                |

---

## Dashboard Pages

### 1. Executive Overview

This page shows high-level business performance, including revenue, orders, customers, average order value, delivery days, and review score.

![Executive Overview](reports/Page1 - Executive Overview.png)

---

### 2. Product & Seller Analysis

This page analyzes product category performance, item sales, seller performance, freight contribution, top seller state, top seller, highest AOV category, and highest items sold category.

![Product and Seller Analysis](reports/Page2 - Product & Seller Analysis.png)

---

### 3. Delivery & Review Analysis

This page analyzes delivery performance, late delivery rate, positive review rate, review score distribution, and the relationship between delivery performance and customer review score.

![Delivery and Review Analysis](reports/Page3 - Delivery & Review Analysis.png)

---

### 4. About This Dashboard

This page explains the dashboard purpose, data source, main metrics, and the value of the analysis.

![About This Dashboard](reports/About Dashboard.png)

---

## Key Dashboard Insights

The dashboard is designed to help stakeholders identify:

1. Revenue trends over time.
2. Top-performing product categories.
3. Customer states with the highest revenue contribution.
4. Seller states and sellers with the highest revenue contribution.
5. Product categories with high revenue and item sales.
6. Delivery performance issues by state.
7. Relationship between delivery performance and customer satisfaction.
8. Review score distribution across delivered orders.

---

## Business Recommendations

Based on the BI analysis framework, the business could take the following actions:

1. Prioritize high-revenue product categories for marketing and inventory planning.
2. Monitor states or cities with high order volume but poor delivery performance.
3. Improve logistics performance in regions with high late delivery rates.
4. Analyze product categories with high freight costs to optimize shipping strategy.
5. Use review score trends to identify customer satisfaction issues.
6. Track monthly revenue trends to support business planning and forecasting.
7. Evaluate top seller states and top sellers for partnership or operational improvement.

---

## How to Run This Project

### 1. Clone the repository

```bash
git clone https://github.com/Kai-Lab23/olist-ecommerce-bi-analytics.git
cd olist-ecommerce-bi-analytics
```

---

### 2. Create virtual environment

For Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

For Mac/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Download dataset

Download the Brazilian E-Commerce Public Dataset by Olist from Kaggle and place all CSV files inside:

```text
data/raw/
```

---

### 5. Run data quality check

```bash
python -m src.data_quality_check
```

---

### 6. Run data cleaning

```bash
python -m src.data_cleaning
```

---

### 7. Create SQLite database

```bash
python -m src.database_loader
```

---

### 8. Export SQL analysis results

```bash
python -m src.sql_runner
```

---

### 9. Export Power BI-ready datasets

```bash
python -m src.powerbi_data_exporter
```

---

### 10. Open Power BI dashboard

Open the Power BI file from:

```text
dashboard/olist_ecommerce_bi_dashboard.pbix
```

---

## Project Outputs

| Output                  | Location                       |
| ----------------------- | ------------------------------ |
| Data quality reports    | `outputs/`                     |
| Cleaned datasets        | `data/processed/`              |
| SQLite database         | `database/`                    |
| SQL query results       | `outputs/sql_results/`         |
| Power BI-ready datasets | `outputs/powerbi_data/`        |
| Dashboard screenshots   | `reports/`                     |
| Case study report       | `reports/case_study_report.md` |

---

## Key Skills Demonstrated

* Data loading with Python
* Data quality checking
* Data cleaning and transformation
* Relational database creation with SQLite
* SQL business analysis
* BI data modeling
* Star schema design
* Power BI dashboard development
* DAX measure creation
* Business insight communication
* Portfolio project documentation

---

## Notes

The raw dataset, processed datasets, SQLite database, output files, and Power BI file are not uploaded to GitHub due to file size and reproducibility reasons.

The repository provides source code, SQL scripts, documentation, and dashboard screenshots.

If the dashboard file is not included in this repository, the dashboard preview can still be reviewed through the screenshots in the `reports/` folder.

---

## Author

**Khairu Ikramendra**
Data Analyst / BI Analyst Portfolio Project
