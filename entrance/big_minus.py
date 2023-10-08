def BigMinus(first_num: str, second_num: str) -> str:
    first_num_digits = list(map(lambda num: int(num), first_num))
    second_num_digits = list(map(lambda num: int(num), second_num))

    big_num = determine_the_larger_number(first_num_digits, second_num_digits)

    if big_num == first_num_digits:
        little_num = second_num_digits
    else:
        little_num = first_num_digits

    # Reverse numbers to enumerate from the end
    big_num.reverse()
    little_num.reverse()

    difference_by_integers = []
    for i, v in enumerate(big_num):
        if i < len(little_num):
            if little_num[i] > big_num[i]:
                big_num[i + 1] -= 1
                big_num[i] += 10
            difference_by_integers.append(big_num[i] - little_num[i])
        else:
            difference_by_integers.append(big_num[i])

    difference_by_integers.reverse()
    difference_by_chars = list(map(lambda integer: str(integer), difference_by_integers))
    difference = "".join(difference_by_chars)
    difference_without_leading_zeros = difference[:-1].lstrip("0") + difference[-1]
    return difference_without_leading_zeros


def determine_the_larger_number(first_num: list, second_num: list) -> list:
    if len(first_num) > len(second_num):
        return first_num

    if len(first_num) < len(second_num):
        return second_num

    for i, v in enumerate(first_num):
        if first_num[i] == second_num[i]:
            continue

        if first_num[i] > second_num[i]:
            return first_num

        if first_num[i] < second_num[i]:
            return second_num

    return first_num
