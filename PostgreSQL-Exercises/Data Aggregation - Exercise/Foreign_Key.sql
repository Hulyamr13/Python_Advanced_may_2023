CREATE TABLE employees_projects (
    id serial PRIMARY KEY,
    employee_id integer REFERENCES employees(id),
    project_id integer REFERENCES projects(id)
);
