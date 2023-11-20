def white_walkers(village: str) -> bool:
    digits = []
    for num in range(0, 10):
        digits.append(str(num))

    second_cityzen_index = None
    is_walkers_identified = False
    for i, char in enumerate(village):
        if char not in digits:
            continue

        if second_cityzen_index is None:
            second_cityzen_index = i
            continue

        first_cityzen_index = second_cityzen_index
        second_cityzen_index = i
        sum_of_two_citizens = int(village[first_cityzen_index]) + int(village[second_cityzen_index])
        if sum_of_two_citizens == 10:
            white_walkers_between_cityzens = village[first_cityzen_index + 1:second_cityzen_index].count("=")
            if white_walkers_between_cityzens != 3:
                return False
            is_walkers_identified = True
    return is_walkers_identified
