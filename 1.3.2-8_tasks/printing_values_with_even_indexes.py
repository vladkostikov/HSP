def printing_values_with_even_indexes(array: list, index: int = 0, printing: bool = True):
    if len(array) <= index:
        return

    printing and print(array[index])

    printing_values_with_even_indexes(array, index + 1, not printing)
