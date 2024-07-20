20.1
SELECT
    *
FROM
    Squads
WHERE
    leader_id IS NULL;

20.2
SELECT
    *
FROM
    Dwarves
WHERE
    age > 150 AND profession = 'Warrior';

20.3
SELECT DISTINCT
    D.dwarf_id,
    D.name,
    D.age,
    D.profession,
    D.squad_id
FROM
    Dwarves AS D
JOIN
    Items AS I
ON
    D.dwarf_id = I.owner_id
WHERE
    I.type = 'weapon';

20.4
SELECT
    D.dwarf_id AS DwarfId,
    D.name AS DwarfName,
    T.status AS TaskStatus,
    COUNT(T.task_id) AS TaskCount
FROM
    Dwarves AS D
JOIN
    Tasks AS T
ON
    D.dwarf_id = T.assigned_to
GROUP BY
    D.dwarf_id,
    D.name,
    T.status;

20.5
SELECT
    T.task_id,
    T.description,
    T.assigned_to,
    T.status
FROM
    Tasks AS T
JOIN
    Dwarves AS D
ON
    T.assigned_to = D.dwarf_id
JOIN
    Squads AS S
ON
    D.squad_id = S.squad_id
WHERE
    S.name = 'Guardians';

20.6
SELECT
    D1.dwarf_id AS DwarfID,
    D1.name AS Name,
    R.related_to AS RelatedTo,
    D2.name AS RelativeName,
    R.relationship AS RelationshipType
FROM
    Relationships AS R
JOIN
    Dwarves AS D1
ON
    R.dwarf_id = D1.dwarf_id
JOIN
    Dwarves AS D2
ON
    R.related_to = D2.dwarf_id
ORDER BY
    R.dwarf_id ASC;
