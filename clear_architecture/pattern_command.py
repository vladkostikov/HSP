# Задание: реализовать паттерн Command для управления роботом, используя базовый модуль pure_robot.py.

from abc import ABC, abstractmethod
from functools import reduce

import pure_robot
from pure_robot import RobotState, WATER
from pure_robot_api import fake_transfer

class RobotCommand(ABC):
    def __init__(self, transfer = fake_transfer) -> None:
        self.transfer = transfer

    @abstractmethod
    def execute(self, state: RobotState) -> RobotState:
        pass

class MoveCommand(RobotCommand):
    def __init__(self, distance: int) -> None:
        super().__init__()
        self.distance = distance

    def execute(self, state: RobotState) -> RobotState:
        return pure_robot.move(self.transfer, self.distance, state)

class TurnCommand(RobotCommand):
    def __init__(self, angle: int) -> None:
        super().__init__()
        self.angle = angle

    def execute(self, state: RobotState) -> RobotState:
        return pure_robot.turn(self.transfer, self.angle, state)

class SetCleaningStateCommand(RobotCommand):
    def __init__(self, new_cleaning_state) -> None:
        super().__init__()
        self.new_cleaning_state = new_cleaning_state

    def execute(self, state: RobotState) -> RobotState:
        return pure_robot.set_state(self.transfer, self.new_cleaning_state, state)

class StartCommand(RobotCommand):
    def __init__(self) -> None:
        super().__init__()

    def execute(self, state: RobotState) -> RobotState:
        return pure_robot.start(self.transfer, state)

class StopCommand(RobotCommand):
    def __init__(self) -> None:
        super().__init__()

    def execute(self, state: RobotState) -> RobotState:
        return pure_robot.stop(self.transfer, state)

class Robot:
    @staticmethod
    def execute_commands(commands: list[RobotCommand], initial_state: RobotState) -> RobotState:
        return reduce(lambda current_state, command: command.execute(current_state), commands, initial_state)

if __name__ == "__main__":
    commands = [
        MoveCommand(10),
        TurnCommand(90),
        SetCleaningStateCommand('soap'),
        StartCommand(),
        MoveCommand(50),
        StopCommand()
    ]

    initial_state = RobotState(x=0.0, y=0.0, angle=0, state=WATER)
    final_state = Robot.execute_commands(commands, initial_state)

    print(final_state)  # RobotState(x=10.0, y=50.0, angle=90, state=SOAP)
