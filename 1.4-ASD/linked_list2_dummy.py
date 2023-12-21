class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class DummyNode(Node):
    def __init__(self):
        super().__init__(None)


class LinkedList2:
    def __init__(self):
        self.head = DummyNode()
        self.tail = self.head
        self.head.next = self.tail
        self.tail.prev = self.head

    # Добавление узла в конец списка.
    def add_in_tail(self, item):
        self.tail.prev.next = item
        item.prev = self.tail.prev
        item.next = self.tail
        self.tail.prev = item
        return None

    # Печать всех узлов списка.
    def print_all_nodes(self):
        node = self.head.next
        while type(node) is Node:
            print(node.value)
            node = node.next
        return None

    # Поиск первого узла с нужным значением.
    def find(self, val):
        node = self.head.next
        while type(node) is Node:
            if node.value == val:
                return node
            node = node.next
        return None

    # Поиск всех узлов с нужным значением.
    def find_all(self, val) -> list:
        nodes = []
        node = self.head.next
        while type(node) is Node:
            if node.value == val:
                nodes.append(node)
            node = node.next
        return nodes

    # Удаление узла/узлов с нужным значением.
    def delete(self, val, delete_all=False):
        node = self.head.next
        while type(node) is Node:
            # Переходим к следующему узлу, если значение не подходит.
            if node.value != val:
                node = node.next
                continue

            # Исключаем текущий узел из списка и переходим к следующему узлу.
            node.prev.next = node.next
            node.next.prev = node.prev
            node = node.next

            # Завершаем цикл, если нужно удалить только один узел.
            if delete_all is False:
                break
        return None

    # Очистка списка.
    def clean(self):
        self.head = DummyNode()
        self.tail = DummyNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        return None

    # Определение длины списка.
    def len(self) -> int:
        length = 0
        node = self.head.next
        while type(node) is Node:
            length += 1
            node = node.next
        return length

    # Добавление узла в список.
    def insert(self, after_node, new_node):
        # Если не указано после какого узла добавить, то:
        # 1) для пустого списка добавляем узел в начало списка;
        # 2) для непустого списка добавляем узел в конец списка.
        if after_node is None:
            self.add_in_tail(new_node)
        # Добавляем узел после указанного узла.
        else:
            after_node.next.prev = new_node
            new_node.next = after_node.next
            new_node.prev = after_node
            after_node.next = new_node
        return None

    def sum_of_two_linked_lists(self, second_list):
        if self.len() != second_list.len():
            return None

        sum_of_lists = []
        first_node = self.head.next
        second_node = second_list.head.next
        while type(first_node) is Node:
            sum_of_lists.append(first_node.value + second_node.value)
            first_node = first_node.next
            second_node = second_node.next

        # Возвращаем сумму элементов списка, только если они равны по длине.
        return sum_of_lists

    def add_in_head(self, new_node):
        new_node.prev = self.head
        new_node.next = self.head.next
        self.head.next.prev = new_node
        self.head.next = new_node

        return None
