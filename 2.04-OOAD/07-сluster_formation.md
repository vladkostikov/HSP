# Формирование кластеров

Объединяем классы как модули в логические группы:

- GameFieldCluster - содержит классы, отвечающие за игровое поле: Map, Cell, Element.
- FactoryCluster - отвечает за создание элементов на игровом поле: ElementFactory.
- BonusSystemCluster - управляет бонусами и их логикой: Bonus, BonusManager.
- StatisticsCluster - собирает данные и метрики в процессе игры: Statistics.
