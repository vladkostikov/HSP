def Football(footballers: list, _count: int) -> bool:
    sorted_footballers = sorted(footballers)

    if footballers == sorted_footballers:
        return True

    if swap_two_football_players(footballers, sorted_footballers):
        return True

    if reverse_any_section(footballers, sorted_footballers):
        return True

    return False


def swap_two_football_players(footballers: list, sorted_footballers: list) -> bool:
    new_placement = footballers[:]
    for i, _footballer in enumerate(footballers[:-1]):
        if footballers[i] < footballers[i + 1]:
            continue

        minimum_number_in_the_following_indexes = min(footballers[i + 1:])
        minimum_number_index = footballers.index(minimum_number_in_the_following_indexes)
        new_placement[i], new_placement[minimum_number_index] \
            = new_placement[minimum_number_index], new_placement[i]

        if new_placement == sorted_footballers:
            return True
        new_placement = footballers[:]
    return False


def reverse_any_section(footballers: list, sorted_footballers: list) -> bool:
    for i, _footballer in enumerate(footballers[:-1]):
        if footballers[i] < footballers[i + 1]:
            continue

        end_index = i + 2
        for _footballer2 in footballers[i:]:
            new_placement = (footballers[:i]
                             + list(reversed(footballers[i:end_index]))
                             + footballers[end_index:])
            if new_placement == sorted_footballers:
                return True
            end_index += 1
    return False
