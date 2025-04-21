# Задача 1. Анализ эффективности экспедиций

### Напишите запрос, который определит наиболее и наименее успешные экспедиции, учитывая:
- Соотношение выживших участников к общему числу
- Ценность найденных артефактов
- Количество обнаруженных новых мест
- Успешность встреч с существами (отношение благоприятных исходов к неблагоприятным)
- Опыт, полученный участниками (сравнение навыков до и после)

Возможный вариант выдачи:
```json
[
  {
    "expedition_id": 2301,
    "destination": "Ancient Ruins",
    "status": "Completed",
    "survival_rate": 71.43,
    "artifacts_value": 28500,
    "discovered_sites": 3,
    "encounter_success_rate": 66.67,
    "skill_improvement": 14,
    "expedition_duration": 44,
    "overall_success_score": 0.78,
    "related_entities": {
      "member_ids": [102, 104, 107, 110, 112, 115, 118],
      "artifact_ids": [2501, 2502, 2503],
      "site_ids": [2401, 2402, 2403]
    }
  },
  {
    "expedition_id": 2305,
    "destination": "Deep Caverns",
    "status": "Completed",
    "survival_rate": 80.00,
    "artifacts_value": 42000,
    "discovered_sites": 2,
    "encounter_success_rate": 83.33,
    "skill_improvement": 18,
    "expedition_duration": 38,
    "overall_success_score": 0.85,
    "related_entities": {
      "member_ids": [103, 105, 108, 113, 121],
      "artifact_ids": [2508, 2509, 2510, 2511],
      "site_ids": [2410, 2411]
    }
  },
  {
    "expedition_id": 2309,
    "destination": "Abandoned Fortress",
    "status": "Completed",
    "survival_rate": 50.00,
    "artifacts_value": 56000,
    "discovered_sites": 4,
    "encounter_success_rate": 42.86,
    "skill_improvement": 23,
    "expedition_duration": 62,
    "overall_success_score": 0.63,
    "related_entities": {
      "member_ids": [106, 109, 111, 119, 124, 125],
      "artifact_ids": [2515, 2516, 2517, 2518, 2519],
      "site_ids": [2420, 2421, 2422, 2423]
    }
  }
]
```

```sql
WITH survival_stats AS (
    SELECT
        e.expedition_id,
        COUNT(*) AS total_count,
        COUNT(*) FILTER (WHERE em.survived) AS survived_count,
        ROUND(
            survived_count * 1.0 / NULLIF(total_count, 0) * 100,
            2
        ) AS survival_rate
    FROM expeditions e
    LEFT JOIN expedition_members em ON e.expedition_id = em.expedition_id
    GROUP BY e.expedition_id
),
artifacts_value AS (
    SELECT
        ea.expedition_id,
        SUM(ea.value) AS total_value
    FROM expedition_artifacts ea
    GROUP BY ea.expedition_id
),
discovered_sites AS (
    SELECT
        es.expedition_id,
        COUNT(DISTINCT es.site_id) AS discovered_sites_count
    FROM expedition_sites es
    GROUP BY es.expedition_id
),
encounter_success_rate AS (
    SELECT
        ec.expedition_id,
        ROUND(
            COUNT(*) FILTER (WHERE ec.outcome = TRUE) * 100.0 / NULLIF(COUNT(*), 0),
            2
        ) AS encounter_success_rate
    FROM expedition_creatures ec
    GROUP BY ec.expedition_id
),
skills_before_expedition AS (
    SELECT
        em.expedition_id,
        em.dwarf_id,
        ds.skill_id,
        ds.experience AS experience_before
    FROM expedition_members em
    JOIN dwarf_skills ds ON em.dwarf_id = ds.dwarf_id
    JOIN expeditions e ON em.expedition_id = e.expedition_id
    WHERE ds.date = (
        SELECT MAX(date)
        FROM dwarf_skills
        WHERE dwarf_id = em.dwarf_id
        AND date < e.departure_date
    )
),
skills_after_expedition AS (
    SELECT
        em.expedition_id,
        em.dwarf_id,
        ds.skill_id,
        ds.experience AS experience_after
    FROM expedition_members em
    JOIN dwarf_skills ds ON em.dwarf_id = ds.dwarf_id
    JOIN expeditions e ON em.expedition_id = e.expedition_id
    WHERE ds.date = (
        SELECT MAX(date)
        FROM dwarf_skills
        WHERE dwarf_id = em.dwarf_id
        AND date > e.departure_date
    )
),
experience_gain AS (
    SELECT
        be.expedition_id,
        SUM(
            CASE
                WHEN ae.experience_after > be.experience_before THEN ae.experience_after - be.experience_before
                ELSE 0
            END
        ) AS total_experience_gain
    FROM skills_before_expedition be
    LEFT JOIN skills_after_expedition ae
        ON be.expedition_id = ae.expedition_id
        AND be.dwarf_id = ae.dwarf_id
    GROUP BY be.expedition_id
)

SELECT
    e.expedition_id,
    e.destination,
    e.status,
    ss.survival_rate,
    av.total_value AS artifacts_value,
    ds.discovered_sites_count AS discovered_sites,
    esr.encounter_success_rate AS encounter_success_rate,
    eg.total_experience_gain AS skill_improvement,
    DATEDIFF(e.return_date, e.departure_date) AS expedition_duration,
    ROUND((ss.survival_rate + esr.encounter_success_rate) / 2, 2) AS overall_success_score,
    JSON_OBJECT(
        'member_ids', (
            SELECT JSON_ARRAYAGG(em.dwarf_id)
            FROM expedition_members em
            WHERE e.expedition_id = em.expedition_id
        ),
        'artifact_ids', (
            SELECT JSON_ARRAYAGG(ea.artifact_id)
            FROM expedition_artifacts ea
            WHERE e.expedition_id = ea.expedition_id
        ),
        'site_ids', (
            SELECT JSON_ARRAYAGG(es.site_id)
            FROM expedition_sites es
            WHERE e.expedition_id = es.expedition_id
        )
    ) AS related_entities
FROM expeditions e
LEFT JOIN survival_stats ss ON ss.expedition_id = e.expedition_id
LEFT JOIN artifacts_value av ON av.expedition_id = e.expedition_id
LEFT JOIN discovered_sites ds ON ds.expedition_id = e.expedition_id
LEFT JOIN encounter_success_rate esr ON esr.expedition_id = e.expedition_id
LEFT JOIN experience_gain eg ON eg.expedition_id = e.expedition_id
```
