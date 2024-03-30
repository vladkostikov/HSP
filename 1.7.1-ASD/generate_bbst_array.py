def GenerateBBSTArray(array: list) -> list:
    sorted_array = sorted(array)
    levels = _generate_bbst_array(sorted_array, {}, 0)

    balanced_array = []
    for level in levels:
        balanced_array.extend(levels[level])
    return balanced_array


def _generate_bbst_array(sorted_array, levels, depth):
    if depth not in levels:
        levels[depth] = []

    center_index = len(sorted_array) // 2
    if center_index < len(sorted_array):
        center = sorted_array[center_index]
        levels[depth].append(center)

    left_array = sorted_array[:center_index]
    if len(left_array) > 0:
        _generate_bbst_array(left_array, levels, depth + 1)

    right_array = sorted_array[center_index + 1:]
    if len(right_array) > 0:
        _generate_bbst_array(right_array, levels, depth + 1)

    return levels
