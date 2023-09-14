SELECT continent_name,
TRIM(BOTH ' ' FROM continent_name) AS "trim"
FROM continents;
