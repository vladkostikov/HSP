def artificial_muscle_fibers(arr: list) -> int:
    indexes_of_numbers_and_counters = []
    for number_index, number in enumerate(arr):
        counter_index = None
        for i, index_in_arr in enumerate(indexes_of_numbers_and_counters[::2]):
            if arr[index_in_arr] == number:
                counter_index = i * 2 + 1
                break

        if counter_index is None:
            indexes_of_numbers_and_counters.extend([number_index, 1])
        else:
            indexes_of_numbers_and_counters[counter_index] += 1

    counter = 0
    for count in indexes_of_numbers_and_counters[1::2]:
        if count > 1:
            counter += 1

    return counter
