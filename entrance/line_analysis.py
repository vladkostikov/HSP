def LineAnalysis(line: str) -> bool:
    match_stars = "*"
    for i, _v in enumerate(line[:-1]):
        if line[i] != line[i + 1]:
            break
        match_stars += line[i + 1]

    splitted_line = line.split(match_stars)[1:-1]

    length = len(splitted_line)
    if length == 0:
        return True

    first_match = splitted_line[0]
    counter = splitted_line.count(first_match)

    return counter == length
