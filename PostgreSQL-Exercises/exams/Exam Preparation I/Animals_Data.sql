SELECT
    a.name AS name,
    at.animal_type AS animal_type,
    TO_CHAR(a.birthdate, 'DD.MM.YYYY') AS birthdate
FROM
    animals AS a
INNER JOIN
    animal_types AS at
ON
    a.animal_type_id = at.id
ORDER BY
    a.name ASC;