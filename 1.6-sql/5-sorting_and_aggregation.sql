5.4.1
SELECT * FROM Employees ORDER BY BirthDate DESC, Country;

5.4.2
SELECT * FROM Employees WHERE Region IS NOT NULL ORDER BY BirthDate DESC, Country;

5.4.3
SELECT AVG(UnitPrice)[Average price], MIN(UnitPrice)[Min price], MAX(UnitPrice)[Max price] FROM [Order Details];

5.4.4
SELECT COUNT(DISTINCT City) FROM Customers;
