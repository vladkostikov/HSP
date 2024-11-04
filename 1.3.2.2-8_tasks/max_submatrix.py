def max_submatrix(n: int, matrix: list) -> str:
    row_index_max = 0
    column_index_max = 0
    size_of_max_submatrix = 0
    sum_of_submatrix = None

    sum_of_elements = calculate_sum_of_elements_from_start(n, matrix)

    for size_matrix in range(2, n):
        for row in range(n - size_matrix + 1):
            for column in range(n - size_matrix + 1):
                sum_of_matrix = calculate_sum_of_matrix(sum_of_elements, row, column, size_matrix)
                if sum_of_submatrix is None or sum_of_matrix > sum_of_submatrix:
                    column_index_max = column
                    row_index_max = row
                    size_of_max_submatrix = size_matrix
                    sum_of_submatrix = sum_of_matrix

    return f"{column_index_max} {row_index_max} {size_of_max_submatrix}"


def calculate_sum_of_elements_from_start(n: int, matrix: list) -> list:
    sum_matrix = [[None for _column in range(n)] for _row in range(n)]

    for row_index in range(n):
        for column_index in range(n):
            sum_matrix[row_index][column_index] = calculate_sum_of_elements(matrix, row_index, column_index)

    return sum_matrix


def calculate_sum_of_elements(matrix: list, row_end_index: int, column_end_index: int) -> int:
    row_start_index = 0
    column_start_index = 0
    sum_of_matrix = 0

    for row in matrix[row_start_index:row_end_index + 1]:
        sum_of_matrix += sum(row[column_start_index:column_end_index + 1])

    return sum_of_matrix


def calculate_sum_of_matrix(sum_of_elements: list, row_start_index: int, column_start_index: int,
                            size_matrix: int) -> int:
    row_end_index = row_start_index + size_matrix - 1
    column_end_index = column_start_index + size_matrix - 1

    sum_of_matrix = 0
    sum_of_matrix += sum_of_elements[row_end_index][column_end_index]

    if row_start_index > 0:
        sum_of_matrix -= sum_of_elements[row_start_index - 1][column_end_index]
    if column_start_index > 0:
        sum_of_matrix -= sum_of_elements[row_end_index][column_start_index - 1]
    if row_start_index > 0 and column_start_index > 0:
        sum_of_matrix += sum_of_elements[row_start_index - 1][column_start_index - 1]

    return sum_of_matrix
