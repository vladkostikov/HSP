class HashTable:
    def __init__(self, size: int, step: int):
        self.length = size
        self.step = step
        self.slots = [None] * self.length

    # Вычисляет индекс слота по входному значению.
    # В качестве value поступают строки.
    def hash_fun(self, value):
        slot = 0
        for char in str(value):
            slot += self.length + ord(char)
            slot *= ord(char)
        return slot % self.length

    # Находит индекс слота со значением.
    # Возращает None, если не удаётся найти.
    def find(self, value):
        slot = self.hash_fun(value)
        for _i in range(self.length):
            if self.slots[slot] == value:
                return slot
            slot += self.step
            slot = slot % self.length
        return None


class PowerSet(HashTable):
    def __init__(self):
        super().__init__(17, 3)

    # Возвращает количество элементов множества.
    def size(self):
        counter = 0
        for value in self.slots:
            if value is not None:
                counter += 1
        return counter

    # Возвращает слот для вставки значения.
    # Либо слот в котором уже находится это значение.
    def seek_slot(self, value):
        slot = self.hash_fun(value)
        for _i in range(self.length):
            if (self.slots[slot] == value) or (self.slots[slot] is None):
                return slot
            slot += self.step
            slot = slot % self.length
        return None

    # Записывает значение в слот по хэш-функции.
    # Увеличивает массив слотов при необходимости.
    def put(self, value):
        slot = self.seek_slot(value)
        if slot is not None:
            self.slots[slot] = value
            return self.slots[slot]

        # Увеличиваем массив слотов в 2 раза.
        old_slots = self.slots
        self.length *= 2
        self.slots = [None] * self.length
        for slot in old_slots:
            self.put(slot)

        return self.put(value)

    # Проверяет наличие значения в множестве.
    def get(self, value):
        slot = self.find(value)
        if slot is not None:
            return True
        return False

    # Удаляет значение из множества.
    def remove(self, value):
        slot = self.find(value)
        if slot is not None:
            self.slots[slot] = None
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
            if value is None:
                continue
            if set2.get(value) is False:
                difference_set.put(value)
        return difference_set

    # Проверяет является ли второе множество подмножеством первого.
    def issubset(self, set2):
        for value in set2.slots:
            if value is None:
                continue
            if self.get(value) is False:
                return False
        return True
