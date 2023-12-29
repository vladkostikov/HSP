class NativeDictionary:
    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size
        self.values = [None] * self.size

    # Вычисляет индекс слота по входному значению.
    # В качестве value поступают строки.
    def hash_fun(self, key):
        slot = 0
        for char in key:
            slot += self.size + ord(char)
            slot *= ord(char)
        return slot % self.size

    # Возвращает True, если ключ имеется, иначе False.
    def is_key(self, key) -> bool:
        slot = self.find(key)
        if slot is None:
            return False
        return True

    # Гарантированно записывает значение value по ключу key.
    def put(self, key, value):
        # Если ключ уже существует.
        slot = self.find(key)
        if slot is not None:
            self.slots[slot] = key
            self.values[slot] = value
            return slot

        # Если ключ ещё не существует.
        slot = self.hash_fun(key)
        for _i in range(self.size):
            if self.slots[slot] is None:
                break
            slot += 7
            slot = slot % self.size
        self.slots[slot] = key
        self.values[slot] = value
        return slot

    # Возвращает value для key.
    # Или None если ключ не найден.
    def get(self, key):
        slot = self.find(key)
        if slot is None:
            return None
        return self.values[slot]

    # Находит индекс слота с ключом.
    # Возращает None, если не удаётся найти.
    def find(self, key):
        slot = self.hash_fun(key)
        for _i in range(self.size):
            if self.slots[slot] == key:
                return slot
            slot += 7
            slot = slot % self.size
        return None
