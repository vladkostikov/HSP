class Stack:
    def __init__(self):
        self.data = LinkedList()

    def size(self):
        return self.data.len()

    # Сложность O(1), т.к. добавляем элемент в конец связного списка.
    def push(self, value):
        return self.data.add_in_tail(Node(value)).value

    # Сложность O(1), т.к. удаляем элемент из конца связного списка.
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
            node.prev.next = self.tail
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


# Проверка сбалансированности скобок.
def check_balance_of_brackets(brackets: str) -> bool:
    stack = Stack()
    for bracket in brackets:
        if bracket == '(':
            stack.push(bracket)
            continue
        if bracket == ')' and stack.peek() == '(':
            stack.pop()
            continue
        return False
    return stack.size() == 0
