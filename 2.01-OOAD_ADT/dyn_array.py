import ctypes


class DynArray:
    INSERT_OK = 1  # значение успешно вставлено по указанному индексу
    INSERT_ERR = 2  # индекс находится за пределами массива

    REMOVE_OK = 1  # значение успешно удалено по указанному индексу
    REMOVE_ERR = 2  # индекс находится за пределами массива

    GET_OK = 1  # значение успешно получено
    GET_ERR = 2  # индекс находится за пределами массива

    INDEX_OK = 1  # элемент с указанным значением успешно найден
    INDEX_ERR = 2  # элемент с указанным значением не найден

    def __init__(self, capacity=16):
        self.count = 0
        self.array_capacity = capacity
        self.array = self.__make_array(self.array_capacity)

        self.insert_status = self.INSERT_ERR
        self.remove_status = self.REMOVE_ERR
        self.get_status = self.GET_ERR
        self.index_status = self.INDEX_ERR

    # Команды

    # Постусловие: в конец массива добавлено указанное значение
    def append(self, value) -> None:
        if self.count == self.array_capacity:
            new_capacity = self.array_capacity * 2
            self.__resize(new_capacity)

        self.array[self.count] = value
        self.count += 1

        return None

    # Предусловие: индекс находится в пределах массива
    # Постусловие: по указанному индексу добавлено новое значение, старый и все последующие
    # элементы сдвинуты вправо
    def insert(self, index, value) -> None:
        # Проверяем, что индекс находится в пределах массива
        if index < 0 or index > self.count:
            self.insert_status = self.INSERT_ERR
            return None

        # Если индекс указывает на конец массива, то просто делаем вставку в конец
        if index == self.count:
            self.append(value)
            self.insert_status = self.INSERT_OK
            return None

        # Если в массиве есть свободное место, то смещаем вперёд все элементы после индекса для вставки
        # и добавляем по указанному индексу новое значение
        if self.count < self.array_capacity:
            for i in range(self.count, index, -1):  # итерируем в обратном порядке с конца до индекса
                self.array[index] = self.array[i - 1]
            self.array[index] = value

            self.count += 1
            self.insert_status = self.INSERT_OK
            return None

        # Если в массиве нет свободного места, то увеличиваем массив, смещаем вперёд все элементы после индекса
        # для вставки и добавляем по указанному индексу новое значение
        new_capacity = 2 * self.array_capacity
        new_array = self.__make_array(new_capacity)

        # Копируем все элементы до индекса для вставки
        for index in range(index):
            new_array[index] = self.array[index]

        # Добавляем по указанному индексу новое значение
        new_array[index] = value

        # Все элементы после индекса для вставки смещаем вперёд
        for index in range(index, self.count):
            new_array[index + 1] = self.array[index]

        self.array = new_array
        self.array_capacity = new_capacity
        self.count += 1
        self.insert_status = self.INSERT_OK
        return None

    # Предусловие: индекс находится в пределах массива
    # Постусловие: элемент по указанному индексу удалён, все последующие элементы сдвинуты влево
    # Массив уменьшается в 1.5 раза, если занимает менее 50%
    def remove(self, index) -> None:
        # Проверяем, что индекс находится в пределах массива
        if index < 0 or index >= self.count:
            self.insert_status = self.REMOVE_ERR
            return None

        # Удаляем элемент по индексу и смещаем все элементы после индекса влево
        self.array[index] = None
        self.count -= 1
        for i in range(index + 1, self.count):
            self.array[i - 1] = self.array[i]

        # Уменьшаем массив, если он занимает менее половины
        # Минимальный размер массива 16
        if self.count < (self.array_capacity * 0.5) and (self.array_capacity > 16):
            new_capacity = int(self.array_capacity / 1.5)
            if new_capacity < 16:
                new_capacity = 16

            new_array = self.__make_array(new_capacity)
            for index in range(self.count):
                new_array[index] = self.array[index]
            self.array = new_array
            self.array_capacity = new_capacity

        self.remove_status = self.REMOVE_OK
        return None

    # Постусловие: массив очищен
    def clear(self, capacity=16) -> None:
        self.count = 0
        self.array_capacity = capacity
        self.array = self.__make_array(self.array_capacity)

        self.insert_status = self.INSERT_ERR
        self.remove_status = self.REMOVE_ERR
        self.get_status = self.GET_ERR
        self.index_status = self.INDEX_ERR

        return None

    def __make_array(self, new_capacity) -> list:
        return (new_capacity * ctypes.py_object)()

    def __resize(self, new_capacity) -> None:
        new_array = self.__make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.array_capacity = new_capacity

        return None

    # Запросы

    # Предусловие: индекс находится в пределах массива
    def get(self, index):
        if index < 0 or index >= self.count:
            self.get_status = self.GET_ERR
            return None

        result = self.array[index]
        self.get_status = self.GET_OK
        return result

    # Находит индекс первого элемента с указанным значением
    def index(self, value) -> int:
        for index in range(self.count):
            if self.array[index] == value:
                self.index_status = self.INDEX_OK
                return index

        self.index_status = self.INDEX_ERR
        return 0

    def size(self) -> int:
        return self.count

    def capacity(self) -> int:
        return self.array_capacity

    # Статусы

    def get_insert_status(self) -> int:
        return self.insert_status

    def get_remove_status(self) -> int:
        return self.remove_status

    def get_get_status(self) -> int:
        return self.get_status

    def get_index_status(self) -> int:
        return self.index_status
