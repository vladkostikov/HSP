def odometer(speeds_and_times: list) -> int:
    speeds = speeds_and_times[::2]
    times = speeds_and_times[1::2]

    distance = speeds[0] * times[0]

    for i, x in enumerate(speeds):
        if i == 0:
            continue

        speed = speeds[i]
        time = times[i] - times[i-1]

        distance += speed * time

    return distance
