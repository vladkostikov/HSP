class NativeCache:
    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size

    # Вычисляет индекс слота по входному значению.
    # В качестве key поступают строки.
    def hash_fun(self, key: str):
        slot = 0
        for char in key:
            slot += self.size + ord(char)
            slot *= ord(char)
        return slot % self.size

    # Возвращает True, если ключ имеется, иначе False.
    def is_key(self, key: str) -> bool:
        slot = self.find(key)
        if slot is None:
            return False
        return True

    # Гарантированно записывает значение value по ключу key.
    # Если ключ уже существует, то перезаписывает значение и количество обращений.
    def put(self, key: str, value):
        slot = self.find(key)
        if slot is None:
            slot = self.find_slot_to_insert(key)
        self.slots[slot] = key
        self.values[slot] = value
        self.hits[slot] = 0
        return slot

    # Возвращает value для key.
    # Или None если ключ не найден.
    def get(self, key: str):
        slot = self.find(key)
        if slot is None:
            return None
        return self.values[slot]

    # Находит индекс слота с ключом.
    # Возращает None, если не удаётся найти.
    def find(self, key: str):
        slot = self.hash_fun(key)
        for _i in range(self.size):
            if self.slots[slot] == key:
                self.record_request(slot)
                return slot
            slot += 7
            slot = slot % self.size
        return None

    # Фиксирует обращение к ключу.
    def record_request(self, slot: int):
        self.hits[slot] += 1

    # Находит слот для вставки.
    def find_slot_to_insert(self, key: str) -> int:
        slot = self.hash_fun(key)
        slot_with_minimum_queries = slot
        for _i in range(self.size):
            # Ищем свободный слот.
            if self.slots[slot] is None:
                return slot

            # Если свободного слота не находим, то ищем и возвращаем слот с минимальным количеством обращений.
            if self.hits[slot] < self.hits[slot_with_minimum_queries]:
                slot_with_minimum_queries = slot
            slot += 7
            slot = slot % self.size
        return slot_with_minimum_queries
