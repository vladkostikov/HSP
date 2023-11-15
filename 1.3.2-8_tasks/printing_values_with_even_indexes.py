def printing_values_with_even_indexes(array: list, index: int = 0):
    if len(array) <= index:
        return

    print(array[index])

    printing_values_with_even_indexes(array, index + 2)
