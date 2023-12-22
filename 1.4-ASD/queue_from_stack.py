class Queue:
    def __init__(self):
        self.data = Stack()

    # Вставка в конец очереди.
    # Сложность O(1), т.к. используем стек.
    def enqueue(self, item):
        return self.data.push(item)

    # Выдача из начала очереди.
    # Сложность O(2n), т.к. при использовании стека копируем все элементы
    # в дополнительный массив, а потом обратно.
    def dequeue(self):
        current_stack = self.data
        additional_stack = Stack()

        for _i in range(current_stack.size() - 1):
            additional_stack.push(current_stack.pop())
        deleted_value = current_stack.pop()

        for _i in range(additional_stack.size()):
            current_stack.push(additional_stack.pop())

        return deleted_value

    # Размер очереди.
    # Сложность O(1), т.к. длину храним в виде атрибута в связном списке.
    def size(self) -> int:
        return self.data.size()

    # Вращает очередь по кругу на m элементов.
    # Первый элемент перемещается на последнее место.
    # Сложность:
    # n - количество элементов в очереди.
    # m - на сколько элементов нужно произвести вращение.
    # В худшем случае O(2n * (n - 1)) ≈ O(n^2), когда вращаем на 1 элемент меньше, чем длина очереди.
    # В среднем o(2n * m), когда вращаем на m элементов.
    # В лучшем случае Ω(1), когда m равняется длине очереди и вращение не требуется.
    # При превышении m длины очереди, m равняется остатку от деления m на длину очереди.
    def rotate(self, spins: int):
        queue_size = self.size()
        if queue_size == 0:
            return None

        for _spin in range(spins % queue_size):
            self.enqueue(self.dequeue())
        return None


class Stack:
    def __init__(self):
        self.data = LinkedList()

    def size(self):
        return self.data.len()

    # Добавление элемента в конец стека.
    # Сложность O(1), т.к. используем связный список.
    def push(self, value):
        return self.data.add_in_tail(Node(value)).value

    # Удаление элемента из конца стека.
    # Сложность O(1), т.к. используем связный список.
    def pop(self):
        if self.size() > 0:
            return self.data.delete_from_tail().value
        return None

    # Возвращает верхушку стека, последний элемент.
    def peek(self):
        if self.size() > 0:
            return self.data.last().value
        return None


class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class DummyNode(Node):
    def __init__(self):
        super().__init__(None)


class LinkedList:
    def __init__(self):
        self.head = DummyNode()
        self.tail = self.head
        self.head.next = self.tail
        self.tail.prev = self.head
        self.length = 0

    # Добавление узла в конец списка.
    def add_in_tail(self, item):
        self.tail.prev.next = item
        item.prev = self.tail.prev
        item.next = self.tail
        self.tail.prev = item
        self.length += 1
        return self.last()

    def delete_from_tail(self):
        node = self.tail.prev
        if type(node) is Node:
            node.prev.next = node.next
            self.tail.prev = node.prev
            self.length -= 1
            return node
        return None

    def last(self):
        node = self.tail.prev
        if type(node) is Node:
            return node
        return None

    # Определение длины списка.
    def len(self) -> int:
        return self.length
