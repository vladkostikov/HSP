def MergeSort(array: list) -> list:
    if len(array) == 1:
        return array

    middle_i = len(array) // 2

    left_array = MergeSort(array[:middle_i])
    right_array = MergeSort(array[middle_i:])

    result_array = []

    left_i = 0
    right_i = 0
    while left_i < len(left_array) and right_i < len(right_array):
        if left_array[left_i] < right_array[right_i]:
            result_array.append(left_array[left_i])
            left_i += 1
            continue
        result_array.append(right_array[right_i])
        right_i += 1

    if left_i < len(left_array):
        result_array.extend(left_array[left_i:])

    if right_i < len(right_array):
        result_array.extend(right_array[right_i:])

    return result_array
