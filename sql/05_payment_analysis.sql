WITH delivered_orders AS (
    SELECT order_id
    FROM orders
    WHERE order_status = 'delivered'
)

SELECT
    p.payment_type,
    COUNT(DISTINCT p.order_id) AS total_orders,
    COUNT(*) AS total_payment_records,
    ROUND(SUM(p.payment_value), 2) AS total_payment_value,
    ROUND(AVG(p.payment_value), 2) AS average_payment_value,
    ROUND(AVG(p.payment_installments), 2) AS average_installments
FROM order_payments p
INNER JOIN delivered_orders o
    ON p.order_id = o.order_id
GROUP BY
    p.payment_type
ORDER BY
    total_payment_value DESC;