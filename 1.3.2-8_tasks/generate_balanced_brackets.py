def generate_balanced_brackets(number_of_opening_brackets: int) -> list:
    return generate_combinations(number_of_opening_brackets, 0, 0, "", [])


def generate_combinations(maximum_opening_brackets: int, opening_brackets: int, closing_brackets: int, string_of_brackets: str, balanced_brackets: list) -> list:
    if (closing_brackets >= maximum_opening_brackets) and (len(string_of_brackets) > 0):
        balanced_brackets.append(string_of_brackets)

    if opening_brackets < maximum_opening_brackets:
        generate_combinations(maximum_opening_brackets, opening_brackets + 1, closing_brackets, string_of_brackets + "(", balanced_brackets)

    if closing_brackets < opening_brackets:
        generate_combinations(maximum_opening_brackets, opening_brackets, closing_brackets + 1, string_of_brackets + ")", balanced_brackets)

    return balanced_brackets
