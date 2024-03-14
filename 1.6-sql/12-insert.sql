12.3.1
INSERT INTO Employees (FirstName, LastName, Title, TitleOfCourtesy, BirthDate, HireDate, Address, PostalCode, City, Country, HomePhone, ReportsTo)
VALUES ('Vladislav', 'Kostikov', 'Software Engineer', 'Mr.', '2001-11-20T12:00:00.000', '2024-03-14T10:00:00.000', 'Kremlin', '109012', 'Moscow', 'Russia', '+7(495) 695-41-87', 2)

12.3.2
INSERT INTO EmployeeTerritories (EmployeeID, TerritoryID)
VALUES (16, 19428)

12.3.3
INSERT INTO Orders (CustomerID, EmployeeID, OrderDate, RequiredDate, ShipVia, Freight, ShipName, ShipAddress, ShipCity, ShipPostalCode, ShipCountry)
VALUES ('RATTC', 16, '2024-03-14T11:00:00.000', '2024-03-15T12:00:00.000', 1, 50, 'Anyone', 'Kremlin', 'Moscow',  '109012', 'Russia')
