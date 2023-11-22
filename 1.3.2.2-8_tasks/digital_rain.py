def digital_rain(col: str) -> str:
    counter0 = 0
    counter1 = 0
    for char in col:
        if char == "0":
            counter0 += 1
        elif char == "1":
            counter1 += 1

    start_index = 0
    end_index = len(col) - 1
    for _char in col:
        if counter0 == counter1:
            return col[start_index:end_index + 1]

        if counter0 < counter1:
            if col[start_index] == "1":
                start_index += 1
                counter1 -= 1
            elif col[end_index] == "1":
                end_index -= 1
                counter1 -= 1
            else:
                start_index += 1
                counter0 -= 1

        elif counter1 < counter0:
            if col[start_index] == "0":
                start_index += 1
                counter0 -= 1
            elif col[end_index] == "0":
                end_index -= 1
                counter0 -= 1
            else:
                start_index += 1
                counter1 -= 1

    return col[start_index:end_index + 1]
