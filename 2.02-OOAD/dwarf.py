from typing import List


# Базовый класс для предметов.
class Item:
    def __init__(self, name: str, value: int):
        self.name: str = name
        self.value: int = value

    def use(self) -> str:
        raise NotImplementedError


# Класс для инструментов. Наследование.
class Tool(Item):
    def __init__(self, name: str, value: int, efficiency: int):
        super().__init__(name, value)
        self.efficiency: int = efficiency

    def use(self) -> str:  # Полиморфизм.
        return f"{self.name} увеличивает эффективность работы на {self.efficiency}%"


# Класс для оружия. Наследование.
class Weapon(Item):
    def __init__(self, name: str, value: int, damage: int):
        super().__init__(name, value)
        self.damage: int = damage

    def use(self) -> str:  # Полиморфизм.
        return f"{self.name} наносит {self.damage} единиц урона."


# Базовый класс для дварфов.
class Dwarf:
    def __init__(self, name: str, age: int):
        self.name: str = name
        self.age: int = age
        self.items: List[Item] = []  # Композиция.

    def add_item(self, item: Item) -> None:
        self.items.append(item)

    def list_items(self) -> List[str]:
        return [item.name for item in self.items]

    def perform_task(self) -> str:
        raise NotImplementedError


# Класс для дварфов-шахтеров. Наследование.
class Miner(Dwarf):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    def perform_task(self) -> str:  # Полиморфизм.
        return f"{self.name} копает руду!"


# Класс для дварфов-воинов. Наследование.
class Warrior(Dwarf):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    def perform_task(self) -> str:  # Полиморфизм.
        return f"{self.name} сражается с врагами!"
