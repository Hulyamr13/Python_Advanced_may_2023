UPDATE currencies
SET description = SUBSTRING(description FROM 5);

SELECT description AS "substring"
FROM currencies;
