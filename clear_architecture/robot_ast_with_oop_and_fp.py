# Задание: реализовать абстрактный тип данных для управления роботом, сочетающий плюсы объектно-ориентированного и функционального программирования.

from dataclasses import dataclass
from typing import Any, Callable, Tuple
from enum import Enum
import math

@dataclass
class RobotState:
    x: float
    y: float
    angle: float
    cleaning_mode: int

class CleaningMode(Enum):
    WATER = 1
    SOAP = 2
    BRUSH = 3

class Transfer:
    def __call__(self, message: str) -> Any:
        print(message)

class Robot:
    @staticmethod
    def create(transfer_fn: Transfer) -> Tuple[RobotState, Callable]:
        state = RobotState(x=0.0, y=0.0, angle=0.0, cleaning_mode=CleaningMode.WATER.value)

        def process_commands(commands: Tuple[str]) -> RobotState:
            nonlocal state
            for command in commands:
                cmd = command.split(' ')
                if cmd[0] == 'move':
                    state = Robot._move(transfer_fn, float(cmd[1]), state)
                elif cmd[0] == 'turn':
                    state = Robot._turn(transfer_fn, float(cmd[1]), state)
                elif cmd[0] == 'set':
                    state = Robot._set_state(transfer_fn, cmd[1], state)
                elif cmd[0] == 'start':
                    state = Robot._start(transfer_fn, state)
                elif cmd[0] == 'stop':
                    state = Robot._stop(transfer_fn, state)
            return state

        return state, process_commands

    @staticmethod
    def _move(transfer: Callable, dist: float, state: RobotState) -> RobotState:
        angle_rads = state.angle * (math.pi / 180.0)
        new_x = state.x + dist * math.cos(angle_rads)
        new_y = state.y + dist * math.sin(angle_rads)
        transfer(f"POS({new_x}, {new_y})")
        return RobotState(x=new_x, y=new_y, angle=state.angle, cleaning_mode=state.cleaning_mode)

    @staticmethod
    def _turn(transfer: Callable, angle: float, state: RobotState) -> RobotState:
        new_angle = state.angle + angle
        transfer(f"ANGLE({new_angle})")
        return RobotState(x=state.x, y=state.y, angle=new_angle, cleaning_mode=state.cleaning_mode)

    @staticmethod
    def _set_state(transfer: Callable, mode: str, state: RobotState) -> RobotState:
        mode_mapping = {
            'water': CleaningMode.WATER.value,
            'soap': CleaningMode.SOAP.value,
            'brush': CleaningMode.BRUSH.value
        }
        if mode not in mode_mapping:
            transfer(f"INVALID_MODE({mode})")
            return state

        new_mode = mode_mapping[mode]
        transfer(f"MODE({new_mode})")
        return RobotState(x=state.x, y=state.y, angle=state.angle, cleaning_mode=new_mode)

    @staticmethod
    def _start(transfer: Callable, state: RobotState) -> RobotState:
        transfer("START WITH MODE " + str(state.cleaning_mode))
        return state

    @staticmethod
    def _stop(transfer: Callable, state: RobotState) -> RobotState:
        transfer("STOP")
        return state

if __name__ == '__main__':
    initial_state, command_processor = Robot.create(Transfer())

    commands = (
        'move 100',
        'turn -90',
        'set soap',
        'start',
        'move 50',
        'stop'
    )

    final_state = command_processor(commands)
    print(f"Final State: {final_state}") # Final State: RobotState(x=100.0, y=-50.0, angle=-90.0, cleaning_mode=2)
