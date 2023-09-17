-- Drop existing tables if they exist
DROP TABLE IF EXISTS customers CASCADE;
DROP TABLE IF EXISTS contacts CASCADE;

-- Create the customers table
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    customer_name VARCHAR(50)
);

-- Create the contacts table with a foreign key constraint
CREATE TABLE contacts (
    id SERIAL PRIMARY KEY,
    contact_name VARCHAR(50),
    phone VARCHAR(20),
    email VARCHAR(50),
    customer_id INT,
    CONSTRAINT fk_contacts_customers
        FOREIGN KEY (customer_id)
        REFERENCES customers(id) ON DELETE SET NULL
);

-- Insert data into the customers table
INSERT INTO customers (customer_name)
VALUES ('BlueBird Inc'), ('Dolphin LLC');

-- Insert data into the contacts table
INSERT INTO contacts (contact_name, phone, email, customer_id)
VALUES
    ('John Doe', '(408)-111-1234', 'john.doe@bluebird.dev', 1),
    ('Jane Doe', '(408)-111-1235', 'jane.doe@bluebird.dev', 1),
    ('David Wright', '(408)-222-1234', 'david.wright@dolphin.dev', 2);

-- Delete the row from the customers table where id matches 1
DELETE FROM customers
WHERE id = 1;
