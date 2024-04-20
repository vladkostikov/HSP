def QuickSort(array: list, left: int, right: int):
    if left > right:
        right += 1

    if left == right:
        return

    reference_value_i = ArrayChunk(array, left, right)

    QuickSort(array, left, reference_value_i)
    QuickSort(array, reference_value_i + 1, right)


def ArrayChunk(array: list, left_i: int, right_i: int) -> int:
    reference_value_i = (left_i + right_i) // 2
    return _array_chunk(array, reference_value_i, left_i, right_i)


def _array_chunk(array: list, reference_value_i: int, left_i: int, right_i: int):
    reference_value = array[reference_value_i]

    while array[left_i] < reference_value:
        left_i += 1

    while array[right_i] > reference_value:
        right_i -= 1

    if (left_i == right_i - 1) and (array[left_i] > array[right_i]):
        array[left_i], array[right_i] = array[right_i], array[left_i]
        return ArrayChunk(array, left_i, right_i)

    if (left_i == right_i) or ((left_i == right_i - 1) and (array[left_i] < array[right_i])):
        return reference_value_i

    if left_i == reference_value_i:
        reference_value_i = right_i
    elif right_i == reference_value_i:
        reference_value_i = left_i
    array[left_i], array[right_i] = array[right_i], array[left_i]
    return _array_chunk(array, reference_value_i, left_i, right_i)
