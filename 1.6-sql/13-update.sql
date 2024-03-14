13.3.1
UPDATE [Order Details]
SET Discount = 0.20
WHERE Quantity > 50

13.3.2
UPDATE Contacts
SET City = 'Piter', Country = 'Russia'
WHERE City = 'Berlin' AND Country = 'Germany'

13.3.3
INSERT INTO Shippers
VALUES ('Apple', '1–800–854–3680'), ('Amazon', '1-888-280-4331');

DELETE FROM Shippers
WHERE ShipperID > 3;