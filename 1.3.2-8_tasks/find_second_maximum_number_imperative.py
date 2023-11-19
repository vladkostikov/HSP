def find_second_maximum_number_imperative(numbers: list) -> int:
    maximum1, maximum2 = numbers[0], numbers[1]
    if maximum2 > maximum1:
        maximum1, maximum2 = numbers[1], numbers[0]

    for num in numbers[2:]:
        if num > maximum1:
            maximum1, maximum2 = num, maximum1
            continue
        if num > maximum2:
            maximum2 = num

    return maximum2
