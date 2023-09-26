-- Update animals without an owner to be owned by Kaloqn Stoqnov (ID: 4)
UPDATE animals
SET owner_id = 4
WHERE owner_id IS NULL;