# Задача 4. Комплексный анализ торговых отношений и их влияния на крепость

### Разработайте запрос, анализирующий торговые отношения со всеми цивилизациями, оценивая:
- Баланс торговли с каждой цивилизацией за все время
- Влияние товаров каждого типа на экономику крепости
- Корреляцию между торговлей и дипломатическими отношениями
- Эволюцию торговых отношений во времени
- Зависимость крепости от определенных импортируемых товаров
- Эффективность экспорта продукции мастерских

Возможный вариант выдачи:
```json
{
  "total_trading_partners": 5,
  "all_time_trade_value": 15850000,
  "all_time_trade_balance": 1250000,
  "civilization_data": {
    "civilization_trade_data": [
      {
        "civilization_type": "Human",
        "total_caravans": 42,
        "total_trade_value": 5240000,
        "trade_balance": 840000,
        "trade_relationship": "Favorable",
        "diplomatic_correlation": 0.78,
        "caravan_ids": [1301, 1305, 1308, 1312, 1315]
      },
      {
        "civilization_type": "Elven",
        "total_caravans": 38,
        "total_trade_value": 4620000,
        "trade_balance": -280000,
        "trade_relationship": "Unfavorable",
        "diplomatic_correlation": 0.42,
        "caravan_ids": [1302, 1306, 1309, 1316, 1322]
      }
    ]
  },
  "critical_import_dependencies": {
    "resource_dependency": [
      {
        "material_type": "Exotic Metals",
        "dependency_score": 2850.5,
        "total_imported": 5230,
        "import_diversity": 4,
        "resource_ids": [202, 208, 215]
      },
      {
        "material_type": "Lumber",
        "dependency_score": 1720.3,
        "total_imported": 12450,
        "import_diversity": 3,
        "resource_ids": [203, 209, 216]
      }
    ]
  },
  "export_effectiveness": {
    "export_effectiveness": [
      {
        "workshop_type": "Smithy",
        "product_type": "Weapons",
        "export_ratio": 78.5,
        "avg_markup": 1.85,
        "workshop_ids": [301, 305, 310]
      },
      {
        "workshop_type": "Jewelery",
        "product_type": "Ornaments",
        "export_ratio": 92.3,
        "avg_markup": 2.15,
        "workshop_ids": [304, 309, 315]
      }
    ]
  },
  "trade_timeline": {
    "trade_growth": [
      {
        "year": 205,
        "quarter": 1,
        "quarterly_value": 380000,
        "quarterly_balance": 20000,
        "trade_diversity": 3
      },
      {
        "year": 205,
        "quarter": 2,
        "quarterly_value": 420000,
        "quarterly_balance": 35000,
        "trade_diversity": 4
      }
    ]
  }
}
```

