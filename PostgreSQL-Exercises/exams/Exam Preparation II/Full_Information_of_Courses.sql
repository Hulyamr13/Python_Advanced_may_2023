SELECT
    a.name AS address,
    CASE
        WHEN EXTRACT(HOUR FROM c.start) BETWEEN 6 AND 20 THEN 'Day'
        ELSE 'Night'
    END AS day_time,
    c.bill,
    cl.full_name AS full_name,
    ca.make,
    ca.model,
    cat.name AS category_name
FROM
    courses AS c
JOIN
    addresses AS a
    ON c.from_address_id = a.id
JOIN
    clients AS cl
    ON c.client_id = cl.id
JOIN
    cars AS ca
    ON c.car_id = ca.id
JOIN
    categories AS cat
    ON ca.category_id = cat.id
ORDER BY
    c.id;