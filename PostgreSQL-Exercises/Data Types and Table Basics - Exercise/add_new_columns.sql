ALTER TABLE minions_info
ADD COLUMN email character varying(20),
ADD COLUMN equipped BOOLEAN CHECK (equipped IN (TRUE, FALSE, NULL));


ALTER TABLE minions_info
ADD COLUMN email VARCHAR(20),
ADD COLUMN equipped BOOL NOT NULL;
