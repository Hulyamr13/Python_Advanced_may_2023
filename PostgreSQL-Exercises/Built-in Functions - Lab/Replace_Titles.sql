-- Update titles that start with "The" to replace with "***"
UPDATE books
SET title = REPLACE(title, 'The', '***')
WHERE title LIKE 'The%';

-- Select updated titles
SELECT title
FROM books
WHERE title LIKE '***%'
ORDER BY id;


SELECT
    CASE
        WHEN POSITION('The' IN title) = 1 THEN CONCAT('***', SUBSTRING(title FROM 4))
        ELSE title
    END AS title
FROM
    books
WHERE
    POSITION('The' IN title) = 1
ORDER BY
    id;