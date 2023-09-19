SELECT mc.country_code, m.mountain_range, p.peak_name, p.elevation
FROM mountains_countries mc
INNER JOIN mountains m ON mc.mountain_id = m.id
INNER JOIN peaks p ON mc.mountain_id = p.mountain_id
WHERE p.elevation > 2835 AND mc.country_code = 'BG'
ORDER BY p.elevation DESC;
