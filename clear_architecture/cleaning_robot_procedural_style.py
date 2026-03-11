# Задача: реализовать программу для дистанционного управления роботом. Реализацию выполнить с помощью функций, без использования классов.
# Робот должен поддерживать следующие команды(DSL): Move, Turn, Set, Start, Stop.

import math

CLEANING_STATES = ['water', 'soap', 'brush']

def create_robot() -> dict:
    return {
        "position_x": 0.0,
        "position_y": 0.0,
        "angle": 0, # 0 - смотрим направо, 90 - смотрим вверх, 180 - смотрим влево, 270 - смотрим вниз
        "cleaning_state": 'water',
        "status": "stop",
    }

def call_robot(robot, command) -> str:
    parts = command.strip().lower().split()
    if not parts:
        return "Error"

    cmd = parts[0]
    if cmd == "move":
        return _move(robot, parts)
    if cmd == "turn":
        return _turn(robot, parts)
    if cmd == "set":
        return _set(robot, parts)
    if cmd == "start":
        return _start(robot)
    if cmd == "stop":
        return _stop(robot)
    return "Error"

def _move(robot, parts) -> str:
    if len(parts) != 2:
        return "Error"

    try:
        distance = int(parts[1])
        angle_radians = robot["angle"] * (math.pi/180.0)
        robot["position_x"] += distance * math.cos(angle_radians)
        robot["position_y"] += distance * math.sin(angle_radians)
        x = round(robot["position_x"], 10)
        y = round(robot["position_y"], 10)
        return f"POS {x},{y}"
    except:
        return "Error"

def _turn(robot, parts) -> str:
    if len(parts) != 2:
        return "Error"

    try:
        angle = int(parts[1])
        robot["angle"] = (robot["angle"] + angle) % 360
        return f"ANGLE {robot['angle']}"
    except:
        return "Error"

def _set(robot, parts) -> str:
    if len(parts) != 2:
        return "Error"

    state = parts[1]
    if state not in CLEANING_STATES:
        return "Error"

    robot["cleaning_state"] = state
    return f"STATE {robot['cleaning_state']}"

def _start(robot) -> str:
    robot["status"] = "start"
    return f"START WITH {robot['cleaning_state']}"

def _stop(robot) -> str:
    robot["status"] = "stop"
    return "STOP"
