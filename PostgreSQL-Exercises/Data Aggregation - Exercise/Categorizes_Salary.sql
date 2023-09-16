WITH AvgSalaries AS (
    SELECT
        job_title,
        AVG(salary) AS avg_salary
    FROM
        employees
    GROUP BY
        job_title
)

SELECT
    job_title,
    CASE
        WHEN avg_salary > 45800 THEN 'Good'
        WHEN avg_salary BETWEEN 27500 AND 45800 THEN 'Medium'
        ELSE 'Need Improvement'
    END AS "Category"
FROM
    AvgSalaries
ORDER BY
    "Category" ASC,
    job_title ASC;
