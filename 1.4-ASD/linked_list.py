class Node:
    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Добавление узла в конец списка.
    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item
        return None

    # Печать всех узлов списка.
    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next
        return None

    # Поиск первого узла с нужным значением.
    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    # Поиск всех узлов с нужным значением.
    def find_all(self, val) -> list:
        nodes = []
        node = self.head
        while node is not None:
            if node.value == val:
                nodes.append(node)
            node = node.next
        return nodes

    # Удаление узла/узлов с нужным значением.
    def delete(self, val, delete_all=False):
        previous_node = self.head
        current_node = self.head
        while current_node is not None:
            # Переходим к следующему узлу, если значение не подходит.
            if current_node.value != val:
                previous_node = current_node
                current_node = current_node.next
                continue

            # Очищаем список и завершаем цикл, если узел для удаления единственный.
            if (current_node is self.head) and (current_node is self.tail):
                self.clean()
                break

            # Смещаем последний узел и завершаем цикл, если узел для удаления последний.
            if current_node is self.tail:
                self.tail = previous_node
                previous_node.next = None
                break

            # Смещаем первый узел, если узел для удаления первый.
            if current_node is self.head:
                self.head = current_node.next

            # Переходим к следующему узлу
            previous_node.next = current_node.next
            current_node = current_node.next

            # Завершаем цикл, если нужно удалить только один узел.
            if delete_all is False:
                break
        return None

    # Очистка списка.
    def clean(self):
        self.head = None
        self.tail = None
        return None

    # Определение длины списка.
    def len(self) -> int:
        length = 0
        node = self.head
        while node is not None:
            length += 1
            node = node.next
        return length

    # Добавление узла в список.
    def insert(self, after_node, new_node):
        node = self.head

        if self.head is None:
            self.add_in_tail(new_node)
        # Добавляем узел в начало списка, если не указано в какое место вставить узел.
        elif after_node is None:
            new_node.next = node
            self.head = new_node
        # Добавляем узел после указанного узла.
        else:
            new_node.next = after_node.next
            after_node.next = new_node
            if after_node is self.tail:
                self.tail = new_node
        return None

    def sum_of_two_linked_lists(self, second_list):
        sum_of_lists = []
        first_node = self.head
        second_node = second_list.head
        while first_node is not None:
            # Если в первом списке ещё есть узлы, а во втором нет, то списки различаются по длине.
            if second_node is None:
                return None
            sum_of_lists.append(first_node.value + second_node.value)
            first_node = first_node.next
            second_node = second_node.next

        # Если во втором списке ещё остались узлы, то списки различаются по длине.
        if second_node is not None:
            return None

        # Возвращаем сумму элементов списка, только если они равны по длине.
        return sum_of_lists
