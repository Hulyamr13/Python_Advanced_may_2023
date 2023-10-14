SELECT
    CONCAT(c.first_name, ' ', c.last_name) AS coach_full_name,
    CONCAT(p.first_name, ' ', p.last_name) AS player_full_name,
    t.name AS team_name,
    ps.passing,
    ps.shooting,
    ps.speed
FROM coaches c
JOIN players_coaches pc ON c.id = pc.coach_id
JOIN players p ON pc.player_id = p.id
JOIN teams t ON p.team_id = t.id
JOIN skills_data ps ON p.skills_data_id = ps.id
ORDER BY coach_full_name ASC, player_full_name DESC;