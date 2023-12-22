class Queue:
    def __init__(self):
        self.data = Stack()

    # Вставка в конец очереди.
    # Сложность O(1), т.к. используем стек.
    def enqueue(self, item):
        return self.data.push(item)

    # Выдача из начала очереди.
    # Сложность O(1), т.к. используем стек.
    def dequeue(self):
        return self.data.pop_from_head()

    # Размер очереди.
    # Сложность O(1), т.к. длину храним в виде атрибута в связном списке.
    def size(self) -> int:
        return self.data.size()

    # Вращает очередь по кругу на N элементов.
    # Первый элемент перемещается на последнее место.
    # Сложность O(N), где N - на сколько элементов нужно произвести вращение.
    # N всегда меньше размера очереди.
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

    # Удаление элемента из начала стека.
    def pop_from_head(self):
        if self.size() > 0:
            return self.data.delete_from_head().value
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

    # Добавление узла в начало списка.
    def add_in_head(self, new_node):
        new_node.prev = self.head
        new_node.next = self.head.next
        self.head.next.prev = new_node
        self.head.next = new_node
        self.length += 1
        return self.first()

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

    def delete_from_head(self):
        node = self.head.next
        if type(node) is Node:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.length -= 1
            return node
        return None

    def first(self):
        node = self.head.next
        if type(node) is Node:
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
