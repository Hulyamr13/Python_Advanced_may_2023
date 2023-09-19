SELECT
    name AS "Name",
    country AS "Country",
    DATE(bookings.booked_at) AS "Booked at"
FROM
    apartments
LEFT JOIN
    bookings ON bookings.booking_id = apartments.booking_id
LIMIT 10;
