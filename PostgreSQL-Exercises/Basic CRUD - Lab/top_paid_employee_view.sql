-- Create a view for the top-paid employee
CREATE VIEW top_paid_employee AS
SELECT *
FROM employees
WHERE salary = (SELECT MAX(salary) FROM employees);

-- Query the view to retrieve information about the top-paid employee
SELECT * FROM top_paid_employee;