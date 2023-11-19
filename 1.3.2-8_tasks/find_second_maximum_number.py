def find_second_maximum_number(numbers: list) -> int:
    maximum1, maximum2 = numbers[0], numbers[1]
    if maximum2 > maximum1:
        maximum1, maximum2 = numbers[1], numbers[0]

    return find_second_maximum(numbers, 2, maximum1, maximum2)


def find_second_maximum(numbers: list, index: int, max1: int, max2: int) -> int:
    if index == len(numbers):
        return max2

    if numbers[index] > max1:
        return find_second_maximum(numbers, index + 1, numbers[index], max1)

    if numbers[index] > max2:
        return find_second_maximum(numbers, index + 1, max1, numbers[index])

    return find_second_maximum(numbers, index + 1, max1, max2)
