# Задание: реализовать паттерн Event Sourcing для управления роботом.

import pure_robot
from pure_robot import RobotState, WATER, SOAP
from pure_robot_api import fake_transfer

class Event: pass

class MoveEvent(Event):
    def __init__(self, distance: float):
        self.distance = distance

class TurnEvent(Event):
    def __init__(self, angle: float):
        self.angle = angle

class SetCleaningStateEvent(Event):
    def __init__(self, cleaning_state: str):
        self.cleaning_state = cleaning_state

class StartEvent(Event): pass

class StopEvent(Event): pass

class EventStore:
    def __init__(self):
        self.events = []

    def save(self, new_events: list[Event]):
        self.events.extend(new_events)

class EventExecutor:
    def __init__(self, event_store: EventStore):
        self.event_store = event_store

    def execute(self) -> RobotState:
        current_state = pure_robot.RobotState(x=0.0, y=0.0, angle=0.0, state=pure_robot.WATER)
        for event in self.event_store.events:
            if isinstance(event, MoveEvent):
                current_state = pure_robot.move(fake_transfer, event.distance, current_state)
            elif isinstance(event, TurnEvent):
                current_state = pure_robot.turn(fake_transfer, event.angle, current_state)
            elif isinstance(event, SetCleaningStateEvent):
                current_state = pure_robot.set_state(fake_transfer, event.cleaning_state, current_state)
            elif isinstance(event, StartEvent):
                current_state = pure_robot.start(fake_transfer, current_state)
            elif isinstance(event, StopEvent):
                current_state = pure_robot.stop(fake_transfer, current_state)
        return current_state

class CommandHandler:
    def __init__(self, event_store: EventStore):
        self.event_store = event_store

    def handle(self, command):
        cmd = command.split(' ')[0]
        if cmd == 'move':
            distance = float(command.split(' ')[1])
            event = MoveEvent(distance)
            self.event_store.save([event])
        elif cmd == 'turn':
            angle = float(command.split(' ')[1])
            event = TurnEvent(angle)
            self.event_store.save([event])
        elif cmd == 'set':
            cleaning_state = command.split(' ')[1]
            event = SetCleaningStateEvent(cleaning_state)
            self.event_store.save([event])
        elif cmd == 'start':
            event = StartEvent()
            self.event_store.save([event])
        elif cmd == 'stop':
            event = StopEvent()
            self.event_store.save([event])
        elif cmd == 'current_state':
            return EventExecutor(self.event_store).execute()

class Client:
    def __init__(self, command_handler: CommandHandler):
        self.command_handler = command_handler

    def send_command(self, command):
        self.command_handler.handle(command)

    def get_current_state(self):
        return self.command_handler.handle('current_state')

if __name__ == "__main__":
    event_store = EventStore()
    command_handler = CommandHandler(event_store)
    client = Client(command_handler)

    print(client.get_current_state()) # RobotState(x=0.0, y=0.0, angle=0.0, state=pure_robot.WATER)
    client.send_command("move 100")
    client.send_command("turn -90")
    client.send_command("set soap")
    client.send_command("start")
    client.send_command("move 50")
    client.send_command("stop")
    print(client.get_current_state()) # RobotState(x=100.0, y=-50.0, angle=-90.0, state=pure_robot.SOAP)
