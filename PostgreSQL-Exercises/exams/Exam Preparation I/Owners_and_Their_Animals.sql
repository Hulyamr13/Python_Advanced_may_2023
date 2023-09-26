WITH OwnerAnimalCounts AS (
    SELECT
        o.name AS Owner,
        COUNT(a.id) AS "Count of animals"
    FROM
        owners AS o
    LEFT JOIN
        animals AS a
    ON
        o.id = a.owner_id
    GROUP BY
        o.name
)
SELECT
    Owner,
    "Count of animals"
FROM
    OwnerAnimalCounts
ORDER BY
    "Count of animals" DESC,
    Owner ASC
LIMIT 5;