```sql
WITH trade_summary AS (
  SELECT
    COUNT(DISTINCT c.civilization_type) AS total_trading_partners,
    SUM(CASE WHEN g.type = 'Import' THEN g.value ELSE 0 END) +
    SUM(CASE WHEN g.type = 'Export' THEN g.value ELSE 0 END) AS all_time_trade_value,
    SUM(CASE WHEN g.type = 'Export' THEN g.value ELSE 0 END) -
    SUM(CASE WHEN g.type = 'Import' THEN g.value ELSE 0 END) AS all_time_trade_balance
  FROM caravans c
  JOIN caravan_goods g ON c.caravan_id = g.caravan_id
),
diplomatic_avg AS (
  SELECT
    caravan_id,
    AVG(relationship_change) AS avg_relationship_change
  FROM diplomatic_events
  GROUP BY caravan_id
),
diplomatic_corr AS (
  SELECT
    c.civilization_type,
    CORR(g.value, COALESCE(d.avg_relationship_change, 0)) AS diplomatic_correlation
  FROM caravans c
  JOIN caravan_goods g ON c.caravan_id = g.caravan_id
  LEFT JOIN diplomatic_avg d ON c.caravan_id = d.caravan_id
  GROUP BY c.civilization_type
),
civilization_trade_data AS (
  SELECT
    c.civilization_type,
    COUNT(DISTINCT c.caravan_id) AS total_caravans,
    SUM(g.value) AS total_trade_value,
    SUM(CASE WHEN g.type = 'Export' THEN g.value ELSE 0 END) -
    SUM(CASE WHEN g.type = 'Import' THEN g.value ELSE 0 END) AS trade_balance,
    CASE
      WHEN AVG(COALESCE(d.avg_relationship_change, 0)) >= 0 THEN 'Favorable'
      ELSE 'Unfavorable'
    END AS trade_relationship,
    dc.diplomatic_correlation,
    JSON_ARRAYAGG(DISTINCT c.caravan_id) AS caravan_ids
  FROM caravans c
  JOIN caravan_goods g ON c.caravan_id = g.caravan_id
  LEFT JOIN diplomatic_avg d ON c.caravan_id = d.caravan_id
  LEFT JOIN diplomatic_corr dc ON dc.civilization_type = c.civilization_type
  GROUP BY c.civilization_type, dc.diplomatic_correlation
),
resource_dependency AS (
  SELECT
    g.material_type,
    SUM(g.quantity) AS total_imported,
    COUNT(DISTINCT r.resource_id) AS import_diversity,
    SUM(g.quantity * COALESCE(g.price_fluctuation, 1)) AS dependency_score,
    JSON_ARRAYAGG(DISTINCT r.resource_id) AS resource_ids
  FROM caravan_goods g
  LEFT JOIN products p ON g.original_product_id = p.product_id
  LEFT JOIN resources r ON p.material_id = r.resource_id
  WHERE g.type = 'Import'
  GROUP BY g.material_type
),
product_exports AS (
  SELECT
    p.workshop_id,
    w.type AS workshop_type,
    p.type AS product_type,
    p.product_id,
    p.value AS original_value,
    (
      SELECT COALESCE(SUM(g.value), 0)
      FROM caravan_goods g
      WHERE g.original_product_id = p.product_id AND g.type = 'Export'
    ) AS exported_value
  FROM products p
  JOIN workshops w ON w.workshop_id = p.workshop_id
),
export_effectiveness AS (
  SELECT
    workshop_type,
    product_type,
    ROUND(SUM(exported_value) * 100.0 / NULLIF(SUM(original_value), 0), 2) AS export_ratio,
    ROUND(AVG(NULLIF(exported_value / NULLIF(original_value, 0), 0)), 2) AS avg_markup,
    JSON_ARRAYAGG(DISTINCT workshop_id) AS workshop_ids
  FROM product_exports
  GROUP BY workshop_type, product_type
),
trade_growth AS (
  SELECT
    EXTRACT(YEAR FROM c.arrival_date)::INT AS year,
    EXTRACT(QUARTER FROM c.arrival_date)::INT AS quarter,
    SUM(g.value) AS quarterly_value,
    SUM(CASE WHEN g.type = 'Export' THEN g.value ELSE 0 END) -
    SUM(CASE WHEN g.type = 'Import' THEN g.value ELSE 0 END) AS quarterly_balance,
    COUNT(DISTINCT g.material_type) AS trade_diversity
  FROM caravans c
  JOIN caravan_goods g ON c.caravan_id = g.caravan_id
  GROUP BY year, quarter
)

SELECT JSON_OBJECT(
  'total_trading_partners', (SELECT total_trading_partners FROM trade_summary),
  'all_time_trade_value', (SELECT all_time_trade_value FROM trade_summary),
  'all_time_trade_balance', (SELECT all_time_trade_balance FROM trade_summary),

  'civilization_data', JSON_OBJECT(
    'civilization_trade_data', (
      SELECT JSON_ARRAYAGG(
        JSON_OBJECT(
          'civilization_type', ctd.civilization_type,
          'total_caravans', ctd.total_caravans,
          'total_trade_value', ctd.total_trade_value,
          'trade_balance', ctd.trade_balance,
          'trade_relationship', ctd.trade_relationship,
          'diplomatic_correlation', ROUND(COALESCE(ctd.diplomatic_correlation, 0), 2),
          'caravan_ids', ctd.caravan_ids
        )
      )
      FROM civilization_trade_data ctd
    )
  ),

  'critical_import_dependencies', JSON_OBJECT(
    'resource_dependency', (
      SELECT JSON_ARRAYAGG(
        JSON_OBJECT(
          'material_type', rd.material_type,
          'dependency_score', ROUND(rd.dependency_score, 2),
          'total_imported', rd.total_imported,
          'import_diversity', rd.import_diversity,
          'resource_ids', rd.resource_ids
        )
      )
      FROM resource_dependency rd
    )
  ),

  'export_effectiveness', JSON_OBJECT(
    'export_effectiveness', (
      SELECT JSON_ARRAYAGG(
        JSON_OBJECT(
          'workshop_type', ee.workshop_type,
          'product_type', ee.product_type,
          'export_ratio', ee.export_ratio,
          'avg_markup', ee.avg_markup,
          'workshop_ids', ee.workshop_ids
        )
      )
      FROM export_effectiveness ee
    )
  ),

  'trade_timeline', JSON_OBJECT(
    'trade_growth', (
      SELECT JSON_ARRAYAGG(
        JSON_OBJECT(
          'year', tg.year,
          'quarter', tg.quarter,
          'quarterly_value', tg.quarterly_value,
          'quarterly_balance', tg.quarterly_balance,
          'trade_diversity', tg.trade_diversity
        )
      )
      FROM trade_growth tg
    )
  )
);
```
