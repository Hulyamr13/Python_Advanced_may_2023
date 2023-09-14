SELECT title, CAST(cost AS numeric(10, 3)) AS modified_price
FROM books
ORDER BY id;
