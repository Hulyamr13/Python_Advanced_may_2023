SELECT bookings.booking_id AS Booking_ID, customers.first_name AS Customer_Name
FROM bookings
CROSS JOIN customers
ORDER BY Customer_Name;
