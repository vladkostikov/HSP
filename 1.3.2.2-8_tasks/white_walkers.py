def white_walkers(village: str) -> bool:
    digits = []
    for num in range(0, 10):
        digits.append(str(num))

    first_cityzen = 0
    white_walkers_between_cityzens = 0
    is_walkers_identified = False
    for char in village:
        if char in digits:
            second_cityzen = char
            sum_of_two_citizens = int(first_cityzen) + int(second_cityzen)

            if sum_of_two_citizens == 10:
                if white_walkers_between_cityzens != 3:
                    return False
                is_walkers_identified = True
            first_cityzen = second_cityzen
            white_walkers_between_cityzens = 0
        elif char == "=":
            white_walkers_between_cityzens += 1

    return is_walkers_identified
