UPDATE countries
SET country_name = 'Burma'
WHERE country_name = 'Myanmar';

INSERT INTO monasteries (monastery_name, country_code)
VALUES
    ('Hanga Abbey', (SELECT country_code FROM countries WHERE country_name = 'Tanzania')),
    ('Myin-Tin-Daik', (SELECT country_code FROM countries WHERE country_name = 'Myanmar'));

SELECT
    con.continent_name AS "Continent Name",
    coun.country_name AS "Country Name",
    COUNT(mon.country_code) AS "Monasteries Count"
FROM monasteries AS mon
RIGHT JOIN countries coun USING (country_code)
JOIN continents con USING (continent_code)
WHERE three_rivers = false
GROUP BY coun.country_name, con.continent_name
ORDER BY "Monasteries Count" DESC, coun.country_name;