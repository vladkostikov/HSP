def exponentiation(number: int, power: int) -> int:
    if power == 0:
        return 1
    return number * exponentiation(number, power - 1)
