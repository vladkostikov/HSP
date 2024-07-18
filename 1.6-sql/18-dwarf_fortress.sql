18.1
SELECT
    Dwarves.dwarf_id,
    Dwarves.name AS dwarf_name,
    Dwarves.age,
    Dwarves.profession,
    Squads.squad_id,
    Squads.name AS squad_name,
    Squads.mission
FROM Dwarves
INNER JOIN Squads ON Dwarves.squad_id = Squads.squad_id
WHERE dwarves.squad_id IS NOT NULL;

18.2
SELECT *
FROM Dwarves
WHERE Dwarves.profession = 'miner' AND Dwarves.squad_id IS NULL;

18.3
SELECT *
FROM Tasks
WHERE Tasks.priority = (SELECT MAX(Tasks.priority) FROM Tasks)
    AND Tasks.status = 'pending';

18.4
SELECT
    Dwarves.dwarf_id,
    Dwarves.name,
    COUNT(Items.item_id) AS "Items count"
FROM Dwarves
INNER JOIN Items ON Dwarves.dwarf_id = Items.owner_id
GROUP BY Dwarves.dwarf_id, Dwarves.name;

18.5
SELECT
    Squads.squad_id,
    Squads.name AS squad_name,
    Squads.mission,
    COUNT(Dwarves.dwarf_id) AS "Dwarves count"
FROM Squads
LEFT JOIN Dwarves ON Squads.squad_id = Dwarves.squad_id
GROUP BY Squads.squad_id, Squads.name, Squads.mission;

18.6
SELECT
    Dwarves.profession,
    COUNT(Tasks.task_id) AS "Unfinished tasks"
FROM Dwarves
INNER JOIN Tasks ON Dwarves.dwarf_id = Tasks.assigned_to
WHERE Tasks.status <> 'Completed'
GROUP BY Dwarves.profession
ORDER BY "Unfinished tasks" DESC;


18.7
SELECT
    Items.type,
    AVG(Dwarves.age) AS "Average owner age"
FROM Items
INNER JOIN Dwarves on Items.owner_id = Dwarves.dwarf_id
GROUP BY Items.type;


18.8
SELECT *
FROM Dwarves
LEFT JOIN Items on Dwarves.dwarf_id = Items.owner_id
WHERE Dwarves.age > (SELECT AVG(age) FROM Dwarves)
    AND Items.owner_id IS NULL;
