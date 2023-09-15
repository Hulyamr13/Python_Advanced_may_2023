-- Add a UNIQUE constraint for the "id" and "email" columns
ALTER TABLE minions_info
ADD CONSTRAINT unique_constraint UNIQUE (id, email);

-- Add a CHECK constraint for the "banana" column
ALTER TABLE minions_info
ADD CONSTRAINT banana_check CHECK (banana > 0);