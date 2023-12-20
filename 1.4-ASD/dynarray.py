import ctypes


# Динамический массив.
class DynArray:

    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        self.array[self.count] = itm
        self.count += 1

    # Сложность:
    # В худшем случае O(n), когда вставка производится в начало массива или требуется увеличение размера массива.
    # В среднем o(n/2) ~= o(n), когда вставка производится в середину массива.
    # В лучшем случае Ω(1), когда вставка производится в конец массива.
    # Где n - длина массива.
    def insert(self, i, itm):
        if i < 0 or i > self.count:
            raise IndexError('Index is out of bounds')

        # Если в массиве есть свободное место, то смещаем вперёд все элементы после индекса для вставки.
        if self.count < self.capacity:
            for index in range(self.count, i, -1):
                self.array[index] = self.array[index - 1]
            self.array[i] = itm

        # Если места нет, то создаём новый массив.
        else:
            new_capacity = 2 * self.capacity
            new_array = self.make_array(new_capacity)

            # Копируем все элементы до индекса для вставки.
            for index in range(i):
                new_array[index] = self.array[index]
            new_array[i] = itm

            # А все элементы после индекса для вставки смещаем вперёд.
            for index in range(i, self.count):
                new_array[index + 1] = self.array[i]
            self.array = new_array
            self.capacity = new_capacity
        self.count += 1

    # Сложность:
    # В худшем случае O(n), когда удаляется элемент в начале массива или требуется уменьшение размера массива.
    # В среднем o(n/2) ~= o(n), когда удаляется элемент в середине массива.
    # В лучшем случае Ω(1), когда удаляется последний элемент массива.
    # Где n - длина массива.
    def delete(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')

        # Рассчитываем новый размер массива, если его нужно будет уменьшить.
        # Минимальный размер массива 16.
        new_capacity = int(self.capacity / 1.5)
        if new_capacity < 16:
            new_capacity = 16

        # Если массив после удаления займёт меньше 50%, то уменьшаем его в 1.5 раза.
        # Минимальный размер массива 16.
        if (self.count - 1) < (self.capacity * 0.5) and (new_capacity >= 16) and (self.capacity != 16):
            new_array = self.make_array(new_capacity)

            # Копируем все элементы до индекса для удаления.
            for index in range(i):
                new_array[index] = self.array[index]

            # Копируем все элементы после индекса для удаления.
            for index in range(i + 1, self.count):
                new_array[index] = self.array[index - 1]
            self.array = new_array
            self.capacity = new_capacity
        # Если массив уменьшать не нужно, то смещаем назад все элементы после индекса для удаления.
        else:
            for index in range(i + 1, self.count):
                self.array[index - 1] = self.array[index]
        self.count -= 1
