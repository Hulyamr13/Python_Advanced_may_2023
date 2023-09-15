-- Delete employees in department 2 or 1
DELETE FROM employees
WHERE department_id IN (1, 2);

-- Select all employees' information ordered by id
SELECT
    id,
    first_name,
    last_name,
    job_title,
    department_id,
    salary
FROM employees
ORDER BY id;