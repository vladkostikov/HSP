def massdriver(activate: list) -> int:
    numbers_indexes = {}

    first_repeating_element_index = None
    for index, number in enumerate(activate):
        if numbers_indexes.get(number) is None:
            numbers_indexes[number] = index
        elif first_repeating_element_index is None:
            first_repeating_element_index = numbers_indexes[number]
        elif first_repeating_element_index > numbers_indexes[number]:
            first_repeating_element_index = numbers_indexes[number]

    if first_repeating_element_index is None:
        return -1
    return first_repeating_element_index
