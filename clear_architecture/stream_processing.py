# Задание: реализовать Stream Processing

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Protocol
from enum import Enum
import math


@dataclass
class RobotState:
    x: float
    y: float
    angle: float
    state: int


class CleaningMode(Enum):
    WATER = 1
    SOAP = 2
    BRUSH = 3


class Event(ABC):
    @abstractmethod
    def apply(self, state: RobotState) -> RobotState:
        pass

    @abstractmethod
    def get_event_type(self) -> str:
        pass


class EventSubscriber(Protocol):
    def __call__(self, event: Event) -> None:
        ...

class RobotRequestEvent(Event):
    def apply(self, state: RobotState) -> RobotState:
        return state

    def get_event_type(self) -> str:
        ...


@dataclass
class RobotMoveRequestEvent(RobotRequestEvent):
    distance: float

    def get_event_type(self) -> str:
        return f'ROBOT_MOVE_REQUEST {self.distance}'


@dataclass
class RobotTurnRequestEvent(RobotRequestEvent):
    angle: float

    def get_event_type(self) -> str:
        return f'ROBOT_TURN_REQUEST {self.angle}'


@dataclass
class RobotSetStateRequestEvent(RobotRequestEvent):
    new_state: CleaningMode

    def get_event_type(self) -> str:
        return f'ROBOT_SET_STATE_REQUEST {self.new_state.name}'


@dataclass
class RobotStartRequestEvent(RobotRequestEvent):
    def get_event_type(self) -> str:
        return 'ROBOT_START_REQUEST'


@dataclass
class RobotStopRequestEvent(RobotRequestEvent):
    def get_event_type(self) -> str:
        return 'ROBOT_STOP_REQUEST'


@dataclass
class RobotMovedEvent(Event):
    distance: float

    def apply(self, state: RobotState) -> RobotState:
        angle_rads = state.angle * (math.pi/180.0)
        return RobotState(
            x=state.x + self.distance * math.cos(angle_rads),
            y=state.y + self.distance * math.sin(angle_rads),
            angle=state.angle,
            state=state.state
        )

    def get_event_type(self) -> str:
        return f'ROBOT_MOVED {self.distance}'


@dataclass
class RobotTurnedEvent(Event):
    angle: float

    def apply(self, state: RobotState) -> RobotState:
        return RobotState(
            x=state.x,
            y=state.y,
            angle=state.angle + self.angle,
            state=state.state
        )

    def get_event_type(self) -> str:
        return f'ROBOT_TURNED {self.angle}'


@dataclass
class RobotStateChangedEvent(Event):
    new_state: CleaningMode

    def apply(self, state: RobotState) -> RobotState:
        return RobotState(
            x=state.x,
            y=state.y,
            angle=state.angle,
            state=self.new_state.value
        )

    def get_event_type(self) -> str:
        return f'ROBOT_STATE_CHANGED {self.new_state.name}'


@dataclass
class RobotStartedEvent(Event):
    def apply(self, state: RobotState) -> RobotState:
        return state

    def get_event_type(self) -> str:
        return 'ROBOT_STARTED'


@dataclass
class RobotStoppedEvent(Event):
    def apply(self, state: RobotState) -> RobotState:
        return state

    def get_event_type(self) -> str:
        return 'ROBOT_STOPPED'


class Command(Protocol):
    def handle(self) -> List[Event]:
        ...

    def get_command_type(self) -> str:
        ...


@dataclass
class MoveCommand:
    distance: float

    def handle(self) -> List[Event]:
        return [RobotMoveRequestEvent(self.distance)]

    def get_command_type(self) -> str:
        return f'MOVE {self.distance}'


@dataclass
class TurnCommand:
    angle: float

    def handle(self) -> List[Event]:
        return [RobotTurnRequestEvent(self.angle)]

    def get_command_type(self) -> str:
        return f'TURN {self.angle}'


@dataclass
class SetStateCommand:
    new_state: CleaningMode

    def handle(self) -> List[Event]:
        return [RobotSetStateRequestEvent(self.new_state)]

    def get_command_type(self) -> str:
        return f'SET_STATE {self.new_state.name}'


