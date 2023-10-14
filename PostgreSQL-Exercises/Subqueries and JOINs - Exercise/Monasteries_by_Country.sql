-- Create the "monasteries" table
CREATE TABLE monasteries (
    id SERIAL PRIMARY KEY,
    monastery_name VARCHAR(255),
    country_code CHAR(2)
);

-- Insert data into the "monasteries" table
INSERT INTO monasteries (monastery_name, country_code)
VALUES
    ('Rila Monastery "St. Ivan of Rila"', 'BG'),
    ('Bachkovo Monastery "Virgin Mary"', 'BG'),
    ('Troyan Monastery "Holy Mother''s Assumption"', 'BG'),
    ('Kopan Monastery', 'NP'),
    ('Thrangu Tashi Yangtse Monastery', 'NP'),
    ('Shechen Tennyi Dargyeling Monastery', 'NP'),
    ('Benchen Monastery', 'NP'),
    ('Southern Shaolin Monastery', 'CN'),
    ('Dabei Monastery', 'CN'),
    ('Wa Sau Toi', 'CN'),
    ('Lhunshigyia Monastery', 'CN'),
    ('Rakya Monastery', 'CN'),
    ('Monasteries of Meteora', 'GR'),
    ('The Holy Monastery of Stavronikita', 'GR'),
    ('Taung Kalat Monastery', 'MM'),
    ('Pa-Auk Forest Monastery', 'MM'),
    ('Taktsang Palphug Monastery', 'BT'),
    ('Sümela Monastery', 'TR');

-- Add a "three_rivers" column to the "countries" table
ALTER TABLE countries
ADD COLUMN three_rivers BOOLEAN DEFAULT FALSE;

-- Update "three_rivers" for countries with more than three rivers
UPDATE countries
SET three_rivers = TRUE
WHERE country_code IN (
    SELECT c.country_code
    FROM countries_rivers cr
    JOIN countries c ON cr.country_code = c.country_code
    GROUP BY c.country_code
    HAVING COUNT(*) > 3
);

-- Select "monastery_name" and "country_name" for countries with less than three rivers
SELECT
    m.monastery_name AS "Monastery",
    c.country_name AS "Country"
FROM
    monasteries m
JOIN
    countries c ON m.country_code = c.country_code
WHERE
    c.three_rivers = FALSE
ORDER BY
    m.monastery_name;
