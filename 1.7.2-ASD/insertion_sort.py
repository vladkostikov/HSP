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


def KnuthSequence(array_size: int) -> list:
    return list(reversed(_knuth_sequence(array_size, [1])))


def _knuth_sequence(array_size: int, arr: list) -> list:
    number = arr[-1] * 3 + 1
    if number >= array_size:
        return arr
    arr.append(number)
    return _knuth_sequence(array_size, arr)
