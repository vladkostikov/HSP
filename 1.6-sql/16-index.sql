16
CREATE UNIQUE CLUSTERED INDEX PK_Territories ON Territories (TerritoryID);
CREATE INDEX idx_Territories_RegionID ON Territories (RegionID);

CREATE UNIQUE CLUSTERED INDEX PK_Region ON Region (RegionID);
