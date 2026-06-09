-- Check all main table row counts

SELECT 'orders' AS table_name, COUNT(*) AS row_count FROM orders
UNION ALL
SELECT 'order_items' AS table_name, COUNT(*) AS row_count FROM order_items
UNION ALL
SELECT 'order_payments' AS table_name, COUNT(*) AS row_count FROM order_payments
UNION ALL
SELECT 'order_reviews' AS table_name, COUNT(*) AS row_count FROM order_reviews
UNION ALL
SELECT 'customers' AS table_name, COUNT(*) AS row_count FROM customers
UNION ALL
SELECT 'products' AS table_name, COUNT(*) AS row_count FROM products
UNION ALL
SELECT 'sellers' AS table_name, COUNT(*) AS row_count FROM sellers
UNION ALL
SELECT 'product_category_translation' AS table_name, COUNT(*) AS row_count FROM product_category_translation;