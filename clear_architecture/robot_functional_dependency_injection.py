# Задание: реализовать функциональную инъекцию зависимостей, используя базовый модуль pure_robot.py, в котором сосредоточены ключевые функции управления роботом.

from pure_robot import RobotState, WATER
import pure_robot

class RobotFunctionalDependencyInjection:
    def __init__(self, transfer, move, turn, set_state, start, stop, make):
        self.state = RobotState(0,0,0, WATER)
        self.transfer = transfer
        self.move_function = move
        self.turn_function = turn
        self.set_state_function = set_state
        self.start_function = start
        self.stop_function = stop
        self.make_function = make

    def move(self, distance):
        new_state = self.move_function(self.transfer, distance, self.state)
        self.state = new_state
        return new_state

    def turn(self, angle):
        new_state = self.turn_function(self.transfer, angle, self.state)
        self.state = new_state
        return new_state

    def set_cleaning_state(self, state):
        new_state = self.set_state_function(self.transfer, state, self.state)
        self.state = new_state
        return new_state

    def start(self):
        new_state = self.start_function(self.transfer, self.state)
        self.state = new_state
        return new_state

    def stop(self):
        new_state = self.stop_function(self.transfer, self.state)
        self.state = new_state
        return new_state

    def make(self, code):
        new_state = self.make_function(self.transfer, code, self.state)
        self.state = new_state
        return new_state

class PureRobot(RobotFunctionalDependencyInjection):
    def __init__(self, transfer):
        super().__init__(transfer,
                         pure_robot.move,
                         pure_robot.turn,
                         pure_robot.set_state,
                         pure_robot.start,
                         pure_robot.stop,
                         pure_robot.make)
