# В файле pure_robot.py реализована функциональность робота.
# Задание: создать API для этого модуля в любом стиле. Все особенности оригинальной реализации должны быть скрыты от пользователя.

from pure_robot import *

def fake_transfer(message):
    return message

database = {}

class PureRobotDatabase:
    def __init__(self, database: dict):
        self.db = database

    def find_or_create(self, id: str) -> RobotState:
        if id not in self.db:
            self.update(id, RobotState(x=0.0, y=0.0, angle=0, state=WATER))
        return self.db[id]

    read = find_or_create

    def update(self, id: str, state: RobotState) -> RobotState:
        self.db[id] = state
        return self.db[id]

class PureRobotAPI:
    def __init__(self, id: str):
        self.robot_id = id
        self.db = PureRobotDatabase(database)
        self.transfer = fake_transfer
        self.db.find_or_create(id)

    def current_state(self) -> RobotState:
        return self.db.read(self.robot_id)

    def move(self, distance: float) -> RobotState:
        new_state = move(self.transfer, distance, self.current_state())
        self.db.update(self.robot_id, new_state)
        return new_state

    def turn(self, angle: float) -> RobotState:
        new_state = turn(self.transfer, angle, self.current_state())
        self.db.update(self.robot_id, new_state)
        return new_state

    def set_cleaning_state(self, new_cleaning_state: str) -> RobotState:
        new_state = set_state(self.transfer, new_cleaning_state, self.current_state())
        self.db.update(self.robot_id, new_state)
        return new_state

    def start(self) -> RobotState:
        new_state = start(self.transfer, self.current_state())
        self.db.update(self.robot_id, new_state)
        return new_state

    def stop(self) -> RobotState:
        self.transfer(('STOP',))
        return self.current_state()
