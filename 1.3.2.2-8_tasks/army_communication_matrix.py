def army_communication_matrix(n: int, matrix: list) -> str:
    x_coordinate_max = 0
    y_coordinate_max = 0
    size_of_max_submatrix = 0
    sum_of_submatrix_elements = None

    x_start_index = 0
    y_start_index = 0
    x_end_index = n - 1
    y_end_index = n - 1
    for step in range(n // 2):
        is_first_row_smaller = is_first_row_smaller_than_last_row(matrix, x_start_index, y_start_index,
                                                                  x_end_index, y_end_index)
        is_first_column_smaller = is_first_column_smaller_than_last_column(matrix, x_start_index, y_start_index,
                                                                           x_end_index, y_end_index)

        if is_first_row_smaller:
            y_start_index += 1
        else:
            y_end_index -= 1

        if is_first_column_smaller:
            x_start_index += 1
        else:
            x_end_index -= 1

        current_sum_of_matrix_elements = find_sum_of_elements(matrix, x_start_index, y_start_index,
                                                              x_end_index, y_end_index)
        if sum_of_submatrix_elements is None or current_sum_of_matrix_elements > sum_of_submatrix_elements:
            x_coordinate_max = x_start_index
            y_coordinate_max = y_start_index
            size_of_max_submatrix = n - step - 1
            sum_of_submatrix_elements = current_sum_of_matrix_elements

    return f"{x_coordinate_max} {y_coordinate_max} {size_of_max_submatrix}"


def is_first_row_smaller_than_last_row(matrix: list, x_start_index: int, y_start_index: int,
                                       x_end_index: int, y_end_index: int) -> bool:
    sum_of_first_row = sum(matrix[y_start_index][x_start_index:x_end_index + 1])
    sum_of_last_row = sum(matrix[y_end_index][x_start_index:x_end_index + 1])

    if sum_of_first_row < sum_of_last_row:
        return True
    return False


def is_first_column_smaller_than_last_column(matrix: list, x_start_index: int, y_start_index: int,
                                             x_end_index: int, y_end_index: int) -> bool:
    sum_of_first_column = 0
    for row in matrix[y_start_index:y_end_index + 1]:
        sum_of_first_column += row[x_start_index]

    sum_of_last_column = 0
    for row in matrix[y_start_index:y_end_index + 1]:
        sum_of_last_column += row[x_end_index]

    if sum_of_first_column < sum_of_last_column:
        return True
    return False


def find_sum_of_elements(matrix: list, x_start_index: int, y_start_index: int,
                         x_end_index: int, y_end_index: int) -> int:
    sum_of_elements = 0
    for row in matrix[y_start_index:y_end_index + 1]:
        sum_of_elements += sum(row[x_start_index:x_end_index + 1])

    return sum_of_elements
