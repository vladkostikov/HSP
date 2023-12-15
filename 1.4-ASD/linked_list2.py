class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    # Добавление узла в конец списка.
    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
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
        node = self.head
        while node is not None:
            # Переходим к следующему узлу, если значение не подходит.
            if node.value != val:
                node = node.next
                continue

            # Если узел для удаления единственный в списке, то очищаем список и завершаем цикл.
            if (node is self.head) and (node is self.tail):
                self.clean()
                break

            # Если узел для удаления последний, то смещаем последний узел и завершаем цикл.
            if node is self.tail:
                self.tail = node.prev
                node.prev.next = None
                break

            # Если узел для удаления первый, то смещаем первый узел.
            if node is self.head:
                self.head = node.next
                node.next.prev = None
                node = node.next
                # Завершаем цикл, если нужно удалить только один узел.
                if delete_all is False:
                    break
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
        # Если не указано после какого узла добавить, то:
        # 1) для пустого списка добавляем узел в начало списка;
        # 2) для непустого списка добавляем узел в конец списка.
        if after_node is None:
            self.add_in_tail(new_node)
        # Добавляем узел после указанного узла.
        elif after_node is self.tail:
            self.add_in_tail(new_node)
        else:
            after_node.next.prev = new_node
            new_node.next = after_node.next
            new_node.prev = after_node
            after_node.next = new_node
        return None

    def sum_of_two_linked_lists(self, second_list):
        sum_of_lists = []
        first_node = self.head
        second_node = second_list.head

        if self.len() != second_list.len():
            return None

        while first_node is not None:
            sum_of_lists.append(first_node.value + second_node.value)
            first_node = first_node.next
            second_node = second_node.next

        # Возвращаем сумму элементов списка, только если они равны по длине.
        return sum_of_lists

    def add_in_head(self, new_node):
        if self.head is None:
            self.add_in_tail(new_node)
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        return None
