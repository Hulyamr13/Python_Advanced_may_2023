WITH BookingsApartments AS (
    SELECT
        bookings.booking_id AS "Booking ID",
        apartments.name AS "Apartment Owner",
        apartments.apartment_id AS "Apartment ID",
        bookings.customer_id
    FROM
        bookings
    FULL JOIN
        apartments ON bookings.booking_id = apartments.booking_id
),
BookingsCustomers AS (
    SELECT
        customers.customer_id,
        CONCAT(customers.first_name, ' ', customers.last_name) AS "Customer Name"
    FROM
        customers
)
SELECT
    BA."Booking ID",
    BA."Apartment Owner",
    BA."Apartment ID",
    BC."Customer Name"
FROM
    BookingsApartments BA
FULL JOIN
    BookingsCustomers BC ON BA.customer_id = BC.customer_id
ORDER BY
    "Booking ID", "Apartment Owner", "Customer Name";
