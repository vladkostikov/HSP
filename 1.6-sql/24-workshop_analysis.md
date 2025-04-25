# Задача 2. Комплексный анализ эффективности производства

### Разработайте запрос, который анализирует эффективность каждой мастерской, учитывая:
- Производительность каждого ремесленника (соотношение созданных продуктов к затраченному времени)
- Эффективность использования ресурсов (соотношение потребляемых ресурсов к производимым товарам)
- Качество производимых товаров (средневзвешенное по ценности)
- Время простоя мастерской
- Влияние навыков ремесленников на качество товаров

Возможный вариант выдачи:
```json
[
  {
    "workshop_id": 301,
    "workshop_name": "Royal Forge",
    "workshop_type": "Smithy",
    "num_craftsdwarves": 4,
    "total_quantity_produced": 256,
    "total_production_value": 187500,
    "daily_production_rate": 3.41,
    "value_per_material_unit": 7.82,
    "workshop_utilization_percent": 85.33,
    "material_conversion_ratio": 1.56,
    "average_craftsdwarf_skill": 7.25,
    "skill_quality_correlation": 0.83,
    "related_entities": {
      "craftsdwarf_ids": [101, 103, 108, 115],
      "product_ids": [801, 802, 803, 804, 805, 806],
      "material_ids": [201, 204, 208, 210],
      "project_ids": [701, 702, 703]
    }
  },
  {
    "workshop_id": 304,
    "workshop_name": "Gemcutter's Studio",
    "workshop_type": "Jewelcrafting",
    "num_craftsdwarves": 2,
    "total_quantity_produced": 128,
    "total_production_value": 205000,
    "daily_production_rate": 2.56,
    "value_per_material_unit": 13.67,
    "workshop_utilization_percent": 78.95,
    "material_conversion_ratio": 0.85,
    "average_craftsdwarf_skill": 8.50,
    "skill_quality_correlation": 0.92,
    "related_entities": {
      "craftsdwarf_ids": [105, 112],
      "product_ids": [820, 821, 822, 823, 824],
      "material_ids": [206, 213, 217, 220],
      "project_ids": [705, 708]
    }
  }
]
```

```sql
WITH avg_production AS (
    SELECT
        wp.workshop_id,
        AVG(wp.daily_total) AS daily_production_rate
    FROM (
        SELECT
            wp.workshop_id,
            wp.production_date,
            SUM(quantity) AS daily_total
        FROM workshop_products wp
        GROUP BY wp.workshop_id, wp.production_date
    ) AS daily_summary
    GROUP BY wp.workshop_id
),
workers_and_products AS (
    SELECT
        wc.workshop_id,
        COUNT(DISTINCT wc.dwarf_id) AS num_craftsdwarves,
        AVG(dwarfs_avg_skill.avg_level) AS average_craftsdwarf_skill,
        CORR(dwarfs_avg_skill.avg_level, p.quality) AS skill_quality_correlation,
        COUNT(DISTINCT p.product_id) AS total_quantity_produced,
        SUM(p.value) AS total_production_value,
        avg_p.daily_production_rate
    FROM (
        SELECT
            ds.dwarf_id,
            AVG(ds.level) AS avg_level
        FROM dwarf_skills ds
        JOIN skills s ON ds.skill_id = s.skill_id
        WHERE s.skill_type = 'craft'
        GROUP BY ds.dwarf_id
    ) AS dwarfs_avg_skill
    JOIN workshop_craftsdwarves wc ON dwarfs_avg_skill.dwarf_id = wc.dwarf_id
    JOIN products p ON wc.workshop_id = p.workshop_id
    JOIN avg_production avg_p ON p.workshop_id = avg_p.workshop_id
    GROUP BY wc.workshop_id
),
materials_and_utilization AS (
    SELECT
        wm.workshop_id,
        SUM(p.value) / NULLIF(SUM(wm.quantity), 0) AS value_per_material_unit,
        (COUNT(DISTINCT wp.production_date) * 100.0) /
        (EXTRACT(DAY FROM MAX(wp.production_date) - MIN(wp.production_date)) + 1) AS workshop_utilization_percent,
        SUM(wm.quantity) / NULLIF(SUM(wp.quantity), 0) AS material_conversion_ratio
    FROM workshop_materials wm
    JOIN products p ON wm.material_id = p.material_id
        AND wm.workshop_id = p.workshop_id
    LEFT JOIN workshop_products wp ON wm.workshop_id = wp.workshop_id
    GROUP BY wm.workshop_id;
)

SELECT
    w.workshop_id,
    w.name AS workshop_name,
    w.type AS workshop_type,
    wp.num_craftsdwarves,
    wp.total_quantity_produced,
    wp.total_production_value,
    wp.daily_production_rate,
    mu.value_per_material_unit,
    mu.workshop_utilization_percent,
    mu.material_conversion_ratio,
    wp.average_craftsdwarf_skill,
    wp.skill_quality_correlation,
    JSON_OBJECT(
        'craftsdwarf_ids', (
            SELECT JSON_ARRAYAGG(wc.dwarf_id)
            FROM workshop_craftsdwarves wc
            WHERE w.workshop_id = wc.workshop_id
        ),
        'product_ids', (
            SELECT JSON_ARRAYAGG(p.product_id)
            FROM products p
            WHERE w.workshop_id = p.workshop_id
        ),
        'material_ids', (
            SELECT JSON_ARRAYAGG(wm.material_id)
            FROM workshop_materials wm
            WHERE w.workshop_id = wm.workshop_id
        ),
        'project_ids', (
            SELECT JSON_ARRAYAGG(p.project_id)
            FROM projects p
            WHERE w.workshop_id = p.workshop_id
        )
    ) AS related_entities
FROM workshops w
LEFT JOIN workers_and_products wp ON w.workshop_id = wp.workshop_id
LEFT JOIN materials_and_utilization mu ON w.workshop_id = mu.workshop_id
ORDER BY w.workshop_id
```
