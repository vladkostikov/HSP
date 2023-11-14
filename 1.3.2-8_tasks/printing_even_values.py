def printing_even_values(array: list, step: int = 0):
    if len(array) <= step:
        return

    if array[step] % 2 == 0:
        print(array[step])

    printing_even_values(array, step + 1)
