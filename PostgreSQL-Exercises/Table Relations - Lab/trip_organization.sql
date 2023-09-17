SELECT
    vehicles.driver_id,
    vehicles.vehicle_type,
    CONCAT(campers.first_name, ' ', campers.last_name) AS driver_name
FROM
    vehicles
INNER JOIN
    campers ON campers.id = vehicles.driver_id;
