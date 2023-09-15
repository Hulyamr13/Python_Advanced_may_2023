SELECT
    id,
    first_name,
    last_name,
    CASE
        WHEN salary IS NOT NULL THEN
            TO_CHAR(salary, '9999.99')
        ELSE
            NULL
    END AS salary,
    department_id,
    CASE
        WHEN department_id = 1 THEN 'Management'
        WHEN department_id = 2 THEN 'Kitchen Staff'
        WHEN department_id = 3 THEN 'Service Staff'
        ELSE 'Other'
    END AS department_name
FROM employees
ORDER BY id;
