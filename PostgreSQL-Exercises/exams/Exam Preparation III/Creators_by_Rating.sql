SELECT
    c.last_name,
    CEIL(AVG(bg.rating)) AS average_rating,
    'Stonemaier Games' AS publisher_name
FROM
    creators AS c
JOIN
    creators_board_games AS cbg ON c.id = cbg.creator_id
JOIN
    board_games AS bg ON cbg.board_game_id = bg.id
JOIN
    publishers AS p ON bg.publisher_id = p.id
WHERE
    p.name = 'Stonemaier Games'
GROUP BY
    c.last_name
HAVING
    COUNT(cbg.creator_id) > 0
ORDER BY
    average_rating DESC;
