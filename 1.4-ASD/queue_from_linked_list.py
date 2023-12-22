class Queue:
    def __init__(self):
        self.data = LinkedList()

    # Вставка в конец очереди.
    # Сложность O(1), т.к. используем оптимизированный связный список.
    def enqueue(self, item):
        self.data.add_in_tail(Node(item))
        return self.data.last().value

    # Выдача из начала очереди.
    # Сложность O(1), т.к. используем оптимизированный связный список.
    def dequeue(self):
        node = self.data.delete_from_head()
        if node is None:
            return None
        return node.value

    # Размер очереди.
    # Сложность O(1), т.к. длину храним в виде атрибута в связном списке.
    def size(self) -> int:
        return self.data.len()


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
        return None

    # Удаление первого узла из списка.
    def delete_from_head(self):
        node = self.head.next
        if type(node) is Node:
            self.head.next = node.next
            node.next.prev = self.head
            self.length -= 1
            return node
        return None

    # Определение длины списка.
    def len(self) -> int:
        return self.length

    def last(self):
        node = self.tail.prev
        if type(node) is Node:
            return node
        return None
