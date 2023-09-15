SELECT department_id, COUNT(CASE WHEN salary IS NOT NULL THEN 1 ELSE NULL END) AS employee_count
FROM employees
GROUP BY department_id
ORDER BY department_id;
