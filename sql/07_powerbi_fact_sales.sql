WITH delivered_orders AS (
    SELECT *
    FROM orders
    WHERE order_status = 'delivered'
),

payment_summary AS (
    SELECT
        order_id,
        GROUP_CONCAT(DISTINCT payment_type) AS payment_types,
        SUM(payment_value) AS total_payment_value,
        AVG(payment_installments) AS average_installments
    FROM order_payments
    GROUP BY order_id
),

review_summary AS (
    SELECT
        order_id,
        AVG(review_score) AS average_review_score,
        MAX(has_review_comment) AS has_review_comment
    FROM order_reviews
    GROUP BY order_id
)

SELECT
    oi.order_id,
    oi.order_item_id,
    o.customer_id,
    oi.product_id,
    oi.seller_id,

    DATE(o.order_purchase_timestamp) AS order_date,
    o.order_purchase_year,
    o.order_purchase_month,
    o.order_purchase_year_month,

    oi.price AS product_revenue,
    oi.freight_value,
    oi.total_item_value,

    o.delivery_days,
    o.estimated_delivery_days,
    o.delivery_delay_days,

    CASE
        WHEN o.is_late_delivery = 1
             OR LOWER(CAST(o.is_late_delivery AS TEXT)) = 'true'
        THEN 1
        ELSE 0
    END AS is_late_delivery,

    ps.payment_types,
    ps.total_payment_value,
    ps.average_installments,

    rs.average_review_score,
    rs.has_review_comment

FROM order_items oi
INNER JOIN delivered_orders o
    ON oi.order_id = o.order_id
LEFT JOIN payment_summary ps
    ON oi.order_id = ps.order_id
LEFT JOIN review_summary rs
    ON oi.order_id = rs.order_id;