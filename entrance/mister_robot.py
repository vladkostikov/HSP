def MisterRobot(length: int, data: list) -> bool:
    center = length // 2
    sorted_data = data.copy()
    for i, _v in enumerate(sorted_data[0:center]):
        # Move maximum number to the end of the list.
        start_index = 0 + i
        while start_index <= (length - 3 - i):
            three_elements_from_start = sorted_data[start_index:start_index + 3]
            while three_elements_from_start[2] != max(three_elements_from_start):
                three_elements_from_start = move_3_elements_to_left(three_elements_from_start)
            sorted_data[start_index:start_index + 3] = three_elements_from_start
            start_index += 1

        # Move minimum number to the start of the list.
        end_index = length - 1 - i
        while end_index >= i + 3:
            three_elements_from_end = sorted_data[end_index-3:end_index]
            while three_elements_from_end[0] != min(three_elements_from_end):
                three_elements_from_end = move_3_elements_to_left(three_elements_from_end)
            sorted_data[end_index-3:end_index] = three_elements_from_end
            end_index -= 1

    left_of_center, center_value, right_of_center = sorted_data[center - 1], sorted_data[center], sorted_data[center + 1]
    return left_of_center < center_value < right_of_center


def move_3_elements_to_left(data: list) -> list:
    first, second, third = data[0:3]
    first, second, third = second, third, first
    return [first, second, third]
