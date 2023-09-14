CREATE TABLE bookings_calculation (
    booked_for INTEGER,
    multiplication NUMERIC,
    modulo NUMERIC
);

INSERT INTO bookings_calculation (booked_for, multiplication, modulo)
SELECT
    booked_for,
    booked_for * 50 AS multiplication,
    booked_for % 50 AS modulo
FROM bookings
WHERE apartment_id = 93;