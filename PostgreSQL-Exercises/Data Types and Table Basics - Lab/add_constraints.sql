-- Set the "salary" column as NOT NULL with a default value of 0
ALTER TABLE employees
ALTER COLUMN salary SET NOT NULL,
ALTER COLUMN salary SET DEFAULT 0;

-- Set the "hiring_date" column as NOT NULL
ALTER TABLE employees
ALTER COLUMN hiring_date SET NOT NULL;
