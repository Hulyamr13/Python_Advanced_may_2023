SELECT
    booking_id AS "Booking ID",
    DATE(starts_at) AS "Start Date",
    apartment_id AS "Apartment ID",
    CONCAT(customers.first_name, ' ', customers.last_name) AS "Customer Name"
FROM
    bookings
RIGHT JOIN
    customers ON bookings.customer_id = customers.customer_id
ORDER BY
    "Customer Name"
LIMIT 10;
