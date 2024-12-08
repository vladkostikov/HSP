class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DummyNode(Node):
    def __init__(self):
        super().__init__(None)


class ParentList:
    HEAD_OK = 1  # курсор установлен на первый узел
    HEAD_ERR = 2  # список пуст

    TAIL_OK = 1  # курсор установлен на последний узел
    TAIL_ERR = 2  # список пуст

    RIGHT_OK = 1  # курсор сдвинут на узел вправо
    RIGHT_ERR = 2  # правее нет элемента

    GET_OK = 1  # возвращено значение текущего узла
    GET_ERR = 2  # список пуст

    ADD_TO_EMPTY_NIL = 0  # add_to_empty() не вызывалась
    ADD_TO_EMPTY_OK = 1  # значение успешно добавлено в пустой список
    ADD_TO_EMPTY_ERR = 2  # список не пустой

    PUT_RIGHT_OK = 1  # значение успешно добавлено в список справа от курсора
    PUT_RIGHT_ERR = 2  # список пуст

    PUT_LEFT_OK = 1  # значение успешно добавлено в список слева от курсора
    PUT_LEFT_ERR = 2  # список пуст

    REMOVE_OK = 1  # значение успешно удалено, курсор сдвинут
    REMOVE_ERR = 2  # список пуст

    REPLACE_OK = 1  # значение текущего узла заменено на заданное
    REPLACE_ERR = 2  # список пуст

    FIND_OK = 1  # следующий элемент найден, курсор сдвинут вправо на узел с искомым значением
    FIND_ERR = 1  # следующий элемент не найден
    FIND_EMPTY = 2  # список пуст

    REMOVE_ALL_OK = 1  # удалены все узлы с указанным значением, курсор сдвинут в начало списка
    REMOVE_ALL_ERR = 2  # список пуст

    # Постусловие: создан новый пустой двусвязный список с dummy узлом
    def __init__(self):
        self.head_node = DummyNode()
        self.tail_node = self.head_node
        self.cursor = self.head_node  # курсор всегда указывает на узел, если список не пуст

        self.head_node.next = self.tail_node
        self.tail_node.prev = self.head_node

        self.head_status = self.HEAD_ERR
        self.tail_status = self.TAIL_ERR
        self.right_status = self.RIGHT_ERR
        self.get_status = self.GET_ERR
        self.add_to_empty_status = self.ADD_TO_EMPTY_NIL
        self.put_right_status = self.PUT_RIGHT_ERR
        self.put_left_status = self.PUT_LEFT_ERR
        self.remove_status = self.REMOVE_ERR
        self.replace_status = self.REPLACE_ERR
        self.find_status = self.FIND_ERR
        self.remove_all_status = self.REMOVE_ALL_ERR

    # Атомарные команды

    # Предусловие: список не пустой
    # Постусловие: курсор указывает на первый узел в списке
    def head(self) -> None:
        if type(self.head_node.next) is Node:
            self.cursor = self.head_node.next
            self.head_status = self.HEAD_OK
        else:
            self.head_status = self.HEAD_ERR

        return None

    # Предусловие: список не пустой
    # Постусловие: курсор указывает на последний узел в списке
    def tail(self) -> None:
        if type(self.tail_node.prev) is Node:
            self.cursor = self.tail_node.prev
            self.head_status = self.HEAD_OK
        else:
            self.head_status = self.HEAD_ERR

        return None

    # Предусловие: курсор не в конце списка
    # Постусловие: курсор сдвинут на один узел вправо
    def right(self) -> None:
        if type(self.cursor.next) is Node:
            self.cursor = self.cursor.next
            self.right_status = self.RIGHT_OK
        else:
            self.right_status = self.RIGHT_ERR

        return None

    # Предусловие: список не пустой
    # Постусловие: следом за курсором добавлен новый узел с заданным значением
    def put_right(self, value) -> None:
        if type(self.cursor) is Node:
            new_node = Node(value)
            new_node.prev = self.cursor
            new_node.next = self.cursor.next

            new_node.prev.next = new_node
            new_node.next.prev = new_node

            self.put_right_status = self.PUT_RIGHT_OK
        else:
            self.put_right_status = self.PUT_RIGHT_ERR

        return None

    # Предусловие: список не пустой
    # Постусловие: перед курсором добавлен новый узел с заданным значением
    def put_left(self, value) -> None:
        if type(self.cursor) is Node:
            new_node = Node(value)
            new_node.prev = self.cursor.prev
            new_node.next = self.cursor

            new_node.prev.next = new_node
            new_node.next.prev = new_node

            self.put_left_status = self.PUT_LEFT_OK
        else:
            self.put_left_status = self.PUT_LEFT_ERR

        return None

    # Предусловие: список не пустой
    # Постусловие: текущий узел удаляется, курсор смещается к правому узлу, если он есть,
    # иначе смещается к левому узлу, если он есть
    def remove(self) -> None:
        if type(self.cursor) is not Node:
            self.remove_status = self.REMOVE_ERR
            return None

        current_node = self.cursor
        left_node = current_node.prev
        right_node = current_node.next
        if type(right_node) is Node:
            self.cursor = right_node
        elif type(left_node) is Node:
            self.cursor = left_node
        else:
            self.cursor = self.head_node

        left_node.next = right_node
        right_node.prev = left_node
        self.remove_status = self.REMOVE_OK
        return None

    # Постусловие: список очищен, курсор не указывает на узел
    def clear(self) -> None:
        self.head_node.next = self.tail_node
        self.tail_node.prev = self.head_node
        self.cursor = self.head_node
        return None

    # Предусловие: список пуст
    # Постусловие: в списке находится один узел с заданным значением и курсор указывает на этот узел
    def add_to_empty(self, value) -> None:
        if type(self.head_node.next) is not Node:
            new_node = Node(value)
            new_node.prev = self.head_node
            new_node.next = self.tail_node

            self.head_node.next = new_node
            self.tail_node.prev = new_node
            self.cursor = new_node
            self.add_to_empty_status = self.ADD_TO_EMPTY_OK
        else:
            self.add_to_empty_status = self.ADD_TO_EMPTY_ERR

        return None

    # Дополнительные команды

    # Постусловие: в конец списка добавлен новый узел с указанным значением
    def add_tail(self, value) -> None:
        new_node = Node(value)
        tail_node = self.tail_node.prev

        new_node.prev = tail_node
        new_node.next = tail_node.next
        tail_node.next = new_node
        new_node.next.prev = new_node

        return None

    # Предусловие: список не пустой
    # Постусловие: значение текущего узла заменено на заданное
    def replace(self, value) -> None:
        if type(self.cursor) is Node:
            new_node = Node(value)
            old_node = self.cursor

            new_node.prev = old_node.prev
            new_node.next = old_node.next
            new_node.prev.next = new_node
            new_node.next.prev = new_node
            self.cursor = new_node
            self.replace_status = self.REPLACE_OK
        else:
            self.replace_status = self.REPLACE_ERR

        return None

    # Предусловие: список не пустой
    # Постусловие: курсор смещается к следующему узлу с искомым значением, если он есть, иначе остаётся на месте
    def find(self, value) -> None:
        if type(self.head_node.next) is not Node:
            self.find_status = self.FIND_EMPTY
            return None

        current_node = self.cursor.next
        while type(current_node) is Node:
            if current_node.value == value:
                break
            current_node = current_node.next

        if current_node.value == value and type(current_node) is Node:
            self.cursor = current_node
            self.find_status = self.FIND_OK
        else:
            self.find_status = self.FIND_ERR

        return None

    # Предусловие: список не пустой
    # Постусловие: удалены все узлы с указанным значением, курсор сдвинут в начало списка
    def remove_all(self, value) -> None:
        current_node = self.head_node.next
        if type(current_node) is not Node:
            self.remove_all_status = self.REMOVE_ALL_ERR
            return None

        while type(current_node) is Node:
            left_node = current_node.prev
            right_node = current_node.next
            if current_node.value == value:
                left_node.next = right_node
                right_node.prev = left_node
            current_node = right_node

        self.cursor = self.head_node.next
        self.remove_all_status = self.REMOVE_ALL_OK
        return None

    # Запросы

    # Предусловие: список не пуст
    def get(self):
        if type(self.cursor) is Node:
            result = self.cursor.value
            self.get_status = self.GET_OK
        else:
            result = None
            self.get_status = self.GET_ERR

        return result

    # Размер списка
    def size(self):
        counter = 0
        node = self.head_node.next
        while type(node) is Node:
            counter += 1
            node = node.next

        return counter

    # Находится ли курсор в начале списка
    def is_head(self) -> bool:
        return self.cursor is self.head_node.next and type(self.cursor) is Node

    # Находится ли курсор в конце списка
    def is_tail(self) -> bool:
        return self.cursor is self.tail_node.prev and type(self.cursor) is Node

    # Установлен ли курсор на какой-либо узел в списке(по сути, непустой ли список)
    def is_value(self) -> bool:
        return type(self.cursor) is Node

    # Запросы статусов

    def get_head_status(self) -> int:
        return self.head_status

    def get_right_status(self) -> int:
        return self.right_status

    def get_get_status(self) -> int:
        return self.get_status

    def get_add_to_empty_status(self) -> int:
        return self.add_to_empty_status

    def get_put_right_status(self) -> int:
        return self.put_right_status

    def get_put_left_status(self) -> int:
        return self.put_left_status

    def get_remove_status(self) -> int:
        return self.remove_status

    def get_replace_status(self) -> int:
        return self.replace_status

    def get_find_status(self) -> int:
        return self.find_status

    def get_remove_all_status(self) -> int:
        return self.remove_all_status


class LinkedList(ParentList):
    def __init__(self):
        super().__init__()


class TwoWayList(ParentList):
    LEFT_OK = 1  # курсор сдвинут на узел влево
    LEFT_ERR = 2  # левее нет элемента

    def __init__(self):
        super().__init__()

        self.left_status = self.LEFT_ERR

    # Команды

    # Предусловие: курсор не в начале списка
    # Постусловие: курсор сдвинут на один узел влево
    def left(self) -> None:
        if type(self.cursor.prev) is Node:
            self.cursor = self.cursor.prev
            self.left_status = self.LEFT_OK
        else:
            self.left_status = self.LEFT_ERR

        return None

    # Запросы статусов

    def get_left_status(self) -> int:
        return self.left_status
