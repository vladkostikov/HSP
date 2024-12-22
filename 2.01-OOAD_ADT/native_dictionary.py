class NativeDictionary:
    PUT_OK = 1  # в словарь записано новое значение по указанному ключу
    PUT_ERR = 2  # нет свободного места для вставки

    REMOVE_OK = 1  # из словаря удален указанный ключ
    REMOVE_ERR = 2  # в словаре не найден указанный ключ

    GET_OK = 1  # найдено значение по указанному ключу
    GET_ERR = 2  # ключ в словаре не найден

    def __init__(self, size: int):
        self.__size = size
        self.__keys = [None] * self.__size
        self.__values = [None] * self.__size
        self.__step = 3

        self.__put_status = self.PUT_ERR
        self.__get_status = self.GET_ERR
        self.__remove_status = self.REMOVE_ERR

    # Команды

    # Предусловие: в словаре имеется свободное место для ключа
    # Постусловие: по указанному ключу записано новое значение
    def put(self, key: str, value) -> None:
        start_index = self.__hash_fun__(key)
        index = start_index
        lap = 0
        while self.__keys[index] is not None:
            if self.__keys[index] == key:
                self.__values[index] = value
                self.__put_status = self.PUT_OK
                return None

            if index == start_index and lap > 0:
                self.__put_status = self.PUT_ERR
                return None

            index += self.__step
            if index >= self.__size:
                index %= self.__size
                lap += 1

        self.__keys[index] = key
        self.__values[index] = value
        self.__put_status = self.PUT_OK
        return None

    # Предусловие: в словаре имеется указанный ключ
    # Постусловие: из словаря удален указанный ключ
    def remove(self, key: str) -> None:
        start_index = self.__hash_fun__(key)
        index = start_index
        lap = 0
        while self.__keys[index] is not None:
            if self.__keys[index] == key:
                self.__keys[index] = None
                self.__values[index] = None
                self.__remove_status = self.REMOVE_OK
                return None

            if index == start_index and lap > 0:
                self.__remove_status = self.REMOVE_ERR
                return None

            index += self.__step
            if index >= self.__size:
                index %= self.__size
                lap += 1

        self.__remove_status = self.REMOVE_ERR
        return None

    # Запросы

    def is_key(self, key: str) -> bool:
        start_index = self.__hash_fun__(key)
        index = start_index
        lap = 0
        while self.__keys[index] != key:
            if index == start_index and lap > 0:
                return False

            index += self.__step
            if index >= self.__size:
                index %= self.__size
                lap += 1

        return True

    # Предусловие: в словаре имеется указанный ключ
    def get(self, key: str):
        start_index = self.__hash_fun__(key)
        index = start_index
        lap = 0
        while self.__keys[index] != key:
            if index == start_index and lap > 0:
                self.__get_status = self.GET_ERR
                return None

            index += self.__step
            if index >= self.__size:
                index %= self.__size
                lap += 1

        self.__get_status = self.GET_OK
        return self.__values[index]

    # Статусы

    def get_put_status(self) -> int:
        return self.__put_status

    def get_get_status(self) -> int:
        return self.__get_status

    def get_remove_status(self) -> int:
        return self.__remove_status

    # Рассчитывает индекс для указанного значения
    def __hash_fun__(self, value: str) -> int:
        index = 0
        for i, char in enumerate(value):
            index += (ord(char) + (i + 1)) * (i + 1)
        return index % self.__size
