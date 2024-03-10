9.4.1
SELECT t1.CustomerID, t2.CustomerID
FROM Customers t1, Customers t2
WHERE t1.Region IS NULL AND t2.Region IS NULL;

9.4.2
SELECT * FROM Orders
WHERE CustomerID = ANY (SELECT CustomerID FROM Customers WHERE Region IS NOT NULL);

9.4.3
SELECT * FROM Orders
WHERE Freight > ANY(SELECT Products.UnitPrice FROM Products);
