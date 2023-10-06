def TheRabbitsFoot(string: str, encode: bool) -> str:
    if encode:
        return encode_string(string)
    else:
        return decode_string(string)


def encode_string(string: str) -> str:
    string_without_spaces = string.replace(" ", "")
    chars = list(string_without_spaces)
    length = len(string_without_spaces)
    square_root = pow(length, 0.5)

    rows = int(square_root)
    columns = round(square_root, 0)
    if rows * columns < length:
        rows += 1

    matrix = chars_to_matrix(chars, rows)
    encoded_matrix = encode_matrix(matrix, chars, rows)

    encoded_strings = []
    for _i, chars in enumerate(encoded_matrix):
        encoded_strings.append("".join(chars))

    encoded_string = " ".join(encoded_strings)

    return encoded_string


def chars_to_matrix(chars: list, rows: int) -> list:
    matrix = [[]]
    row = 0
    column = 0
    for i, char in enumerate(chars):
        matrix[row].append(char)
        if (i % rows) < (rows - 1):
            column += 1
        else:
            matrix.append([])
            row += 1
            column = 0
    return matrix


def encode_matrix(matrix: list, chars: list, rows: int) -> list:
    encoded_matrix = [[]]
    row = 0
    column = 0
    for _v in enumerate(chars):
        if row == rows - 1:
            if column < len(matrix[row]):
                encoded_matrix[column].append(matrix[row][column])
                encoded_matrix.append([])
                column += 1
                row = 0
            else:
                column += 1
                row = 0
                encoded_matrix.append([])
                encoded_matrix[column].append(matrix[row][column])
                row += 1
        else:
            encoded_matrix[column].append(matrix[row][column])
            row += 1

    return encoded_matrix


def decode_string(string: str) -> str:
    string_without_spaces = string.replace(" ", "")
    chars = list(string_without_spaces)
    encoded_rows = string.split(" ")

    decoded_string = ""
    row = 0
    column = 0
    for _char in enumerate(chars):
        if row < len(encoded_rows[row]):
            decoded_string += encoded_rows[row][column]
            row += 1
        else:
            decoded_string += encoded_rows[row][column]
            row = 0
            column += 1

    return decoded_string
