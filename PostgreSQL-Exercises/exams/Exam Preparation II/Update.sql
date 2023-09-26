-- 42601: syntax error at or near "21"

UPDATE cars
SET "condition" = 'C'
WHERE (
    (mileage >= 800000 OR mileage IS NULL)
    AND "year" <= 2010
    AND make != 'Mercedes-Benz'
);