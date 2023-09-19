SELECT
    addresses.town_id,
    towns.name AS town_name,
    addresses.address_text
FROM
    addresses
INNER JOIN
    towns ON addresses.town_id = towns.town_id
WHERE
    towns.name = 'San Francisco'
    OR towns.name = 'Sofia'
    OR towns.name = 'Carnation'
ORDER BY
    addresses.town_id,
    addresses.address_id;
