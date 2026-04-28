# Задание: доработать код так, чтобы использовались и работали MoveResponse, SetStateResponse, check_position и check_resources.

from functools import wraps
from collections import namedtuple
import math

RobotState = namedtuple("RobotState", "x y angle state water_level soap_level")

WATER = 1
SOAP = 2
BRUSH = 3

class StateMonad:
    def __init__(self, state, log=None):
        self.state = state
        self.log = log or []

    def bind(self, func):
        new_state, new_log = func(self.state, self.log)
        return StateMonad(new_state, new_log)

class MoveResponse:
    OK = "MOVE_OK"
    BARRIER = "HIT_BARRIER"

class SetStateResponse:
    OK = "STATE_OK"
    NO_WATER = "OUT_OF_WATER"
    NO_SOAP = "OUT_OF_SOAP"

def move(dist):
    def inner(old_state, log):
        angle_rads = old_state.angle * (math.pi/180.0)
        possible_x = old_state.x + dist * math.cos(angle_rads)
        possible_y = old_state.y + dist * math.sin(angle_rads)
        check_position_result = check_position(possible_x, possible_y)
        new_state = RobotState(
            x = check_position_result[0],
            y = check_position_result[1],
            angle = old_state.angle,
            state = old_state.state,
            water_level = old_state.water_level - (dist * 0.1) if old_state.state == WATER else old_state.water_level,
            soap_level = old_state.soap_level - (dist * 0.1) if old_state.state == SOAP else old_state.soap_level
        )
        if check_position_result[2] == MoveResponse.BARRIER:
            return new_state, log + [f'BARRIER at ({int(possible_x)},{int(possible_y)})']
        return new_state, log + [f'POS({int(new_state.x)},{int(new_state.y)})']
    return inner

def turn(angle):
    def inner(old_state, log):
        new_state = RobotState(
            old_state.x,
            old_state.y,
            old_state.angle + angle,
            old_state.state,
            old_state.water_level,
            old_state.soap_level
        )
        return new_state, log + [f'ANGLE {new_state.angle}']
    return inner

def set_state(new_mode):
    def inner(old_state, log):
        if check_resources(new_mode, old_state) != SetStateResponse.OK:
            return old_state, log + [f'FAILED to set state {new_mode} due to resource constraints']

        new_state = RobotState(
            old_state.x,
            old_state.y,
            old_state.angle,
            new_mode,
            old_state.water_level,
            old_state.soap_level
        )
        return new_state, log + [f'STATE {new_mode}']
    return inner

def start(old_state, log):
    return old_state, log + ['START']

def stop(old_state, log):
    return old_state, log + ['STOP']

def check_position(x: float, y: float) -> tuple[float, float, str]:
    constrained_x = max(0, min(100, x))
    constrained_y = max(0, min(100, y))

    if x == constrained_x and y == constrained_y:
        return (x, y, MoveResponse.OK)
    return (constrained_x, constrained_y, MoveResponse.BARRIER)

def check_resources(new_mode: int, state: RobotState) -> str:
    if new_mode == WATER and state.water_level <= 0:
        return SetStateResponse.NO_WATER
    elif new_mode == SOAP and state.soap_level <= 0:
        return SetStateResponse.NO_SOAP
    return SetStateResponse.OK

if __name__ == "__main__":
    initial_state = StateMonad(RobotState(x=0.0, y=0.0, angle=0, state=WATER, water_level=15.0, soap_level=9.0))
    result = (initial_state
        .bind(move(100))
        .bind(turn(-90))
        .bind(set_state(SOAP))
        .bind(start)
        .bind(move(50))
        .bind(stop))

    print(f"Final state: {result.state}") # Final state: RobotState(x=100, y=0, angle=-90, state=2, water_level=5.0, soap_level=4.0)
    print(f"Log: {result.log}") # Log: ['POS(100,0)', 'ANGLE -90', 'STATE 2', 'START', 'BARRIER at (100,-50)', 'STOP']
