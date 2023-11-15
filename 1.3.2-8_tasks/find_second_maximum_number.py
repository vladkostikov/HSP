def find_second_maximum_number(array: list, first_maximum_index: int = 0, determining_first_maximum: bool = True) -> int:
    maximum_index = 0
    if first_maximum_index == 0 and not determining_first_maximum:
        maximum_index = 1

    for index, num in enumerate(array):
        if index == first_maximum_index:
            continue

        if num > array[maximum_index]:
            maximum_index = index

    if determining_first_maximum:
        return find_second_maximum_number(array, maximum_index, False)

    return array[maximum_index]
