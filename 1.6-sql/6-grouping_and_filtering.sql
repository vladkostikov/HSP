6.3.1
SELECT ContactType, COUNT(*) AS NUMBER
FROM Contacts
GROUP BY ContactType;

6.3.2
SELECT CategoryID, AVG(UnitPrice) AS AVG_PRICE
FROM Products
GROUP BY CategoryID
ORDER BY AVG_PRICE ASC;