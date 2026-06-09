WITH delivered_orders AS (
    SELECT *
    FROM orders
    WHERE order_status = 'delivered'
),

order_revenue AS (
    SELECT
        order_id,
        SUM(price) AS product_revenue,
        SUM(freight_value) AS freight_value,
        SUM(total_item_value) AS total_order_value
    FROM order_items
    GROUP BY order_id
)

SELECT
    o.order_purchase_year_month,
    o.order_purchase_year,
    o.order_purchase_month,
    COUNT(DISTINCT o.order_id) AS total_orders,
    COUNT(DISTINCT c.customer_unique_id) AS total_unique_customers,
    ROUND(SUM(r.product_revenue), 2) AS total_product_revenue,
    ROUND(SUM(r.freight_value), 2) AS total_freight_value,
    ROUND(SUM(r.total_order_value), 2) AS total_sales_value,
    ROUND(SUM(r.product_revenue) / COUNT(DISTINCT o.order_id), 2) AS average_order_value
FROM delivered_orders o
LEFT JOIN order_revenue r
    ON o.order_id = r.order_id
LEFT JOIN customers c
    ON o.customer_id = c.customer_id
GROUP BY
    o.order_purchase_year_month,
    o.order_purchase_year,
    o.order_purchase_month
ORDER BY
    o.order_purchase_year,
    o.order_purchase_month;