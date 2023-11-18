def find_second_maximum_number(numbers: list) -> int:
    second_maximum_index = find_second_maximum_number_index(numbers, [])
    return numbers[second_maximum_index]


def find_second_maximum_number_index(numbers: list, maximum_indexes: list) -> int:
    maximum_index = 0
    if maximum_index in maximum_indexes:
        maximum_index = 1

    for index, num in enumerate(numbers):
        if (num > numbers[maximum_index]) and (index not in maximum_indexes):
            maximum_index = index

    if len(maximum_indexes) == 0:
        return find_second_maximum_number_index(numbers, [maximum_index])
    return maximum_index
