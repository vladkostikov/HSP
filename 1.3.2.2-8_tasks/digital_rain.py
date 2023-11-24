def digital_rain(col: str) -> str:
    counter0 = {}
    counter1 = {}
    differences_by_index = {}
    differences_by_value = {}
    max_length = 0
    start_index = 0
    end_index = 0
    for i, char in enumerate(list(col)):
        if char == "0":
            counter0[i] = counter0.get(i - 1, 0) + 1
            counter1[i] = counter1.get(i - 1, 0)
        elif char == "1":
            counter1[i] = counter1.get(i - 1, 0) + 1
            counter0[i] = counter0.get(i - 1, 0)
        differences_by_index[i] = counter0[i] - counter1[i]

        if differences_by_index[i] == 0:
            start_index = 0
            end_index = i + 1
            max_length = end_index - start_index
        elif differences_by_value.get(differences_by_index[i]) is not None:
            new_start_index = differences_by_value[differences_by_index[i]] + 1
            new_end_index = i + 1
            new_max_length = new_end_index - new_start_index
            if new_max_length >= max_length:
                start_index = new_start_index
                end_index = new_end_index
                max_length = new_max_length
        else:
            differences_by_value[differences_by_index[i]] = i

    return col[start_index:end_index]
