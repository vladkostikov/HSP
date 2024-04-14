def InsertionSort(array: list, step: int) -> list:
    index = 0
    while index < step and index < len(array):
        InsertionSortStep(array, step, index)
        index += 1
    return array


def InsertionSortStep(array: list, step: int, index: int) -> list:
    array_for_step = array[index::step]
    sorted_array_for_step = list(sorted(array_for_step))
    array[index::step] = sorted_array_for_step
    return array
