# Задание: реализовать управление роботом в конкатенативном стиле, используя базовый модуль pure_robot.py.
# Клиент передает на вход workflow единой строкой-стримом в постфиксной нотации, а на выходе получает состояние робота после выполнения всех команд.
# Input: "100 move -90 turn soap set start 50 move stop"

from typing import Any

from pure_robot import RobotState, WATER
import pure_robot

ALLOWED_COMMANDS = ['move', 'turn', 'set', 'start', 'stop']

class RobotAPI:
    def __init__(self, transfer, state=RobotState(x=0.0, y=0.0, angle=0, state=WATER)):
        self.transfer = transfer
        self.state = state

    def __call__(self, command: str) -> RobotState:
        return self._make(command)

    def _parse_commands(self, commands: str) -> list[tuple[str, Any]]:
        cmd = commands.split(' ')
        parsed_commands = []
        parsed_actions = []
        parsed_values = []
        for arg in cmd:
            if arg in ALLOWED_COMMANDS:
                parsed_actions.append(arg)
            else:
                parsed_values.append(arg)

            if len(parsed_actions) > 0:
                action = parsed_actions[0]
                values = list(reversed(parsed_values))
                parsed_commands.append(tuple([action, values]))
                parsed_actions = []
                parsed_values = []
        return parsed_commands

    def _make(self, commands: str) -> RobotState:
        parsed_commands = self._parse_commands(commands)
        for action, values in parsed_commands:
            if action=='move':
                self.state = pure_robot.move(self.transfer, int(list(values)[0]), self.state)
            elif action=='turn':
                self.state = pure_robot.turn(self.transfer, int(list(values)[0]), self.state)
            elif action=='set':
                self.state = pure_robot.set_state(self.transfer, list(values)[0], self.state)
            elif action=='start':
                self.state = pure_robot.start(self.transfer, self.state)
            elif action=='stop':
                self.state = pure_robot.stop(self.transfer, self.state)
        return self.state
