def QuickSortTailOptimization(array: list, left: int, right: int):
    while left < right:
        reference_value_i = ArrayChunk(array, left, right)
        QuickSortTailOptimization(array, left, reference_value_i - 1)
        left = reference_value_i + 1


def ArrayChunk(array: list, left: int, right: int) -> int:
    left_i = left
    right_i = right
    reference_value_i = (left_i + right_i + 1) // 2
    while True:
        reference_value = array[reference_value_i]

        while array[left_i] < reference_value:
            left_i += 1

        while array[right_i] > reference_value:
            right_i -= 1

        if (left_i == right_i - 1) and (array[left_i] > array[right_i]):
            array[left_i], array[right_i] = array[right_i], array[left_i]
            return ArrayChunk(array, left, right)

        if (left_i == right_i) or ((left_i == right_i - 1) and (array[left_i] < array[right_i])):
            return reference_value_i

        if array[left_i] >= array[reference_value_i] and array[right_i] <= array[reference_value_i]:
            array[left_i], array[right_i] = array[right_i], array[left_i]
            if left_i == reference_value_i:
                reference_value_i = right_i
            elif right_i == reference_value_i:
                reference_value_i = left_i
