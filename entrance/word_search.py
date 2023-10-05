def WordSearch(alignment_width: int, string: str, substring: str) -> list:
    splitted_string = string.split(" ")
    merged_rows_by_alignment_width = merge_rows_by_alignment_width(alignment_width, splitted_string)
    filtered_rows = filter_rows(merged_rows_by_alignment_width)
    substring_in_lines = check_strings_for_substring(filtered_rows, substring)
    return substring_in_lines


def merge_rows_by_alignment_width(alignment_width: int, splitted_string: list) -> list:
    merged_rows_by_alignment_width = []
    for i, string in enumerate(splitted_string):
        if i == 0:
            short_lines = split_string_by_alignment_width(string, alignment_width)
            merged_rows_by_alignment_width.extend(short_lines)
        elif len(" ".join(merged_rows_by_alignment_width[-1] + [string])) <= alignment_width:
            merged_rows_by_alignment_width[-1].append(string)
        elif len(string) > alignment_width:
            short_lines = split_string_by_alignment_width(string, alignment_width)
            merged_rows_by_alignment_width.extend(short_lines)
        else:
            merged_rows_by_alignment_width.append([string])
    return merged_rows_by_alignment_width


def check_strings_for_substring(merged_rows_by_alignment_width: list, substring: str) -> list:
    result = []
    for _i, line in enumerate(merged_rows_by_alignment_width):
        if substring in line:
            result.append(1)
        else:
            result.append(0)
    return result


def split_string_by_alignment_width(string: str, alignment_width: int) -> list:
    short_strings = []
    start_index = 0
    end_index = alignment_width
    for _i in string[::alignment_width]:
        short_strings.append([string[start_index:end_index]])
        start_index += alignment_width
        end_index += alignment_width
    return short_strings


# Delete empty lines
def filter_rows(rows: list) -> list:
    filtered_rows = []
    for row in rows:
        if len(row[0]) > 0:
            filtered_rows.append(row)
        else:
            continue
    return filtered_rows
