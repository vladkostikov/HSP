class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    # Сложность O(N), т.к. удаляем первый элемент, а остальные сдвигаем.
    def pop(self):
        if self.size() > 0:
            return self.stack.pop(0)
        return None

    # Сложность O(N), т.к. добавляем элемент в начало списка списка, а остальные сдвигаем.
    def push(self, value):
        self.stack.insert(0, value)
        return self.stack[0]

    # Возвращает верхушку стека, в данной реализация это голова, первый элемент.
    def peek(self):
        if self.size() > 0:
            return self.stack[0]
        return None

    # Проверка сбалансированности скобок.
    def check_balance_of_brackets(self, brackets: str) -> bool:
        for bracket in brackets:
            if bracket == '(':
                self.push(bracket)
                continue
            if bracket == ')' and self.peek() == '(':
                self.pop()
                continue
            return False
        return self.size() == 0
