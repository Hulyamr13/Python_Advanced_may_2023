-- Create the "employees" table
CREATE TABLE employees (
    id serial PRIMARY KEY NOT NULL,
    first_name VARCHAR(30),
    last_name VARCHAR(50),
    hiring_date DATE,
    salary NUMERIC(10, 2),
    devices_number INTEGER
);

-- Create the "departments" table
CREATE TABLE departments (
    id serial PRIMARY KEY NOT NULL,
    name VARCHAR(50),
    code CHAR(3),
    description TEXT
);

-- Create the "issues" table
CREATE TABLE issues (
    id serial PRIMARY KEY UNIQUE,
    description VARCHAR(150),
    date DATE,
    start TIMESTAMP
);
