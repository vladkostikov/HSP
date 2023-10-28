def Keymaker(doors_count: int) -> str:
    doors = list(map(lambda door: False, range(doors_count)))

    for step, _door in enumerate(doors):
        current_step = doors[step:]
        current_step[::step + 1] = list(map(lambda door: (not door), current_step[::step + 1]))
        doors = doors[:step] + current_step

    return "".join(list(map(lambda door: ("1" if door else "0"), doors)))
