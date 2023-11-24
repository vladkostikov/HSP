def EEC_help(arr1: list, arr2: list) -> bool:
    if len(arr1) != len(arr2):
        return False

    arr1_values_counter = {}
    for value in arr1:
        if arr1_values_counter.get(value) is None:
            arr1_values_counter[value] = 1
        else:
            arr1_values_counter[value] += 1

    for value in arr2:
        if arr1_values_counter.get(value) is None:
            return False
        elif arr1_values_counter[value] > 1:
            arr1_values_counter[value] -= 1
        else:
            arr1_values_counter.pop(value)

    return True
