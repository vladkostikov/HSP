def SherlockValidString(string: str) -> bool:
    frequency = {}
    for char in string:
        old_frequency = frequency.get(char, 0)
        frequency[char] = old_frequency + 1

    values = list(frequency.values())
    keys = list(frequency.keys())
    minimum = min(values)
    maximum = max(values)
    if minimum == maximum:
        return True

    if values.count(minimum) == 1:
        position_minimum_in_values = values.index(minimum)
        minimum_char = keys[position_minimum_in_values]
        del frequency[minimum_char]
        new_values = list(frequency.values())
        return min(new_values) == max(new_values)

    if values.count(maximum) == 1:
        position_maximum_in_values = values.index(maximum)
        maximum_char = keys[position_maximum_in_values]
        frequency[maximum_char] -= 1
        new_values = list(frequency.values())
        return min(new_values) == max(new_values)

    return False
