SELECT
    CONCAT(mountain_range, ' ', peak_name) AS "Mountain Information",
    LENGTH(CONCAT(mountain_range, ' ', peak_name)) AS "Characters Length",
    LENGTH(CONVERT_TO(CONCAT(mountain_range, ' ', peak_name), 'UTF8')) * 8 AS "Bits of a String"
FROM mountains
JOIN peaks ON mountains.id = peaks.mountain_id;
