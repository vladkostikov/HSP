4.3.1
SELECT * FROM Customers WHERE ContactName LIKE 'C%';

4.3.2
SELECT * FROM Orders WHERE (Freight BETWEEN 100 AND 200) AND (ShipCountry IN ('USA', 'FRANCE'));

4.3.3
SELECT * FROM EmployeeTerritories WHERE (TerritoryID BETWEEN 6897 AND 31000);
