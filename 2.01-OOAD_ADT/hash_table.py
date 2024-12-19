class HashTable:
    PUT_OK = 1  # в таблицу успешно добавлено указанное значение
    PUT_ERR = 2  # таблица полная
    PUT_EXIST = 3  # значение уже существует в таблице

    SEEK_SLOT_OK = 1  # индекс для вставки указанного значения найден
    SEEK_SLOT_ERR = 2  # таблица полная
    SEEK_SLOT_EXIST = 3  # значение уже существует в таблице

    def __init__(self, max_size: int):
        self.storage = [None] * max_size
        self.step = 3

        self.put_status = self.PUT_ERR
        self.seek_slot_status = self.SEEK_SLOT_ERR

    # Команды

    # Предусловие: таблица не полная и такое значение ещё не добавлялось
    # Постусловие: в таблицу успешно добавлено указанное значение
    def put(self, value: str) -> None:
        index = self.seek_slot(value)
        if self.seek_slot_status == self.SEEK_SLOT_ERR:
            self.put_status = self.PUT_ERR
            return None
        if self.seek_slot_status == self.SEEK_SLOT_EXIST:
            self.put_status = self.PUT_EXIST
            return None

        self.storage[index] = value
        self.put_status = self.PUT_OK
        return None

    # Запросы

    # Содержит ли таблица указанное значение
    def find(self, value: str) -> bool:
        start_index = self.hash_fun(value)
        index = start_index
        lap = 0
        while self.storage[index] != value:
            if index == start_index and lap > 0:
                return False

            index += self.step
            if index >= len(self.storage):
                index %= len(self.storage)
                lap += 1

        return True

    # Рассчитывает индекс для указанного значения
    def hash_fun(self, value: str) -> int:
        index = 0
        for i, char in enumerate(value):
            index += (ord(char) + (i + 1)) * (i + 1)
        return index % len(self.storage)

    # Находит индекс для вставки указанного значения с учётом коллизий
    # Предусловие: таблица не полная и такое значение ещё не добавлялось
    def seek_slot(self, value: str) -> int:
        start_index = self.hash_fun(value)
        index = start_index
        lap = 0
        while self.storage[index] is not None:
            if self.storage[index] == value:
                self.seek_slot_status = self.SEEK_SLOT_EXIST
                return index

            if index == start_index and lap > 0:
                self.seek_slot_status = self.SEEK_SLOT_ERR
                return index

            index += self.step
            if index >= len(self.storage):
                index %= len(self.storage)
                lap += 1

        self.seek_slot_status = self.SEEK_SLOT_OK
        return index

    # Статусы

    def get_put_status(self) -> int:
        return self.put_status

    def get_seek_slot_status(self) -> int:
        return self.seek_slot_status
