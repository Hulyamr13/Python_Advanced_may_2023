SELECT
    c.full_name,
    COUNT(DISTINCT co.car_id) AS count_of_cars,
    ROUND(SUM(co.bill)::NUMERIC, 2) AS total_sum
FROM
    clients AS c
JOIN
    courses AS co
    ON c.id = co.client_id
WHERE
    SUBSTRING(c.full_name, 2, 1) = 'a'
GROUP BY
    c.full_name
HAVING
    COUNT(DISTINCT co.car_id) > 1
ORDER BY
    c.full_name;