-- Get information about the hiking routes and their leaders using the 'campers' table
SELECT
    r.start_point,
    r.end_point,
    r.leader_id,
    CONCAT(c.first_name, ' ', c.last_name) AS leader_name
FROM
    routes r
INNER JOIN
    campers c ON r.leader_id = c.id;
