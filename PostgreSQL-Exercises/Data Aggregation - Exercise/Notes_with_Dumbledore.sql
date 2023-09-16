SELECT
    last_name,
    COUNT(notes) AS "Dumbledore Notes Count"
FROM
    wizard_deposits
WHERE
    notes LIKE '%Dumbledore%'
GROUP BY
    last_name;
