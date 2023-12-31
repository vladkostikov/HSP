class PowerSet:
    def __init__(self):
        self.slots = {}

    # Возвращает количество элементов множества.
    def size(self):
        return len(self.slots)

    # Вставка значения в множество.
    def put(self, value):
        self.slots[value] = True
        return value

    # Проверяет наличие значения в множестве.
    def get(self, value) -> bool:
        return value in self.slots

    # Удаляет значение из множества.
    def remove(self, value) -> bool:
        if self.get(value):
            del self.slots[value]
            return True
        return False

    # Возвращает пересечение двух множеств.
    def intersection(self, set2):
        intersection_set = PowerSet()
        for value in set2.slots:
            if value is None:
                continue
            if self.get(value):
                intersection_set.put(value)

        return intersection_set

    # Объединяет два множества.
    def union(self, set2):
        union_set = PowerSet()
        for value in self.slots:
            if value is None:
                continue
            union_set.put(value)

        for value in set2.slots:
            if value is None:
                continue
            union_set.put(value)

        return union_set

    # Вычитает второе множество из первого.
    def difference(self, set2):
        difference_set = PowerSet()
        for value in self.slots:
            if set2.get(value) is False:
                difference_set.put(value)
        return difference_set

    # Проверяет является ли второе множество подмножеством первого.
    def issubset(self, set2):
        for value in set2.slots:
            if self.get(value) is False:
                return False
        return True
