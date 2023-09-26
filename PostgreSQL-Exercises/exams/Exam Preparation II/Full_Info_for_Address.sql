-- Create the search_results table if it doesn't exist
CREATE TABLE IF NOT EXISTS search_results (
    id SERIAL PRIMARY KEY,
    address_name VARCHAR(100),
    full_name VARCHAR(100),
    level_of_bill VARCHAR(20),
    make VARCHAR(30),
    condition CHAR(1),
    category_name VARCHAR(50)
);

-- Create or replace the stored procedure
CREATE OR REPLACE PROCEDURE sp_courses_by_address(
    IN address_name VARCHAR(100)
)
LANGUAGE plpgsql
AS $$
BEGIN
    -- Clear previous results from the table
    TRUNCATE TABLE search_results;

    -- Insert new results into the table
    INSERT INTO search_results (
        address_name,
        full_name,
        level_of_bill,
        make,
        condition,
        category_name
    )
    SELECT
        a."name" AS address_name,
        cl.full_name AS full_name,
        CASE
            WHEN cou.bill <= 20 THEN 'Low'
            WHEN cou.bill <= 30 THEN 'Medium'
            ELSE 'High'
        END AS level_of_bill,
        c.make AS make,
        c.condition AS condition,
        cat."name" AS category_name
    FROM
        courses AS cou
    INNER JOIN
        addresses AS a
        ON cou.from_address_id = a."id"
    INNER JOIN
        clients AS cl
        ON cou.client_id = cl."id"
    INNER JOIN
        cars AS c
        ON cou.car_id = c."id"
    INNER JOIN
        categories AS cat
        ON c.category_id = cat."id"
    WHERE
        a."name" = address_name
    ORDER BY
        c.make,
        cl.full_name;
END;
$$;
