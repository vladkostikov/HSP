# Задание: реализовать схему функциональной инъекции с одной функцией вместо пяти, используя базовый модуль pure_robot.py.

from pure_robot import RobotState, WATER
import pure_robot

class RobotApi:
    def setup(self, f_handler, f_transfer):
        self.f_handler = f_handler
        self.f_transfer = f_transfer

    def make(self, command):
        if not hasattr(self, 'cleaner_state'):
            self.cleaner_state = RobotState(0.0, 0.0, 0, WATER)

        new_state = self.f_handler(command, self.f_transfer, self.cleaner_state)
        self.cleaner_state = new_state
        return new_state

    def __call__(self, command):
        return self.make(command)

def robot_handler(command, transfer, state):
    cmd = command.split(' ')
    if cmd[0]=='move':
        state = pure_robot.move(transfer,int(cmd[1]), state)
    elif cmd[0]=='turn':
        state = pure_robot.turn(transfer,int(cmd[1]), state)
    elif cmd[0]=='set':
        state = pure_robot.set_state(transfer,cmd[1], state)
    elif cmd[0]=='start':
        state = pure_robot.start(transfer, state)
    elif cmd[0]=='stop':
        state = pure_robot.stop(transfer, state)
    return state

def fake_transfer(message):
    return message

api = RobotApi()
api.setup(robot_handler, fake_transfer)

# ===== Дополнительный обработчик для теста двойного перемещения робота =====

def double_move_robot_handler(command, transfer, state):
    cmd = command.split(' ')
    if cmd[0]=='move':
            state = pure_robot.move(transfer,int(cmd[1])*2, state)
            return state

    return robot_handler(command, transfer, state)

# api.setup(double_move_robot_handler, fake_transfer)
