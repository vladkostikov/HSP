def ConquestCampaign(height: int, width: int, battalions: int, coordinates: list) -> int:
    day = 1
    bridgehead = [[None for columns in range(width)] for rows in range(height)]

    # Landing
    heights = coordinates[::2]
    widths = coordinates[1::2]
    for i, _value in enumerate(heights):
        bridgehead[heights[i] - 1][widths[i] - 1] = day

    while not is_win(bridgehead):
        day += 1
        bridgehead = attack(bridgehead, day)

    return day


def is_win(bridgehead: list):
    bridgehead_flatten = []
    for row in bridgehead:
        bridgehead_flatten.extend(row)

    if None in bridgehead_flatten:
        return False
    else:
        return True


def find_areas_captured_on_day(bridgehead: list, day: int) -> list:
    rows_and_indexes = []
    for index_row, row in enumerate(bridgehead):
        rows_and_indexes.append([index_row, [index_column for index_column, value in enumerate(row) if value == day]])
    return rows_and_indexes


def attack(bridgehead: list, day: int) -> list:
    areas_captured_the_previous_day = find_areas_captured_on_day(bridgehead, day - 1)

    for rows_and_indexes in enumerate(areas_captured_the_previous_day):
        index_row = rows_and_indexes[1][0]
        indexes_columns = rows_and_indexes[1][1]
        for _i, index_column in enumerate(indexes_columns):
            current_row = bridgehead[index_row]
            left = index_column - 1
            right = index_column + 1
            up = index_row - 1
            down = index_row + 1

            if 0 <= left < len(current_row):
                current_row[left] = day

            if 0 <= right < len(current_row):
                current_row[right] = day

            if 0 <= up < len(bridgehead):
                bridgehead[up][index_column] = day

            if 0 <= down < len(bridgehead):
                bridgehead[down][index_column] = day
    return bridgehead
