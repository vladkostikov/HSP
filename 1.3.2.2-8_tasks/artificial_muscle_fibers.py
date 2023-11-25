def artificial_muscle_fibers(arr: list) -> int:
    bit_array = [False for _i in range(65536)]

    counter = 0
    for number in arr:
        if bit_array[number] == False:
            bit_array[number] = True
        elif bit_array[number + len(bit_array) // 2] == False:
            bit_array[number + len(bit_array) // 2] = True
            counter += 1

    return counter
