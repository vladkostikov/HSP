# Задание: попрактиковаться с dependency injection (внедрение/инъекция зависимостей). Реализовать разделение интерфейса и реализации для одного из предудыщих примеров.

from abc import ABC, abstractmethod
from pure_robot import RobotState
import pure_robot

class OutputHandler(ABC):
    @abstractmethod
    def send(self, message):
        pass

class FakeOutputHandler(OutputHandler):
    def send(self, message):
        return message

class RobotController(ABC):
    @abstractmethod
    def move(self, distance: int, state: RobotState) -> RobotState:
        pass

    @abstractmethod
    def turn(self, angle: int, state: RobotState) -> RobotState:
        pass

    @abstractmethod
    def set_state(self, new_state: str, state: RobotState) -> RobotState:
        pass

    @abstractmethod
    def start(self, state: RobotState) -> RobotState:
        pass

    @abstractmethod
    def stop(self, state: RobotState) -> RobotState:
        pass

class PureRobotController(RobotController):
    def __init__(self, output_handler: OutputHandler):
        self.output_handler = output_handler

    def move(self, distance: int, state: RobotState) -> RobotState:
        return pure_robot.move(self.output_handler.send, distance, state)

    def turn(self, angle: int, state: RobotState) -> RobotState:
        return pure_robot.turn(self.output_handler.send, angle, state)

    def set_state(self, new_state: str, state: RobotState) -> RobotState:
        return pure_robot.set_state(self.output_handler.send, new_state, state)

    def start(self, state: RobotState) -> RobotState:
        return pure_robot.start(self.output_handler.send, state)

    def stop(self, state: RobotState) -> RobotState:
        return pure_robot.stop(self.output_handler.send, state)

class PureRobotAPIDependencyInjection:
    def __init__(self, controller: RobotController, output_handler: OutputHandler, initial_state: RobotState):
        self.controller = controller
        self.output_handler = output_handler
        self.cleaner_state = initial_state

    def get_x(self):
        return self.cleaner_state.x

    def get_y(self):
        return self.cleaner_state.y

    def get_angle(self):
        return self.cleaner_state.angle

    def get_cleaning_state(self):
        return self.cleaner_state.state

    def activate_cleaner(self,code):
        for command in code:
            cmd = command.split(' ')
            if cmd[0]=='move':
                self.cleaner_state = self.controller.move(int(cmd[1]), self.cleaner_state)
            elif cmd[0]=='turn':
                self.cleaner_state = self.controller.turn(int(cmd[1]), self.cleaner_state)
            elif cmd[0]=='set':
                self.cleaner_state = self.controller.set_state(cmd[1], self.cleaner_state)
            elif cmd[0]=='start':
                self.cleaner_state = self.controller.start(self.cleaner_state)
            elif cmd[0]=='stop':
                self.cleaner_state = self.controller.stop(self.cleaner_state)
