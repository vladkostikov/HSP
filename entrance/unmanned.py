def Unmanned(length_of_road: int, _traffic_lights: int, track: list) -> int:
    stopping_time = 0
    for _i, traffic_light in enumerate(track):
        time_to_current_traffic_light = traffic_light[0]
        red_light_time = traffic_light[1]
        green_light_time = traffic_light[2]
        traffic_light_cycle = red_light_time + green_light_time
        current_time = time_to_current_traffic_light + stopping_time

        time_on_traffic_light = current_time % traffic_light_cycle
        red_light_range = range(0, red_light_time)

        if time_on_traffic_light in red_light_range:
            waiting_time = red_light_time - time_on_traffic_light
            stopping_time += waiting_time

    total_time = stopping_time + length_of_road
    return total_time
