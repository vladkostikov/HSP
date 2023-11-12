def list_length_with_pop(array: list) -> int:
    if len(array) == 0:
        return 0
    array.pop(0)
    return 1 + list_length_with_pop(array)
