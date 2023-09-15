CREATE VIEW view_continents_countries_currencies_details AS
SELECT
    c.continent_name || ': ' || c.continent_code AS "Continent Details",
    co.country_name || ' - ' || co.capital || ' - ' || co.area_in_sq_km || ' - km2' AS "Country Information",
    curr.description || ' (' || curr.currency_code || ')' AS "Currencies"
FROM continents c
JOIN countries co ON c.continent_code = co.continent_code
JOIN currencies curr ON co.currency_code = curr.currency_code
ORDER BY "Country Information" ASC, "Currencies" ASC;