ALTER TABLE minions_info
ADD COLUMN code character(4),
ADD COLUMN task text,
ADD COLUMN salary numeric(8, 3);