3.9.1
SELECT ProductName, UnitsInStock FROM Products;

3.9.2
SELECT ProductName, UnitPrice FROM Products WHERE UnitPrice < 20;

3.9.3
SELECT * FROM Orders WHERE (Freight >= 11.7) AND (Freight <= 98.1);

3.9.4
SELECT * FROM Employees WHERE (TitleOfCourtesy = 'Mr.') OR (TitleOfCourtesy = 'Dr.');

3.9.5
SELECT * FROM Suppliers WHERE Country = 'Japan';

3.9.6
SELECT * FROM Orders WHERE EmployeeID IN (2, 4, 8);

3.9.7
SELECT OrderID, ProductID FROM [Order Details] WHERE (UnitPrice > 40) AND (Quantity < 10);
