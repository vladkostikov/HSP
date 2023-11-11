def sum_of_digits(number: int) -> int:
    if len(str(number)) == 1:
        return number
    return int(str(number)[0]) + sum_of_digits(int(str(number)[1:]))
