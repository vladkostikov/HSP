from stack import Stack


# Реализация вычисления постфиксного выражения.
# Допускается использовать целые числа, +, *.
def postfix(expressions: str) -> int:
    stack_of_numbers = Stack()
    operations = ['+', '*']

    char_index = 0
    while char_index < len(expressions):
        # Сканируем строку на число начиная с текущего индекса.
        number = scan_number(expressions, char_index)
        if number is not None:
            stack_of_numbers.push(number)

        # Проверяем является ли данный символ операцией.
        # Выполняем операцию, если в стеке есть 2 числа.
        if expressions[char_index] in operations:
            perform_operation(stack_of_numbers, expressions[char_index])

        # Возвращаем результат принудительно, если встречаем =.
        if expressions[char_index] == '=':
            break

        if number is not None:
            char_index += len(str(number))
        else:
            char_index += 1
    return stack_of_numbers.peek()


def perform_operation(stack_of_numbers, operation):
    if stack_of_numbers.size() >= 2:
        first_number = stack_of_numbers.pop()
        second_number = stack_of_numbers.pop()
        if operation == '+':
            stack_of_numbers.push(first_number + second_number)
        if operation == '*':
            stack_of_numbers.push(first_number * second_number)


def scan_number(expressions: str, start_index: int):
    numbers = [str(number) for number in range(10)]
    number = ''
    for char in expressions[start_index:]:
        if char in numbers:
            number += char
            continue
        break

    if len(number) > 0:
        return int(number)
    return None
