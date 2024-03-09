8.3.1
SELECT Products.ProductName, Categories.CategoryName
FROM Products, Categories
WHERE Products.CategoryID = Categories.CategoryID;

8.3.2
SELECT Products.ProductName, [Order Details].UnitPrice
FROM Products, [Order Details]
WHERE Products.ProductID = [Order Details].ProductID
  AND [Order Details].UnitPrice < 20;

8.3.3
SELECT Products.ProductName, Categories.CategoryName, [Order Details].UnitPrice
FROM Products, [Order Details], Categories
WHERE Products.ProductID = [Order Details].ProductID
  AND [Order Details].UnitPrice < 20
  AND Products.CategoryID = Categories.CategoryID;
