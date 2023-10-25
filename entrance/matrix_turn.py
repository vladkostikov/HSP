def MatrixTurn(matrix: list, height: int, width: int, rotations: int):
    for _i in range(rotations):
        for circle_number_outside in range(min(height, width) // 2):
            sides_of_circle = find_sides_of_circle(matrix, height, width, circle_number_outside)
            rotated_sides_of_circle = make_rotation(sides_of_circle)
            replace_values_in_matrix(matrix, height, width, circle_number_outside, rotated_sides_of_circle)


def find_sides_of_circle(matrix: list, height: int, width: int, circle_number_outside: int) -> list:
    start_top_side_index = circle_number_outside
    end_top_side_index = width - circle_number_outside
    top_side = list(matrix[circle_number_outside][start_top_side_index:end_top_side_index])
    top_side = "".join(top_side)

    start_right_side_index = circle_number_outside
    end_right_side_index = height - circle_number_outside - 1
    right_side = []
    for _index, row in enumerate(matrix[start_right_side_index:end_right_side_index + 1]):
        right_side_index = width - 1 - circle_number_outside
        right_side.append(row[right_side_index])
    right_side = right_side[1:-1]
    right_side = "".join(right_side)

    start_bottom_side_index = circle_number_outside
    end_bottom_side_index = width - circle_number_outside - 1
    bottom_side_index = height - 1 - circle_number_outside
    bottom_side = list(matrix[bottom_side_index][start_bottom_side_index:end_bottom_side_index + 1])
    bottom_side = "".join(list(reversed(bottom_side)))

    start_left_side_index = circle_number_outside
    end_left_side_index = height - circle_number_outside - 1
    left_side = []
    for _index, row in enumerate(matrix[start_left_side_index:end_left_side_index + 1]):
        left_side_index = circle_number_outside
        left_side.append(row[left_side_index])
    left_side = "".join(list(reversed(left_side))[1:-1])

    return [top_side, right_side, bottom_side, left_side]


def make_rotation(sides_of_circle: list) -> list:
    top_side, right_side, bottom_side, left_side = sides_of_circle
    circle = "".join(sides_of_circle)
    rotated_circle = circle[-1:] + circle[:-1]

    start_top_side_index = 0
    end_top_side_index = start_top_side_index + len(top_side)
    rotated_top_side = rotated_circle[0:end_top_side_index]

    start_right_side_index = end_top_side_index
    end_right_side_index = end_top_side_index + len(right_side)
    rotated_right_side = rotated_circle[start_right_side_index:end_right_side_index]

    start_bottom_side_index = end_right_side_index
    end_bottom_side_index = start_bottom_side_index + len(bottom_side)
    rotated_bottom_side = rotated_circle[start_bottom_side_index:end_bottom_side_index]
    rotated_bottom_side = "".join(list(reversed(rotated_bottom_side)))

    start_left_side_index = end_bottom_side_index
    end_left_side_index = start_left_side_index + len(left_side)
    rotated_left_side = rotated_circle[start_left_side_index:end_left_side_index]
    rotated_left_side = "".join(list(reversed(rotated_left_side)))

    return [rotated_top_side, rotated_right_side, rotated_bottom_side, rotated_left_side]


def replace_values_in_matrix(matrix: list, height: int, width: int, circle_number_outside: int,
                             rotated_sides_of_circle: list):
    rotated_top_side, rotated_right_side, rotated_bottom_side, rotated_left_side = rotated_sides_of_circle

    top_line_index = circle_number_outside
    start_top_side_index = circle_number_outside
    end_top_side_index = width - circle_number_outside - 1
    replaced_top_line = (matrix[top_line_index][0:start_top_side_index]
                         + rotated_top_side
                         + matrix[top_line_index][end_top_side_index + 1:])
    matrix[top_line_index] = replaced_top_line

    right_side_index = width - circle_number_outside - 1
    start_row_right_side_index = circle_number_outside + 1
    for char in rotated_right_side:
        replaced_right_line = (matrix[start_row_right_side_index][:right_side_index]
                               + char
                               + matrix[start_row_right_side_index][right_side_index + 1:])
        matrix[start_row_right_side_index] = replaced_right_line
        start_row_right_side_index += 1

    bottom_line_index = height - 1 - circle_number_outside
    start_bottom_side_index = circle_number_outside
    end_bottom_side_index = width - circle_number_outside - 1
    replaced_bottom_line = (matrix[bottom_line_index][0:start_bottom_side_index]
                            + rotated_bottom_side
                            + matrix[bottom_line_index][end_bottom_side_index + 1:])
    matrix[bottom_line_index] = replaced_bottom_line

    left_side_index = circle_number_outside
    start_row_left_side_index = circle_number_outside + 1
    for char in rotated_left_side:
        replaced_left_line = (matrix[start_row_left_side_index][:left_side_index]
                              + char
                              + matrix[start_row_left_side_index][left_side_index + 1:])
        matrix[start_row_left_side_index] = replaced_left_line
        start_row_left_side_index += 1
