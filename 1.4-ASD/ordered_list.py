class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    # -1 если new_value < old_value
    # 0 если new_value == old_value
    # +1 если new_value > old_value
    def compare(self, new_value, old_value) -> int:
        if new_value < old_value:
            return -1
        if new_value > old_value:
            return 1
        return 0

    # Автоматическая вставка value в нужную позицию.
    def add(self, value):
        new_node = Node(value)
        node = self.head

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return new_node.value

        while node is not None:
            comparison = self.compare(new_node.value, node.value)
            # Вставляем новый элемент перед текущим элементом если:
            # 1. порядок по возрастанию и новый элемент меньше или равен текущему элементу.
            # 2. порядок по убыванию и новый элемент больше или равен текущему элементу.
            if (self.__ascending and comparison in (-1, 0) or
                    (not self.__ascending and comparison in (1, 0))):
                new_node.prev = node.prev
                new_node.next = node

                # Проверяем что вставка происходит в начало списка.
                if node.prev is None:
                    self.head = new_node
                elif node.prev is not None:
                    node.prev.next = new_node

                node.prev = new_node
                return new_node.value
            node = node.next

        # Вставляем новый элемент в конец списка.
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        return new_node.value

    def find(self, value):
        # Если значение меньше, чем минимум или больше, чем максимум, то
        # нужное значение в списке отсутствует.
        if self.__ascending and (value < self.head.value or value > self.tail.value):
            return None

        if not self.__ascending and (value > self.head.value or value < self.tail.value):
            return None

        node = self.head
        while type(node) is Node:
            # Прерывание поиска если найден заведомо больший или меньший элемент, чем искомый.
            if self.__ascending and node.value > value:
                return None
            if not self.__ascending and node.value < value:
                return None

            if node.value == value:
                return node
            node = node.next
        return None

    def delete(self, value):
        node = self.find(value)
        if node is None:
            return None

        # Когда удаляем последний элемент.
        if self.head is self.tail:
            self.clean(self.__ascending)
            return node.value

        if node is self.head:
            node.next.prev = None
            self.head = node.next
        elif node is self.tail:
            node.prev.next = None
            self.tail = node.prev
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

        # Когда удаляем предпоследний элемент.
        if self.head == self.tail:
            self.head.next = self.tail
            self.tail.prev = self.head
        return node.value

    def clean(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def len(self):
        length = 0
        node = self.head
        while node is not None:
            length += 1
            node = node.next
        return length

    def get_all(self):
        result = []
        node = self.head
        while node is not None:
            result.append(node)
            node = node.next
        return result


class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    # Переопределённая версия для строк.
    def compare(self, new_value: str, old_value: str) -> int:
        stripped_new_value = new_value.strip()
        stripped_old_value = old_value.strip()
        if stripped_new_value < stripped_old_value:
            return -1
        if stripped_new_value > stripped_old_value:
            return 1
        return 0
