def TankRush(_rows1: int, _columns1: int, map_main: str, rows2: int, _columns2: int, map_tanks: str) -> bool:
    main_map = map_main.split(" ")
    tanks_map = map_tanks.split(" ")

    for index_main_map, _v1 in enumerate(main_map):
        counter = 0
        for index_tanks_map, _v2 in enumerate(tanks_map):
            if index_main_map + index_tanks_map > len(main_map) - 1:
                break
            new_indexes = set(find_substrings_in_string(main_map[index_main_map + index_tanks_map], tanks_map[index_tanks_map]))
            if index_tanks_map == 0:
                indexes = new_indexes
            if index_tanks_map > 0:
                indexes = indexes & new_indexes
            if len(indexes) == 0:
                counter = 0
                break
            if len(indexes) > 0:
                counter += 1
            if counter >= rows2:
                return True

    if counter >= rows2:
        return True
    return False


def find_substrings_in_string(string: str, substring: str) -> list:
    indexes = []
    for i, _v in enumerate(string):
        index = string.find(substring, i)
        if index >= 0 and index not in indexes:
            indexes.append(index)
    return indexes
