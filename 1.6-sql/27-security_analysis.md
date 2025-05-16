# Задача 5. Многофакторный анализ угроз и безопасности крепости

### Разработайте запрос, который комплексно анализирует безопасность крепости, учитывая:
- Историю всех атак существ и их исходов
- Эффективность защитных сооружений
- Соотношение между типами существ и результативностью обороны
- Оценку уязвимых зон на основе архитектуры крепости
- Корреляцию между сезонными факторами и частотой нападений
- Готовность военных отрядов и их расположение
- Эволюцию защитных способностей крепости со временем

Возможный вариант выдачи:
```json
{
  "total_recorded_attacks": 183,
  "unique_attackers": 42,
  "overall_defense_success_rate": 76.50,
  "security_analysis": {
    "threat_assessment": {
      "current_threat_level": "Moderate",
      "active_threats": [
        {
          "creature_type": "Goblin",
          "threat_level": 3,
          "last_sighting_date": "0205-08-12",
          "territory_proximity": 1.2,
          "estimated_numbers": 35,
          "creature_ids": [124, 126, 128, 132, 136]
        },
        {
          "creature_type": "Forgotten Beast",
          "threat_level": 5,
          "last_sighting_date": "0205-07-28",
          "territory_proximity": 3.5,
          "estimated_numbers": 1,
          "creature_ids": [158]
        }
      ]
    },
    "vulnerability_analysis": [
      {
        "zone_id": 15,
        "zone_name": "Eastern Gate",
        "vulnerability_score": 0.68,
        "historical_breaches": 8,
        "fortification_level": 2,
        "military_response_time": 48,
        "defense_coverage": {
          "structure_ids": [182, 183, 184],
          "squad_ids": [401, 405]
        }
      }
    ],
    "defense_effectiveness": [
      {
        "defense_type": "Drawbridge",
        "effectiveness_rate": 95.12,
        "avg_enemy_casualties": 12.4,
        "structure_ids": [185, 186, 187, 188]
      },
      {
        "defense_type": "Trap Corridor",
        "effectiveness_rate": 88.75,
        "avg_enemy_casualties": 8.2,
        "structure_ids": [201, 202, 203, 204]
      }
    ],
    "military_readiness_assessment": [
      {
        "squad_id": 403,
        "squad_name": "Crossbow Legends",
        "readiness_score": 0.92,
        "active_members": 7,
        "avg_combat_skill": 8.6,
        "combat_effectiveness": 0.85,
        "response_coverage": [
          {
            "zone_id": 12,
            "response_time": 0
          },
          {
            "zone_id": 15,
            "response_time": 36
          }
        ]
      }
    ],
    "security_evolution": [
      {
        "year": 203,
        "defense_success_rate": 68.42,
        "total_attacks": 38,
        "casualties": 42,
        "year_over_year_improvement": 3.20
      },
      {
        "year": 204,
        "defense_success_rate": 72.50,
        "total_attacks": 40,
        "casualties": 36,
        "year_over_year_improvement": 4.08
      }
    ]
  }
}
```

