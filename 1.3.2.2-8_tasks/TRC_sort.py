def TRC_sort(trc: list) -> list:
    numbers = {}

    for num in trc:
        numbers[num] = numbers.get(num, 0) + 1

    return [0] * numbers[0] + [1] * numbers[1] + [2] * numbers[2]
