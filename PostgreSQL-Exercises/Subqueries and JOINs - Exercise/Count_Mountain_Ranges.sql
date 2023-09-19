
SELECT country_code, COUNT(country_code) AS mountain_range_count
FROM mountains_countries
WHERE country_code IN ('US', 'RU', 'BG')
GROUP BY country_code
ORDER BY mountain_range_count DESC;
