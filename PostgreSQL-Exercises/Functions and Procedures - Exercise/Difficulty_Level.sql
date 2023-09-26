CREATE OR REPLACE FUNCTION fn_difficulty_level(level INT) RETURNS VARCHAR AS
$$
DECLARE
    difficulty VARCHAR;
BEGIN
    IF level <= 40 THEN
        difficulty := 'Normal Difficulty';
    ELSIF level BETWEEN 41 AND 60 THEN
        difficulty := 'Nightmare Difficulty';
    ELSE
        difficulty := 'Hell Difficulty';
    END IF;

    RETURN difficulty;
END;
$$
LANGUAGE plpgsql;

SELECT
    ug.user_id,
    ug.level,
    ug.cash,
    fn_difficulty_level(ug.level) AS difficulty_level
FROM
    users_games ug
ORDER BY
    ug.user_id;
