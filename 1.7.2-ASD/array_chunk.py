def ArrayChunk(array: list) -> int:
    reference_value_i = len(array) // 2
    left_i = 0
    right_i = len(array) - 1
    return _array_chunk(array, reference_value_i, left_i, right_i)


def _array_chunk(array: list, reference_value_i: int, left_i: int, right_i: int):
    reference_value = array[reference_value_i]

    while array[left_i] < reference_value:
        left_i += 1

    while array[right_i] > reference_value:
        right_i -= 1

    if (left_i == right_i - 1) and (array[left_i] > array[right_i]):
        array[left_i], array[right_i] = array[right_i], array[left_i]
        return ArrayChunk(array)

    if (left_i == right_i) or ((left_i == right_i - 1) and (array[left_i] < array[right_i])):
        return reference_value_i

    if left_i == reference_value_i:
        reference_value_i = right_i
    elif right_i == reference_value_i:
        reference_value_i = left_i
    array[left_i], array[right_i] = array[right_i], array[left_i]
    return _array_chunk(array, reference_value_i, left_i, right_i)
