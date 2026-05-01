# Задание: сделать абстрактное синтаксическое дерево и интерпретатор для управления роботом.
# Каждая команда (Move, Turn, SetState) - это узел в дереве.
# Команда содержит параметры (например, расстояние для Move) и ссылку на следующую команду.
# Для каждой команды должен быть определен тип ответа (например, MoveResponse), который содержит результат выполнения команды.
# Каждый узел должен иметь метод interpret(), который принимает текущее состояние робота и возвращает новое состояние и ответ.

from abc import ABC, abstractmethod
from dataclasses import dataclass
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

class Node(ABC):
    @abstractmethod
    def __init__(self, parameters: dict):
        self.parameters = parameters

    def next(self, next_node: 'Node'):
        self.next_node = next_node

    @abstractmethod
    def interpret(self, state) -> tuple['RobotState', 'Response']:
        pass

class Response(ABC):
    def __init__(self, data: dict, success: str):
        self.data = data
        self.success = success

class MoveResponse(Response):
    def __init__(self, distance: float, success: str):
        super().__init__({'distance': distance}, success)

class Move(Node):
    def __init__(self, distance: float):
        super().__init__({'distance': distance})

    def interpret(self, state: RobotState) -> tuple[RobotState, MoveResponse]:
        distance = self.parameters.get('distance', 0)
        angle_rads = state.angle * (math.pi/180.0)
        new_x = state.x + distance * math.cos(angle_rads)
        new_y = state.y + distance * math.sin(angle_rads)
        new_state = RobotState(
            x=round(new_x, 10),
            y=round(new_y, 10),
            angle=state.angle,
            cleaning_mode=state.cleaning_mode)
        return (new_state, MoveResponse(distance, 'MOVE_OK'))

class TurnResponse(Response):
    def __init__(self, angle: float, success: str):
        super().__init__({'angle': angle}, success)

class Turn(Node):
    def __init__(self, angle: float):
        super().__init__({'angle': angle})

    def interpret(self, state: RobotState) -> tuple[RobotState, TurnResponse]:
        turn_angle = self.parameters.get('angle', 0)
        new_state = RobotState(
            x=state.x,
            y=state.y,
            angle=state.angle + turn_angle,
            cleaning_mode=state.cleaning_mode)
        return (new_state, TurnResponse(turn_angle, 'TURN_OK'))

class SetCleaningStateResponse(Response):
    def __init__(self, new_state: int, success: str):
        super().__init__({'new_state': new_state}, success)

class SetCleaningState(Node):
    def __init__(self, cleaning_mode: CleaningMode):
        super().__init__({'cleaning_mode': cleaning_mode})

    def interpret(self, state: RobotState) -> tuple[RobotState, SetCleaningStateResponse]:
        new_cleaning_mode = self.parameters.get('cleaning_mode')
        if not isinstance(new_cleaning_mode, CleaningMode):
            return (state, SetCleaningStateResponse(state.cleaning_mode, 'INVALID_SET_CLEANING_MODE'))

        new_state = RobotState(
            x=state.x,
            y=state.y,
            angle=state.angle,
            cleaning_mode=new_cleaning_mode.value
        )
        return (new_state, SetCleaningStateResponse(new_cleaning_mode.value, 'SET_CLEANING_MODE_OK'))

class Start(Node):
    def __init__(self):
        super().__init__({})

    def interpret(self, state: RobotState) -> tuple[RobotState, Response]:
        return (state, Response({}, 'START_OK'))

class Stop(Node):
    def __init__(self):
        super().__init__({})

    def interpret(self, state: RobotState) -> tuple[RobotState, Response]:
        return (state, Response({}, 'STOP_OK'))

if __name__ == "__main__":
    initial_state = RobotState(x=0, y=0, angle=0, cleaning_mode=CleaningMode.WATER.value)

    move_node100 = Move(100)
    turn_node = Turn(-90)
    set_state_node = SetCleaningState(CleaningMode.SOAP)
    start_node = Start()
    move_node50 = Move(50)
    stop_node = Stop()

    move_node100.next(turn_node)
    turn_node.next(set_state_node)
    set_state_node.next(start_node)
    start_node.next(move_node50)
    move_node50.next(stop_node)

    current_node = move_node100
    current_state = initial_state
    responses = []
    while current_node is not None:
        current_state, response = current_node.interpret(current_state)
        responses.append(response)
        current_node = current_node.next_node if hasattr(current_node, 'next_node') else None

    for i, response in enumerate(responses):
        print(f'{i+1}: {response.success}, Data: {response.data}')
    # 1: MOVE_OK, Data: {'distance': 100}
    # 2: TURN_OK, Data: {'angle': -90}
    # 3: SET_CLEANING_MODE_OK, Data: {'new_state': 2}
    # 4: START_OK, Data: {}
    # 5: MOVE_OK, Data: {'distance': 50}
    # 6: STOP_OK, Data: {}

    print(f'Final State: {current_state}')
    # Final State: RobotState(x=100.0, y=0.0, angle=-90, cleaning_mode=2)