@dataclass
class StartCommand:
    def handle(self) -> List[Event]:
        return [RobotStartRequestEvent()]

    def get_command_type(self) -> str:
        return 'START'


@dataclass
class StopCommand:
    def handle(self) -> List[Event]:
        return [RobotStopRequestEvent()]

    def get_command_type(self) -> str:
        return 'STOP'


class EventStore:
    def __init__(self):
        self._events: dict[str, List[Event]] = {}
        self._subscribers: List[EventSubscriber] = []

    def subscribe(self, callback: EventSubscriber) -> None:
        self._subscribers.append(callback)

    def append_events(self, robot_id: str, events: List[Event]) -> None:
        if robot_id not in self._events:
            self._events[robot_id] = []
        self._events[robot_id].extend(events)

        for event in events:
            for subscriber in self._subscribers:
                subscriber(event)

    def get_events(self, robot_id: str) -> List[Event]:
        return self._events.get(robot_id, [])


class StateProjector:
    def __init__(self, initial_state: RobotState):
        self._initial_state = initial_state

    def project_state(self, events: List[Event]) -> RobotState:
        current_state = self._initial_state
        for event in events:
            current_state = event.apply(current_state)
        return current_state


class Logger:
    def __init__(self):
        self._log: List[str] = []

    def call(self, message: str) -> None:
        self._log.append(message)

    def get_log(self) -> List[str]:
        return self._log


class LoggerProcessor:
    def __init__(self, event_store: EventStore, logger: Logger):
        self._event_store = event_store
        self._logger = logger
        self._event_store.subscribe(self)

    def __call__(self, event: Event) -> None:
        self._logger.call(event.get_event_type())


class BusinessLogicProcessor:
    def __init__(self, event_store: EventStore, robot_id: str):
        self._event_store = event_store
        self._robot_id = robot_id
        self._event_store.subscribe(self)

    def __call__(self, event: Event) -> None:
        if isinstance(event, RobotMoveRequestEvent):
            result = RobotMovedEvent(event.distance)
            self._event_store.append_events(self._robot_id, [result])
        elif isinstance(event, RobotTurnRequestEvent):
            result = RobotTurnedEvent(event.angle)
            self._event_store.append_events(self._robot_id, [result])
        elif isinstance(event, RobotSetStateRequestEvent):
            result = RobotStateChangedEvent(event.new_state)
            self._event_store.append_events(self._robot_id, [result])
        elif isinstance(event, RobotStartRequestEvent):
            result = RobotStartedEvent()
            self._event_store.append_events(self._robot_id, [result])
        elif isinstance(event, RobotStopRequestEvent):
            result = RobotStoppedEvent()
            self._event_store.append_events(self._robot_id, [result])


class CommandHandler:
    def __init__(self, event_store: EventStore, logger: Logger):
        self._event_store = event_store
        self._logger = logger

    def handle_command(self, robot_id: str, command: Command) -> None:
        self._logger.call(command.get_command_type())
        events = command.handle()
        if events:
            self._event_store.append_events(robot_id, events)


if __name__ == "__main__":
    event_store = EventStore()
    robot_id = "robot_001"
    logger = Logger()

    logger_processor = LoggerProcessor(event_store, logger)
    logic_processor = BusinessLogicProcessor(event_store, robot_id)
    command_handler = CommandHandler(event_store, logger)

    commands = [
        MoveCommand(100),
        TurnCommand(-90),
        SetStateCommand(CleaningMode.SOAP),
        StartCommand(),
        MoveCommand(50),
        StopCommand()
    ]

    for cmd in commands:
        command_handler.handle_command(robot_id, cmd)

    for i, entry in enumerate(logger.get_log()):
        print(f"{i+1}: {entry}")

    initial_state = RobotState(x=0.0, y=0.0, angle=0.0, state=CleaningMode.WATER.value)
    projector = StateProjector(initial_state)
    events = event_store.get_events(robot_id)
    final_state = projector.project_state(events)
    print(f"\nInitial: {initial_state}") # RobotState(x=0.0, y=0.0, angle=0.0, state=1)
    print(f"Final:   {final_state}") # RobotState(x=100.0, y=-50.0, angle=-90.0, state=2)
