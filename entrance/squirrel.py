def squirrel(number: int) -> int:
    if number < 1:
        return 0

    nuts = 1
    counter = 1
    while counter <= number:
        nuts *= counter
        counter += 1

    emeralds = int(str(nuts)[0])
    return emeralds
