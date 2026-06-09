WITH delivered_orders AS (
    SELECT *
    FROM orders
    WHERE order_status = 'delivered'
)

SELECT
    CASE
        WHEN o.is_late_delivery = 1
             OR LOWER(CAST(o.is_late_delivery AS TEXT)) = 'true'
        THEN 'Late Delivery'
        ELSE 'On-Time Delivery'
    END AS delivery_status_group,
    COUNT(DISTINCT o.order_id) AS total_orders,
    ROUND(AVG(o.delivery_days), 2) AS average_delivery_days,
    ROUND(AVG(o.delivery_delay_days), 2) AS average_delivery_delay_days,
    ROUND(AVG(r.review_score), 2) AS average_review_score,
    COUNT(DISTINCT r.review_id) AS total_reviews,
    ROUND(
        AVG(
            CASE
                WHEN r.review_score >= 4 THEN 1.0
                ELSE 0.0
            END
        ) * 100,
        2
    ) AS positive_review_percentage
FROM delivered_orders o
LEFT JOIN order_reviews r
    ON o.order_id = r.order_id
GROUP BY
    CASE
        WHEN o.is_late_delivery = 1
             OR LOWER(CAST(o.is_late_delivery AS TEXT)) = 'true'
        THEN 'Late Delivery'
        ELSE 'On-Time Delivery'
    END
ORDER BY
    total_orders DESC;