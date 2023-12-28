class HashTable:
    def __init__(self, size, step):
        self.size = size
        self.step = step
        self.slots = [None] * self.size

    # Вычисляет индекс слота по входному значению.
    # В качестве value поступают строки.
    def hash_fun(self, value):
        slot = 0
        for char in value:
            slot += (self.step + ord(char)) * ord(char)
        return slot % self.size

    # Находит индекс пустого слота для значения.
    # Сначала рассчитывает индекс хэш-функцией, а затем отыскивает подходящий слот
    # для него с учётом коллизий.
    # Возвращает None, если не удаётся найти подходящий слот.
    def seek_slot(self, value):
        slot = self.hash_fun(value)
        for _i in range(self.size):
            if self.slots[slot] is None:
                return slot
            slot += self.step
            slot = slot % self.size
        return None

    # Записывает значение в слот по хэш-функции.
    # Возвращает индекс слота или None, если из-за коллизий элемент не удаётся разместить.
    def put(self, value):
        slot = self.seek_slot(value)
        if slot is None:
            return None

        self.slots[slot] = value
        return slot

    # Находит индекс слота со значением.
    # Возращает None, если не удаётся найти.
    def find(self, value):
        slot = self.hash_fun(value)
        for _i in range(self.size):
            print(slot)
            if self.slots[slot] == value:
                return slot
            slot += self.step
            slot = slot % self.size
        return None
