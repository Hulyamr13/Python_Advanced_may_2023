WITH row_number AS (
  SELECT
    c.country_name,
    p.peak_name,
    p.elevation,
    m.mountain_range,
    ROW_NUMBER() OVER (
        PARTITION BY c.country_name
        ORDER BY p.elevation DESC
    ) AS peak_rank
  FROM countries c
    LEFT JOIN mountains_countries mc ON c.country_code = mc.country_code
    LEFT JOIN mountains m ON mc.mountain_id = m.id
    LEFT JOIN peaks p ON m.id = p.mountain_id
)
SELECT
    country_name,
    COALESCE(peak_name, '(no highest peak)') AS "Highest Peak Name",
    COALESCE(elevation, 0) AS "Highest Peak Elevation",
    CASE
        WHEN peak_name IS NULL OR mountain_range IS NULL THEN '(no mountain)'
        ELSE mountain_range
    END AS "Mountain"
FROM row_number
WHERE peak_rank = 1
ORDER BY country_name ASC, elevation DESC;
