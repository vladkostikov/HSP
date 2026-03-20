# В файле pure_robot.py реализована функциональность робота.
# Задание: создать API для этого модуля, придумать и реализовать stateless-архитектуру. Все особенности оригинальной реализации должны быть скрыты от пользователя.

# Моя предыдущая реализация pure_robot_api.py почти выполняет эти требования, поэтому я только немного улучшу ее.

from pure_robot import *

VALID_CLEANING_STATES = {'water', 'soap', 'brush'}

Result = namedtuple("Result", "ok error message position cleaning_state")

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

class PureRobotAPIStateless:
    def __init__(self, id: str):
        self.robot_id = id
        self.db = PureRobotDatabase(database)
        self.transfer = fake_transfer
        self.db.find_or_create(id)

    def _current_state(self) -> RobotState:
        return self.db.read(self.robot_id)

    def _result(self, ok=True, error=False, message="") -> Result:
        state = self._current_state()
        position = {'x': state.x, 'y': state.y, 'angle': state.angle}
        return Result(ok=ok, error=error, message=message, position=position, cleaning_state=state.state)

    def _success(self, message="") -> Result:
        return self._result(ok=True, error=False, message=message)

    def _failure(self, message="") -> Result:
        return self._result(ok=False, error=True, message=message)

    def current_state(self) -> Result:
        return self._success()

    def move(self, distance: int | float) -> Result:
        if not isinstance(distance, (int, float)):
            return self._failure(message="Invalid distance value.")

        new_state = move(self.transfer, distance, self._current_state())
        self.db.update(self.robot_id, new_state)
        return self._success()

    def turn(self, angle: int | float) -> Result:
        if not isinstance(angle, (int, float)):
            return self._failure(message="Invalid angle value.")

        new_state = turn(self.transfer, angle, self._current_state())
        self.db.update(self.robot_id, new_state)
        return self._success()

    def set_cleaning_state(self, new_cleaning_state: str) -> Result:
        if new_cleaning_state not in VALID_CLEANING_STATES:
            return self._failure(message="Invalid new cleaning state value.")

        new_state = set_state(self.transfer, new_cleaning_state, self._current_state())
        self.db.update(self.robot_id, new_state)
        return self._success()

    def start(self) -> Result:
        new_state = start(self.transfer, self._current_state())
        self.db.update(self.robot_id, new_state)
        return self._success()

    def stop(self) -> Result:
        new_state = stop(self.transfer, self._current_state())
        self.db.update(self.robot_id, new_state)
        return self._success()
