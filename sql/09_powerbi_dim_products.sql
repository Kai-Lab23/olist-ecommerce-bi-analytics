SELECT
    product_id,
    COALESCE(product_category_name_english, 'unknown') AS product_category,
    product_weight_g,
    product_length_cm,
    product_height_cm,
    product_width_cm,

    product_length_cm * product_height_cm * product_width_cm AS product_volume_cm3,

    product_name_lenght,
    product_description_lenght,
    product_photos_qty

FROM products;