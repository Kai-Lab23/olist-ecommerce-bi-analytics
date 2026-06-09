WITH delivered_orders AS (
    SELECT order_id
    FROM orders
    WHERE order_status = 'delivered'
)

SELECT
    COALESCE(p.product_category_name_english, 'unknown') AS product_category,
    COUNT(DISTINCT oi.order_id) AS total_orders,
    COUNT(oi.order_item_id) AS total_items_sold,
    ROUND(SUM(oi.price), 2) AS total_product_revenue,
    ROUND(SUM(oi.freight_value), 2) AS total_freight_value,
    ROUND(SUM(oi.total_item_value), 2) AS total_sales_value,
    ROUND(AVG(oi.price), 2) AS average_item_price,
    ROUND(AVG(oi.freight_value), 2) AS average_freight_value
FROM order_items oi
INNER JOIN delivered_orders o
    ON oi.order_id = o.order_id
LEFT JOIN products p
    ON oi.product_id = p.product_id
GROUP BY
    COALESCE(p.product_category_name_english, 'unknown')
ORDER BY
    total_product_revenue DESC;