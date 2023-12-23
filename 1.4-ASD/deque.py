class Deque:
    def __init__(self):
        self.storage = LinkedList()

    # Добавление в голову.
    def addFront(self, item):
        return self.storage.add_in_head(Node(item)).value

    # Добавление в хвост.
    def addTail(self, item):
        return self.storage.add_in_tail(Node(item)).value

    # Удаление из головы.
    def removeFront(self):
        if self.size() == 0:
            return None
        return self.storage.delete_from_head().value

    # Удаление из хвоста.
    def removeTail(self):
        if self.size() == 0:
            return None
        return self.storage.delete_from_tail().value

    # Размер очереди.
    def size(self):
        return self.storage.len()


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
    def add_in_head(self, item):
        item.prev = self.head
        item.next = self.head.next
        item.prev.next = item
        item.next.prev = item
        self.length += 1
        return self.first()

    # Удаление узла из начала списка.
    def delete_from_head(self):
        node = self.head.next
        if type(node) is Node:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.length -= 1
            return node
        return None

    # Добавление узла в конец списка.
    def add_in_tail(self, item):
        self.tail.prev.next = item
        item.prev = self.tail.prev
        item.next = self.tail
        self.tail.prev = item
        self.length += 1
        return self.last()

    # Удаление узла из конца списка.
    def delete_from_tail(self):
        node = self.tail.prev
        if type(node) is Node:
            node.prev.next = node.next
            self.tail.prev = node.prev
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


def is_palindrome(string: str) -> bool:
    prepared_string = prepare_string(string)
    deque = Deque()
    for char in prepared_string:
        deque.addTail(char)

    for _i in range(deque.size() // 2):
        if deque.removeFront() != deque.removeTail():
            return False

    return deque.size() <= 1


def prepare_string(string: str) -> str:
    return "".join([char.lower() for char in string if char.isalpha()])
