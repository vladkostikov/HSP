def PatternUnlock(length: int, hits: list) -> str:
    keypad = [[6, 1, 9], [5, 2, 8], [4, 3, 7]]

    rows_index_of_hits = []
    for hit in hits:
        row_index = find_row(hit, keypad)
        rows_index_of_hits.append(row_index)

    columns_index_of_hits = []
    for hit in hits:
        column_index = find_column(hit, keypad)
        columns_index_of_hits.append(column_index)

    length_of_lines = []
    for i, hit in enumerate(hits[:-1]):
        if rows_index_of_hits[i] == rows_index_of_hits[i + 1]:
            length_of_lines.append(1)
        elif columns_index_of_hits[i] == columns_index_of_hits[i + 1]:
            length_of_lines.append(1)
        else:
            length_of_diagonal = pow(2.0, 0.5)
            length_of_lines.append(length_of_diagonal)

    length_of_line = sum(length_of_lines)
    rounded_length_of_line = round(length_of_line, 5)
    str_rounded_length_of_line = str(rounded_length_of_line)
    password = str_rounded_length_of_line.replace('.', '').replace('0', '')

    return password

def find_row(hit: int, keypad: list) -> int:
    for row_index, keys_row in enumerate(keypad):
        if hit in keys_row:
            return row_index

def find_column(hit: int, keypad: list) -> int:
    for i, keys_row in enumerate(keypad):
        for column_index, key in enumerate(keys_row):
            if hit == key:
                return column_index
