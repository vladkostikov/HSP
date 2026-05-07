# Задание: реализовать управление роботом с помощью монады состояний и списка возможностей (capabilities).

import math
from collections import namedtuple

RobotState = namedtuple("RobotState", "x y angle state water_level soap_level")

WATER = 1
SOAP = 2
BRUSH = 3

class Boundary:
    SIZE = 100

    @staticmethod
    def check(x: float, y: float) -> tuple[float, float, bool]:
        constrained_x = max(0, min(Boundary.SIZE, x))
        constrained_y = max(0, min(Boundary.SIZE, y))
        is_blocked = x != constrained_x or y != constrained_y
        return constrained_x, constrained_y, is_blocked

    @staticmethod
    def can_move(x: float, y: float, angle: float, dist: float) -> bool:
        angle_rads = angle * (math.pi / 180.0)
        next_x = x + dist * math.cos(angle_rads)
        next_y = y + dist * math.sin(angle_rads)
        return 0 <= next_x <= Boundary.SIZE and 0 <= next_y <= Boundary.SIZE

class RobotStateMonad:
    def __init__(self, state, log=None):
        self.state = state
        self.log = log or []

    @property
    def capabilities(self):
        return {
            'move': Boundary.can_move(self.state.x, self.state.y, self.state.angle, 1),
            'turn': True,
            'set_water': self.state.water_level > 0,
            'set_soap': self.state.soap_level > 0,
            'start': True,
            'stop': True
        }

    def bind(self, func):
        new_state, new_log = func(self.state, self.log)
        return RobotStateMonad(new_state, new_log)

def move(dist):
    def inner(old_state, log):
        angle_rads = old_state.angle * (math.pi / 180.0)
        possible_x = old_state.x + dist * math.cos(angle_rads)
        possible_y = old_state.y + dist * math.sin(angle_rads)
        constrained_x, constrained_y, is_blocked = Boundary.check(possible_x, possible_y)
        new_state = RobotState(
            x=constrained_x,
            y=constrained_y,
            angle=old_state.angle,
            state=old_state.state,
            water_level=max(0, old_state.water_level - (dist * 0.1)) if old_state.state == WATER else old_state.water_level,
            soap_level=max(0, old_state.soap_level - (dist * 0.1)) if old_state.state == SOAP else old_state.soap_level
        )
        if is_blocked:
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
        if new_mode == WATER and old_state.water_level <= 0:
            return old_state, log + [f'FAILED to set state {new_mode} due to resource constraints']
        elif new_mode == SOAP and old_state.soap_level <= 0:
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

if __name__ == "__main__":
    initial_state = RobotStateMonad(RobotState(x=0.0, y=0.0, angle=0, state=WATER, water_level=15.0, soap_level=9.0))

    result = (initial_state
        .bind(move(100))
        .bind(turn(90))
        .bind(set_state(SOAP))
        .bind(start)
        .bind(move(101))
        .bind(stop))

    print(f"Log: {result.log}")
    # Log: ['POS(100,0)', 'ANGLE 90', 'STATE 2', 'START', 'BARRIER at (100,101)', 'STOP']
    print(f"Final state: {result.state}")
    # Final state: RobotState(x=100, y=100, angle=90, state=2, water_level=5.0, soap_level=0)
    print(f"Final capabilities: {result.capabilities}")
    # Final capabilities: {'move': False, 'turn': True, 'set_water': True, 'set_soap': False, 'start': True, 'stop': True}

    at_barrier_with_empty_resources = RobotStateMonad(RobotState(x=100.0, y=50.0, angle=0, state=WATER, water_level=0.0, soap_level=0.0))
    print(f"At barrier with empty resources (x=100, angle=0) capabilities: {at_barrier_with_empty_resources.capabilities}")
    # At barrier with empty resources (x=100, angle=0) capabilities: {'move': False, 'turn': True, 'set_water': False, 'set_soap': False, 'start': True, 'stop': True}
