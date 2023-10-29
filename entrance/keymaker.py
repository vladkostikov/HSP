def Keymaker(doors_count: int) -> str:
    # Генерирую массив закрытых дверей.
    doors = list(map(lambda door: False, range(doors_count)))

    # Нахожу количество открытых дверей. Это квадратный корень из количества дверей.
    open_doors_count = int(doors_count ** 0.5)

    # Нахожу позиции открытых дверей. Это массив от 1 до "количества открытых дверей",
    # где каждый элемент возведён в квадрат. То есть 1, 4, 9, 16, 25, 36, 49 и т.д.
    open_doors_positions = []
    for open_door_number in list(range(1, open_doors_count + 1)):
        open_doors_positions.append(open_door_number ** 2)

    # Устанавливаю для открытых дверей значение True.
    for position in open_doors_positions:
        doors[position - 1] = True

    # Возвращаю результат в виде строки, где 0 - закрытая дверь, 1 - открытая дверь.
    return "".join(list(map(lambda door: ("1" if door else "0"), doors)))
