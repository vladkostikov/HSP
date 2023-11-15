def find_second_maximum_number(array: list) -> int:
    return array[find_second_maximum_index(array)]


def find_second_maximum_index(array: list, first_maximum_index: int = None) -> int:
    maximum_index = 0
    if first_maximum_index == 0:
        maximum_index = 1

    for index, num in enumerate(array):
        # Find first maximum index.
        if (first_maximum_index is None) and (num > array[maximum_index]):
            maximum_index = index
            continue

        # Find second maximum index.
        if (first_maximum_index is not None) and (first_maximum_index != index) and (num > array[maximum_index]):
            maximum_index = index

    if first_maximum_index is None:
        return find_second_maximum_index(array, maximum_index)

    return maximum_index
