# Задача 3. Комплексная оценка военной эффективности отрядов

### Создайте запрос, оценивающий эффективность военных отрядов на основе:
- Результатов всех сражений (победы/поражения/потери)
- Соотношения побед к общему числу сражений
- Навыков членов отряда и их прогресса
- Качества экипировки
- Истории тренировок и их влияния на результаты
- Выживаемости членов отряда в долгосрочной перспективе

Возможный вариант выдачи:
```json
[
  {
    "squad_id": 401,
    "squad_name": "The Axe Lords",
    "formation_type": "Melee",
    "leader_name": "Urist McAxelord",
    "total_battles": 28,
    "victories": 22,
    "victory_percentage": 78.57,
    "casualty_rate": 24.32,
    "casualty_exchange_ratio": 3.75,
    "current_members": 8,
    "total_members_ever": 12,
    "retention_rate": 66.67,
    "avg_equipment_quality": 4.28,
    "total_training_sessions": 156,
    "avg_training_effectiveness": 0.82,
    "training_battle_correlation": 0.76,
    "avg_combat_skill_improvement": 3.85,
    "overall_effectiveness_score": 0.815,
    "related_entities": {
      "member_ids": [102, 104, 105, 107, 110, 115, 118, 122],
      "equipment_ids": [5001, 5002, 5003, 5004, 5005, 5006, 5007, 5008, 5009],
      "battle_report_ids": [1101, 1102, 1103, 1104, 1105, 1106, 1107, 1108],
      "training_ids": [901, 902, 903, 904, 905, 906]
    }
  },
  {
    "squad_id": 403,
    "squad_name": "Crossbow Legends",
    "formation_type": "Ranged",
    "leader_name": "Dokath Targetmaster",
    "total_battles": 22,
    "victories": 18,
    "victory_percentage": 81.82,
    "casualty_rate": 16.67,
    "casualty_exchange_ratio": 5.20,
    "current_members": 7,
    "total_members_ever": 10,
    "retention_rate": 70.00,
    "avg_equipment_quality": 4.45,
    "total_training_sessions": 132,
    "avg_training_effectiveness": 0.88,
    "training_battle_correlation": 0.82,
    "avg_combat_skill_improvement": 4.12,
    "overall_effectiveness_score": 0.848,
    "related_entities": {
      "member_ids": [106, 109, 114, 116, 119, 123, 125],
      "equipment_ids": [5020, 5021, 5022, 5023, 5024, 5025, 5026],
      "battle_report_ids": [1120, 1121, 1122, 1123, 1124, 1125],
      "training_ids": [920, 921, 922, 923, 924]
    }
  }
]
```

```sql
WITH battle_stats AS (
    SELECT
        sb.squad_id,
        COUNT(sb.battle_id) AS total_battles,
        SUM(CASE WHEN sb.result = 'Victory' THEN 1 ELSE 0 END) AS victories,
        SUM(sb.casualties) AS total_casualties,
        SUM(sb.enemy_casualties) AS total_enemy_casualties
    FROM squad_battles sb
    GROUP BY sb.squad_id
),
member_stats AS (
    SELECT
        sm.squad_id,
        SUM(CASE WHEN sm.exit_date IS NULL THEN 1 ELSE 0 END) AS current_members,
        COUNT(DISTINCT sm.dwarf_id) AS total_members_ever
    FROM squad_members sm
    GROUP BY sm.squad_id
),
equipment_stats AS (
    SELECT
        se.squad_id,
        SUM(e.quality * se.quantity) * 1.0 / SUM(se.quantity) AS avg_equipment_quality
    FROM squad_equipment se
    JOIN equipment e ON se.equipment_id = e.equipment_id
    GROUP BY se.squad_id
),
training_stats AS (
    SELECT
        st.squad_id,
        SUM(FLOOR((EXTRACT(EPOCH FROM (NOW() - date)) / 3600) / st.frequency)) AS total_training_sessions,
        ROUND(AVG(effectiveness), 2) AS avg_training_effectiveness
    FROM
        squad_training st
    GROUP BY st.squad_id
)

SELECT
    s.squad_id,
    s.squad_name,
    s.formation_type,
    d.name AS leader_name,
    bs.total_battles,
    bs.victories,
    ROUND(bs.victories::DECIMAL / NULLIF(bs.total_battles, 0), 2) AS victory_percentage,
    ROUND(bs.total_casualties::DECIMAL / NULLIF(bs.total_battles, 0), 2) AS casualty_rate,
    ROUND(bs.total_enemy_casualties::DECIMAL / NULLIF(bs.total_casualties, 0), 2) AS casualty_exchange_ratio,
    ms.current_members,
    ms.total_members_ever,
    ROUND(ms.current_members::DECIMAL / NULLIF(ms.total_members_ever,0), 2) AS retention_rate,
    es.avg_equipment_quality,
    ts.total_training_sessions,
    ts.avg_training_effectiveness,
    ROUND(
        (bs.victories::DECIMAL / NULLIF(bs.total_battles, 0)) * 0.3 +
        (1 - (bs.total_casualties::DECIMAL / NULLIF(ms.total_members_ever, 0))) * 0.2 +
        (ms.current_members::DECIMAL / NULLIF(ms.total_members_ever, 0)) * 0.15 +
        (es.avg_equipment_quality::DECIMAL / 10) * 0.2 +
        (ts.avg_training_effectiveness) * 0.15,
        3
    ) AS overall_effectiveness_score
    CORR(ts.total_training_sessions, bs.victories) AS training_battle_correlation,
    JSON_OBJECT(
        'member_ids', (
            SELECT JSON_ARRAYAGG(sm.dwarf_id)
            FROM squad_members sm
            WHERE s.squad_id = sm.squad_id
        ),
        'equipment_ids', (
            SELECT JSON_ARRAYAGG(sq.equipment_id)
            FROM squad_equipment sq
            WHERE s.squad_id = sq.squad_id
        ),
        'battle_report_ids', (
            SELECT JSON_ARRAYAGG(sb.report_id)
            FROM squad_battles sb
            WHERE s.squad_id = sb.squad_id
        ),
        'training_ids', (
            SELECT JSON_ARRAYAGG(st.schedule_id)
            FROM squad_training st
            WHERE s.squad_id = st.squad_id
        )
    ) AS related_entities
FROM military_squads s
LEFT JOIN dwarves d ON s.leader_id = d.dwarf_id
LEFT JOIN battle_stats bs ON s.squad_id = bs.squad_id
LEFT JOIN member_stats ms ON s.squad_id = ms.squad_id
LEFT JOIN equipment_stats es ON s.squad_id = es.squad_id
LEFT JOIN training_stats ts ON s.squad_id = ts.squad_id
GROUP BY s.squad_id, s.formation_type
ORDER BY overall_effectiveness_score
```
