def matrix(width: int, height: int, matrix: list) -> list:
    spiral = []
    for circle_number in range(width // 2 + 1):
        top_side = matrix[circle_number][circle_number:width - circle_number]
        spiral.extend(top_side)

        right_side = []
        rows_in_current_circle_for_right_side = matrix[circle_number + 1:width - circle_number]
        for row in rows_in_current_circle_for_right_side:
            right_side.append(row[-1 - circle_number])
        spiral.extend(right_side)

        bottom_side = list(reversed(matrix[width - circle_number - 1][circle_number:width - circle_number - 1]))
        spiral.extend(bottom_side)

        left_side = []
        rows_in_current_circle_for_left_side = list(reversed(matrix[circle_number + 1:width - circle_number - 1]))
        for row in rows_in_current_circle_for_left_side:
            left_side.append(row[circle_number])
        spiral.extend(left_side)

    return spiral
