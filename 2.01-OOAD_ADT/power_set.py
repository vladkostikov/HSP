class HashTable:
    PUT_OK = 1  # в таблицу успешно добавлено указанное значение
    PUT_ERR = 2  # таблица полная
    PUT_EXIST = 3  # значение уже существует в таблице

    REMOVE_OK = 1  # из таблицы успешно удалено указанное значение
    REMOVE_ERR = 2  # значение не найдено

    def __init__(self, size: int):
        if size < 1:
            size = 1

        self._storage = [None] * size
        self.__size = size
        self.__step = 3

        self.__put_status = self.PUT_ERR
        self.__remove_status = self.REMOVE_ERR

    # Команды

    # Предусловие: таблица не полная и такое значение ещё не добавлялось
    # Постусловие: в таблицу успешно добавлено указанное значение
    def put(self, value: str) -> None:
        start_index = self.__hash_fun__(value)
        index = start_index
        lap = 0
        while self._storage[index] is not None:
            if self._storage[index] == value:
                self.__put_status = self.PUT_EXIST
                return None

            if index == start_index and lap > 0:
                self.__put_status = self.PUT_ERR
                return None

            index += self.__step
            if index >= self.__size:
                index %= self.__size
                lap += 1

        self._storage[index] = value
        self.__put_status = self.PUT_OK
        return None

    # Предусловие: значение содержится в таблице
    # Постусловие: из таблицы удалено указанное значение
    def remove(self, value: str) -> None:
        start_index = self.__hash_fun__(value)
        index = start_index
        lap = 0
        while self._storage[index] is not None:
            if self._storage[index] == value:
                self._storage[index] = None
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

    # Содержит ли таблица указанное значение
    def get(self, value: str) -> bool:
        start_index = self.__hash_fun__(value)
        index = start_index
        lap = 0
        while self._storage[index] != value:
            if index == start_index and lap > 0:
                return False

            index += self.__step
            if index >= self.__size:
                index %= self.__size
                lap += 1

        return True

    def size(self) -> int:
        counter = 0
        for el in self._storage:
            if el is not None:
                counter += 1
        return counter

    # Статусы

    def get_put_status(self) -> int:
        return self.__put_status

    def get_remove_status(self) -> int:
        return self.__remove_status

    # Рассчитывает индекс для указанного значения
    def __hash_fun__(self, value: str) -> int:
        index = 0
        for i, char in enumerate(value):
            index += (ord(char) + (i + 1)) * (i + 1)
        return index % self.__size


class PowerSet(HashTable):
    def __init__(self, size: int):
        super().__init__(size)

    def intersection(self, second_set: "PowerSet") -> "PowerSet":
        intersection_set = PowerSet(self.size())
        for el in self._storage:
            if el is not None and second_set.get(el):
                intersection_set.put(el)
        return intersection_set

    def union(self, second_set: "PowerSet") -> "PowerSet":
        union_set = PowerSet(self.size() + second_set.size())
        for el in self._storage:
            if el is not None:
                union_set.put(el)
        for el in second_set._storage:
            if el is not None:
                union_set.put(el)
        return union_set

    def difference(self, second_set: "PowerSet") -> "PowerSet":
        difference_set = PowerSet(self.size())
        for el in self._storage:
            if el is not None and not second_set.get(el):
                difference_set.put(el)
        return difference_set

    def issubset(self, second_set: "PowerSet") -> bool:
        for el in second_set._storage:
            if el is not None and not self.get(el):
                return False
        return True

    def equals(self, second_set: "PowerSet") -> bool:
        if self.size() != second_set.size():
            return False

        for el in self._storage:
            if el is not None and not second_set.get(el):
                return False

        return True
