15.7
ALTER TABLE Region ADD CONSTRAINT PK_Region_RegionID PRIMARY KEY (RegionID);

CREATE TABLE Territories (
     TerritoryID int NOT NULL,
     TerritoryDescription nchar(50) NOT NULL,
     RegionID int NOT NULL,
     CONSTRAINT PK_Territories_TerritoryID PRIMARY KEY (TerritoryID),
     CONSTRAINT FK_Territories_Region FOREIGN KEY (RegionID)
         REFERENCES Region (RegionID),
);

INSERT INTO Region (RegionID, RegionDescription)
VALUES (1, 'Moscow'), (2, 'Saint Petersburg');

INSERT INTO Territories (TerritoryID, TerritoryDescription, RegionID)
VALUES (1, 'Kremlin', 1), (2, 'Bolshoi Theatre', 1), (3, 'Hermitage', 2);
