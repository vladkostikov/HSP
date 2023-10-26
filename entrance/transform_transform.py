def TransformTransform(input_array: list, length: int) -> bool:
    primary_array = transformative_transformation(input_array, length)
    secondary_array = transformative_transformation(primary_array, len(primary_array))
    master_key = sum(secondary_array)
    return master_key % 2 == 0


def transformative_transformation(input_array: list, length: int) -> list:
    output_array = []
    for i, _i_value in enumerate(input_array[:length]):
        for j, _j_value in enumerate(input_array[:length - i]):
            k = i + j
            if len(input_array[j:k + 1]) > 0:
                maximum_value_from_range = max(input_array[j:k + 1])
                output_array.append(maximum_value_from_range)
    return output_array
