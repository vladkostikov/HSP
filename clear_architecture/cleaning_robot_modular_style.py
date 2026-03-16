# Задача: реализовать программу для дистанционного управления роботом. Реализацию выполнить в модульном стиле.
# Робот должен поддерживать следующие команды(DSL): Move, Turn, Set, Start, Stop.

import math

# Класс здесь размещён условно. В соответствии с модульным подходом класс должен находиться в отдельном файле cleaning_robot_transfer.py и импортироваться в нужных местах.
class CleaningRobotTransfer:
    def __call__(self, message: str) -> str:
        return message

# Класс здесь размещён условно. В соответствии с модульным подходом класс должен находиться в отдельном файле сleaning_robot.py и импортироваться в нужных местах.
class CleaningRobot:
    CLEANING_STATES = ['water', 'soap', 'brush']

    def __init__(self, transfer):
        self.position_x = 0.0
        self.position_y = 0.0
        self.angle = 0 # 0 - вправо, 90 - вверх, 180 - влево, 270 - вниз
        self.cleaning_state = 'water'
        self.status = "stopped"
        self.transfer = transfer

    def call(self, command: str) -> str:
        command_parts = command.strip().lower().split()
        if not command_parts:
            return self._error("empty command")

        cmd = command_parts[0]
        if cmd == "start":
            return self._start()
        if cmd == "stop":
            return self._stop()

        if len(command_parts) == 1:
            return self._error("no argument")

        command_arg = command_parts[1]
        if cmd == "move":
            return self._move(command_arg)
        if cmd == "turn":
            return self._turn(command_arg)
        if cmd == "set":
            return self._set(command_arg)

        return self._error("unknown command")

    def _error(self, description: str = "") -> str:
        message = f"Error: {description}" if description else "Error"
        return message

    def _start(self) -> str:
        self.status = "running"
        return self.transfer(f"START WITH {self.cleaning_state}")

    def _stop(self) -> str:
        self.status = "stopped"
        return self.transfer("STOP")

    def _move(self, move_distance: str) -> str:
        try:
            distance = int(move_distance)
            angle_radians = math.radians(self.angle)
            self.position_x += distance * math.cos(angle_radians)
            self.position_y += distance * math.sin(angle_radians)
            x = round(self.position_x, 10)
            y = round(self.position_y, 10)
            return self.transfer(f"POS {x},{y}")
        except:
            return self._error()

    def _turn(self, turn_angle: str) -> str:
        try:
            angle = int(turn_angle)
            self.angle = (self.angle + angle) % 360
            return self.transfer(f"ANGLE {self.angle}")
        except:
            return self._error()

    def _set(self, new_state: str) -> str:
        if new_state not in self.CLEANING_STATES:
            return self._error("invalid cleaning state")

        self.cleaning_state = new_state
        return self.transfer(f"STATE {self.cleaning_state}")
