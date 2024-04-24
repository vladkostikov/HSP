def KthOrderStatisticsStep(array: list[int], left_i: int, right_i: int, position: int) -> list[int]:
    start_i = left_i
    end_i = right_i

    pivot_element_i = (start_i + end_i) // 2
    pivot_element = array[pivot_element_i]

    ArrayChunk(array, start_i, end_i)
    new_pivot_element_i = array.index(pivot_element)

    if new_pivot_element_i == position:
        return [new_pivot_element_i, new_pivot_element_i]

    if new_pivot_element_i < position:
        start_i = new_pivot_element_i + 1

    if new_pivot_element_i > position:
        end_i = new_pivot_element_i - 1

    return [start_i, end_i]


def KthOrderStatistics(array: list[int], left_i: int, right_i: int, position: int) -> int:
    start_i = left_i
    end_i = right_i
    while start_i <= end_i:
        pivot_element_i = (start_i + end_i + 1) // 2
        pivot_element = array[pivot_element_i]

        ArrayChunk(array, start_i, end_i)
        new_pivot_element_i = array.index(pivot_element)

        if new_pivot_element_i == position:
            return array[position]

        if new_pivot_element_i < position:
            start_i = new_pivot_element_i + 1

        if new_pivot_element_i > position:
            end_i = new_pivot_element_i - 1


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
