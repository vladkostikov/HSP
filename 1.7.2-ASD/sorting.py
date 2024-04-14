def SelectionSortStep(array: list, index: int) -> list:
    result_array = array[:]

    min_index = index
    current_index = index
    while current_index < len(result_array):
        if result_array[current_index] < result_array[min_index]:
            min_index = current_index
        current_index += 1

    if min_index > index:
        result_array[index], result_array[min_index] = result_array[min_index], result_array[index]

    return result_array


def BubbleSortStep(array: list) -> bool:
    result_array = array[:]
    is_swapped = False

    index = 0
    while index + 1 < len(result_array):
        if result_array[index] > result_array[index + 1]:
            result_array[index], result_array[index + 1] = result_array[index + 1], result_array[index]
            is_swapped = True
        index += 1

    return not is_swapped
