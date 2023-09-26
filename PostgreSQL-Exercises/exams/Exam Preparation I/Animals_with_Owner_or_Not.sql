CREATE OR REPLACE PROCEDURE sp_animals_with_owners_or_not_1(
	IN animal_name VARCHAR(30),
	OUT owner_name TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
    SELECT
		COALESCE(o."name", 'For adoption')
    INTO
		owner_name
    FROM
		animals AS a
    LEFT JOIN
		owners AS o
		ON
		a.owner_id = o."id"
    WHERE
		a."name" = animal_name;
END;
$$;


CALL sp_animals_with_owners_or_not_1('Pumpkinseed Sunfish', '');
CALL sp_animals_with_owners_or_not_1('Hippo', '');
CALL sp_animals_with_owners_or_not_1('Brown bear', '');