def printing_values_with_even_indexes(array: list, index: int = 0):
    if len(array) <= index:
        return

    if index % 2 == 0:
        print(array[index])

    printing_values_with_even_indexes(array, index + 1)
