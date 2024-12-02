class BoundedStack:
    PUSH_NIL = 0  # push() не вызывалась
    PUSH_OK = 1  # последняя push() отработала корректно
    PUSH_ERR = 2  # последняя push() отработала некорректно, стек был полностью заполнен

    POP_NIL = 0  # pop() не вызывалась
    POP_OK = 1  # последняя pop() отработала корректно
    POP_ERR = 2  # стек пуст

    PEEK_NIL = 0  # peek() не вызывалась
    PEEK_OK = 1  # последняя peek() отработала корректно
    PEEK_ERR = 2  # стек пуст

    def __init__(self, max_size=32):
        self.stack = []
        self.max_size = max_size

        self.push_status = self.PUSH_NIL
        self.pop_status = self.POP_NIL
        self.peek_status = self.PEEK_NIL

    # Команды

    # Предусловие: в стеке есть свободное место
    # Постусловие: в стек добавлен новый элемент
    def push(self, element) -> None:
        if len(self.stack) < self.max_size:
            self.stack.append(element)
            self.push_status = self.PUSH_OK
        else:
            self.push_status = self.PUSH_ERR

        return None

    # Предусловие: стек не пустой
    # Постусловие: из стека удален последний элемент
    def pop(self) -> None:
        if len(self.stack) > 0:
            self.stack.pop()
            self.pop_status = self.POP_OK
        else:
            self.pop_status = self.POP_ERR

        return None

    # Постусловие: из стека удалены все элементы
    def clear(self) -> None:
        self.stack = []

        self.push_status = self.PUSH_NIL
        self.pop_status = self.POP_NIL
        self.peek_status = self.PEEK_NIL

        return None

    # Запросы

    # Предусловие: стек не пустой
    def peek(self):
        if len(self.stack) > 0:
            result = self.stack[-1]
            self.peek_status = self.PEEK_OK
        else:
            result = 0
            self.peek_status = self.PEEK_ERR

        return result

    def size(self) -> int:
        return len(self.stack)

    # Дополнительные запросы

    def get_push_status(self) -> int:
        return self.push_status

    def get_pop_status(self) -> int:
        return self.pop_status

    def get_peek_status(self) -> int:
        return self.peek_status