```sql
WITH attack_history AS (
    SELECT
        c.creature_id,
        c.name AS creature_type,
        COUNT(ca.attack_id) AS total_attacks,
        SUM(CASE WHEN ca.outcome = 'Defended' THEN 1 ELSE 0 END) AS successful_defenses,
        MAX(ca.date) AS last_attack_date
    FROM creature_attacks ca
    JOIN creatures c ON ca.creature_id = c.creature_id
    GROUP BY c.creature_id, c.name
),

threat_level_calculation AS (
    SELECT
        CASE
            WHEN (SELECT COUNT(*) FROM creature_attacks WHERE date >= CURRENT_DATE - INTERVAL '1 year') > 50 THEN 'High'
            WHEN (SELECT COUNT(*) FROM creature_attacks WHERE date >= CURRENT_DATE - INTERVAL '1 year') > 20 THEN 'Moderate'
            ELSE 'Low'
        END AS current_threat_level
),

defense_effectiveness AS (
    SELECT
        ca.defense_structures_used AS defense_type,
        COUNT(ca.attack_id) AS total_attacks,
        SUM(CASE WHEN ca.outcome = 'Defended' THEN 1 ELSE 0 END) AS successful_defenses,
        AVG(ca.enemy_casualties) AS avg_enemy_casualties
    FROM creature_attacks ca
    GROUP BY ca.defense_structures_used
),

vulnerable_zones AS (
    SELECT
        l.location_id AS zone_id,
        l.name AS zone_name,
        COUNT(ca.attack_id) AS historical_breaches,
        l.fortification_level,
        AVG(ca.military_response_time_minutes) AS avg_military_response_time
    FROM creature_attacks ca
    JOIN creature_sightings cs ON ca.creature_id = cs.creature_id
    JOIN locations l ON cs.location = l.name
    GROUP BY l.location_id, l.name, l.fortification_level
),

military_readiness AS (
    SELECT
        ms.squad_id,
        ms.name AS squad_name,
        COUNT(sm.dwarf_id) AS active_members,
        AVG(ds.level) AS avg_combat_skill,
        AVG(CASE WHEN ca.outcome = 'Defended' THEN 1 ELSE 0 END) AS combat_effectiveness,
        ARRAY_AGG(DISTINCT l.location_id) AS response_coverage_zones
    FROM military_squads ms
    JOIN squad_members sm ON ms.squad_id = sm.squad_id
    JOIN dwarves d ON sm.dwarf_id = d.dwarf_id
    JOIN dwarf_skills ds ON d.dwarf_id = ds.dwarf_id
    JOIN skills s ON ds.skill_id = s.skill_id AND s.skill_type = 'Combat'
    LEFT JOIN fortresses f ON d.fortress_id = f.fortress_id
    LEFT JOIN locations l ON l.name = f.location
    GROUP BY ms.squad_id, ms.name
),

security_evolution AS (
    SELECT
        EXTRACT(YEAR FROM ca.date) AS year,
        SUM(CASE WHEN ca.outcome = 'Defended' THEN 1 ELSE 0 END) * 100.0 / COUNT(*) AS defense_success_rate,
        COUNT(*) AS total_attacks,
        SUM(ca.casualties) AS casualties,
        (SUM(CASE WHEN ca.outcome = 'Defended' THEN 1 ELSE 0 END) * 100.0 / COUNT(*)) -
        LAG(SUM(CASE WHEN ca.outcome = 'Defended' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 1) OVER (ORDER BY EXTRACT(YEAR FROM ca.date)) AS year_over_year_improvement
    FROM creature_attacks ca
    GROUP BY EXTRACT(YEAR FROM ca.date)
),

SELECT
    JSON_OBJECT(
        'total_recorded_attacks', (SELECT COUNT(*) FROM creature_attacks),
        'unique_attackers', (SELECT COUNT(DISTINCT creature_id) FROM creature_attacks),
        'overall_defense_success_rate', (SELECT (SUM(CASE WHEN outcome = 'Defended' THEN 1 ELSE 0 END) * 100.0 / COUNT(*)) FROM creature_attacks),
        'security_analysis', JSON_OBJECT(
            'threat_assessment', JSON_OBJECT(
                'current_threat_level', (SELECT current_threat_level FROM threat_level_calculation),
                'active_threats', (
                    SELECT JSON_ARRAYAGG(
                        JSON_OBJECT(
                            'creature_type', creature_type,
                            'threat_level', threat_level,
                            'last_sighting_date', last_attack_date,
                            'territory_proximity', territory_proximity,
                            'estimated_numbers', estimated_numbers,
                            'creature_ids', (
                                SELECT JSON_ARRAYAGG(creature_id)
                                FROM creatures c
                                WHERE c.name = ah.creature_type
                            )
                        )
                    )
                    FROM (
                        SELECT
                            ah.creature_type,
                            c.threat_level,
                            ah.last_attack_date,
                            ct.distance_to_fortress AS territory_proximity,
                            ah.total_attacks AS estimated_numbers
                        FROM attack_history ah
                        JOIN creatures c ON ah.creature_id = c.creature_id
                        JOIN creature_territories ct ON c.creature_id = ct.creature_id
                        WHERE ah.last_attack_date >= CURRENT_DATE - INTERVAL '1 year'
                        GROUP BY ah.creature_type, c.threat_level, ah.last_attack_date, ct.distance_to_fortress, ah.total_attacks
                    ) AS active_threats
                )
            ),
            'vulnerability_analysis', (
                SELECT JSON_ARRAYAGG(
                    JSON_OBJECT(
                        'zone_id', zone_id,
                        'zone_name', zone_name,
                        'vulnerability_score', (historical_breaches / (historical_breaches + 1)),
                        'historical_breaches', historical_breaches,
                        'fortification_level', fortification_level,
                        'military_response_time', avg_military_response_time,
                        'defense_coverage', JSON_OBJECT(
                            'structure_ids', (
                                SELECT JSON_ARRAYAGG(ca.defense_structures_used)
                                FROM creature_attacks ca
                                JOIN creature_sightings cs ON ca.creature_id = cs.creature_id
                                JOIN locations l2 ON cs.location = l2.name
                                WHERE l2.location_id = vz.zone_id
                            ),
                            'squad_ids', (
                                SELECT JSON_ARRAYAGG(ms.squad_id)
                                FROM military_squads ms
                                JOIN fortresses f ON ms.fortress_id = f.fortress_id
                                JOIN locations l3 ON l3.name = f.location
                                WHERE l3.location_id = vz.zone_id
                            )
                        )
                    )
                )
                FROM vulnerable_zones vz
            ),
            'defense_effectiveness', (
                SELECT JSON_ARRAYAGG(
                    JSON_OBJECT(
                        'defense_type', defense_type,
                        'effectiveness_rate', (successful_defenses * 100.0 / total_attacks),
                        'avg_enemy_casualties', avg_enemy_casualties,
                        'structure_ids', (
                            SELECT JSON_ARRAYAGG(ca.defense_structures_used)
                            FROM creature_attacks ca
                            WHERE ca.defense_structures_used = de.defense_type
                        )
                    )
                )
                FROM defense_effectiveness de
            ),
            'military_readiness_assessment', (
                SELECT JSON_ARRAYAGG(
                    JSON_OBJECT(
                        'squad_id', squad_id,
                        'squad_name', squad_name,
                        'readiness_score', (active_members * avg_combat_skill * combat_effectiveness) / 100,
                        'active_members', active_members,
                        'avg_combat_skill', avg_combat_skill,
                        'combat_effectiveness', combat_effectiveness,
                        'response_coverage', (
                            SELECT JSON_ARRAYAGG(
                                JSON_OBJECT(
                                    'zone_id', l.location_id,
                                    'response_time', ca.military_response_time_minutes
                                )
                            )
                            FROM creature_attacks ca
                            JOIN creature_sightings cs ON ca.creature_id = cs.creature_id
                            JOIN locations l ON cs.location = l.name
                        )
                    )
                )
                FROM military_readiness mr
            ),
            'security_evolution', (
                SELECT JSON_ARRAYAGG(
                    JSON_OBJECT(
                        'year', year,
                        'defense_success_rate', defense_success_rate,
                        'total_attacks', total_attacks,
                        'casualties', casualties,
                        'year_over_year_improvement', year_over_year_improvement
                    )
                )
                FROM security_evolution
            )
        )
    );
```
