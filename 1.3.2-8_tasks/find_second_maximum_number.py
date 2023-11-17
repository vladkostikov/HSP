def find_second_maximum_number(array: list, maximum_indexes: list = None) -> int:
    maximum_index = 0
    if maximum_indexes is None:
        maximum_indexes = []
    if 0 in maximum_indexes:
        maximum_index = 1

    for index, num in enumerate(array):
        if (num > array[maximum_index]) and (index not in maximum_indexes):
            maximum_index = index

    if len(maximum_indexes) == 0:
        return find_second_maximum_number(array, maximum_indexes + [maximum_index])

    return array[maximum_index]
