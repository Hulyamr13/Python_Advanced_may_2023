SELECT
    a.name AS "Animal Name",
    EXTRACT(YEAR FROM a.birthdate) AS "Birth Year",
    at.animal_type AS "Animal Type"
FROM
    animals AS a
INNER JOIN
    animal_types AS at
ON
    a.animal_type_id = at.id
LEFT JOIN
    owners AS o
ON
    a.owner_id = o.id
WHERE
    a.birthdate >= '2017-01-01' -- Animals younger than 5 years as of '01/01/2022'
    AND at.animal_type != 'Birds' -- Exclude Birds
    AND o.id IS NULL -- Animals that are not owned
ORDER BY
    "Animal Name" ASC;