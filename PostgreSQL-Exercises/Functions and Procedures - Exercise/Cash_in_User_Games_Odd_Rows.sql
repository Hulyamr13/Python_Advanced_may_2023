CREATE OR REPLACE FUNCTION fn_cash_in_users_games(game_name VARCHAR(50))
RETURNS TABLE (total_cash NUMERIC)
LANGUAGE SQL
AS $$
    SELECT ROUND(SUM(cash), 2) AS total_cash
    FROM (
        SELECT cash, ROW_NUMBER() OVER (ORDER BY cash DESC) AS row_num
        FROM users_games
        WHERE game_id = (SELECT id FROM games WHERE name = game_name)
    ) AS ranked_rows
    WHERE row_num % 2 <> 0;
$$;