CREATE VIEW with_rivers AS
SELECT
    countries.country_code,
    COUNT(countries_rivers.river_id) AS river_count
FROM
    countries_rivers
INNER JOIN
    countries ON countries.country_code = countries_rivers.country_code
GROUP BY
    countries.country_code;

SELECT
    (SELECT COUNT(country_code) FROM countries) - COUNT(river_count) AS countries_without_rivers
FROM
    with_rivers;
