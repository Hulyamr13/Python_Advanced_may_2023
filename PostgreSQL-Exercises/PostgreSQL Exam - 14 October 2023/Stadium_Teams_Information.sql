CREATE OR REPLACE FUNCTION fn_stadium_team_name(stadium_name VARCHAR(30)) RETURNS TABLE (fn_stadium_team_name VARCHAR(45)) AS $$
BEGIN
    RETURN QUERY
    SELECT t.name
    FROM teams t
    WHERE t.stadium_id = (SELECT s.id FROM stadiums s WHERE s.name = stadium_name)
    ORDER BY t.name;

    RETURN;
END;
$$ LANGUAGE plpgsql;