def MadMax(amount: int, telemetry: list) -> list:
    sorted_numbers = sorted(telemetry)
    max_number = sorted_numbers[-1]

    left_side = sorted_numbers[:len(sorted_numbers) // 2]
    right_side = sorted_numbers[len(sorted_numbers) // 2:-1]
    right_side = list(reversed(right_side))

    starting_impulse = left_side + [max_number] + right_side

    return starting_impulse
