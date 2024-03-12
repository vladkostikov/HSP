10.4.1
SELECT Products.ProductName, [Order Details].UnitPrice
FROM Products INNER JOIN [Order Details]
ON Products.ProductID = [Order Details].ProductID
WHERE [Order Details].UnitPrice < 20;

10.4.2
Выдача получилась объемнее за счёт объединения множеств без фактического соответствия CustomerID.
Встречаются значения NULL Freight для компаний 'Paris spécialités' и 'FISSA Fabrica Inter. Salchichas S.A.', т.к. отсутствуют заказы с их CustomerID.

10.4.3
Добавить к запросу
WHERE Employees.EmployeeID = Orders.EmployeeID

10.4.4
SELECT Products.ProductName, [Order Details].UnitPrice
FROM Products INNER JOIN [Order Details]
ON Products.ProductID = [Order Details].ProductID