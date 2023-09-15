CREATE TABLE minions_birthdays (
    id serial PRIMARY KEY,
    name character varying(50) NOT NULL,
    date_of_birth date NOT NULL,
    age integer NOT NULL,
    present character varying(100),
    party timestamp with time zone NOT NULL
);
