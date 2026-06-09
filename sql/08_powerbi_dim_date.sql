SELECT DISTINCT
    DATE(order_purchase_timestamp) AS order_date,
    CAST(STRFTIME('%Y', order_purchase_timestamp) AS INTEGER) AS year,
    CAST(STRFTIME('%m', order_purchase_timestamp) AS INTEGER) AS month_number,

    CASE STRFTIME('%m', order_purchase_timestamp)
        WHEN '01' THEN 'January'
        WHEN '02' THEN 'February'
        WHEN '03' THEN 'March'
        WHEN '04' THEN 'April'
        WHEN '05' THEN 'May'
        WHEN '06' THEN 'June'
        WHEN '07' THEN 'July'
        WHEN '08' THEN 'August'
        WHEN '09' THEN 'September'
        WHEN '10' THEN 'October'
        WHEN '11' THEN 'November'
        WHEN '12' THEN 'December'
    END AS month_name,

    'Q' || CAST(
        ((CAST(STRFTIME('%m', order_purchase_timestamp) AS INTEGER) - 1) / 3 + 1)
        AS INTEGER
    ) AS quarter,

    STRFTIME('%Y-%m', order_purchase_timestamp) AS year_month

FROM orders
WHERE order_purchase_timestamp IS NOT NULL
ORDER BY order_date;