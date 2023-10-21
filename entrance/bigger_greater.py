def BiggerGreater(line: str) -> str:
    magic = list(line)
    for i, char in enumerate(magic[::-1]):
        index = find_index_with_value_less_than_the_current(magic[:len(magic) - 1 - i], char)
        if index is not None:
            magic[len(magic) - 1 - i], magic[index] = magic[index], magic[len(magic) - 1 - i]
            magic = magic[:index + 1] + sorted(magic[index + 1:])
            return "".join(magic)
    return ""


def find_index_with_value_less_than_the_current(chars: list, value: str) -> int:
    for index, char in enumerate(chars[::-1]):
        if value > char:
            return len(chars) - 1 - index
    return None
