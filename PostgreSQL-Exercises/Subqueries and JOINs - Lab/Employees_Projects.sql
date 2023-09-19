SELECT ep.employee_id,
       CONCAT(e.first_name, ' ', e.last_name) AS "full_name",
       p.project_id,
       p.name
FROM employees_projects ep
JOIN employees e ON e.employee_id = ep.employee_id
JOIN projects p ON p.project_id = ep.project_id
WHERE p.name = 'Classic Vest';
