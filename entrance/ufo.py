def UFO(_length: int, encoded_numbers: list, octal: bool) -> list:
    decoded_numbers = []

    if octal:
        for _i, number in enumerate(encoded_numbers):
            decoded_number = int(str(number), 8)
            decoded_numbers.append(decoded_number)
        return decoded_numbers

    for _i, number in enumerate(encoded_numbers):
        decoded_number = int(str(number), 16)
        decoded_numbers.append(decoded_number)
    return decoded_numbers
