def SelectionSortStep(array: list, index: int) -> list:
    min_index = index
    current_index = index
    while current_index < len(array):
        if array[current_index] < array[min_index]:
            min_index = current_index
        current_index += 1

    if min_index > index:
        array[index], array[min_index] = array[min_index], array[index]

    return array


def BubbleSortStep(array: list) -> bool:
    is_swapped = False

    index = 0
    while index + 1 < len(array):
        if array[index] > array[index + 1]:
            array[index], array[index + 1] = array[index + 1], array[index]
            is_swapped = True
        index += 1

    return not is_swapped
