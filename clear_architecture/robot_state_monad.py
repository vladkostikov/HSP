# Задание: реализовать архитектуру с монадой состояния для управления роботом, используя базовый модуль pure_robot.py.
# Визуально должно получиться что-то вроде: ... >> move(100) >> turn(-90) >> set_state(SOAP) >> ...

from typing import Any, Callable, Tuple
from pure_robot_api import fake_transfer
import pure_robot

class State:
    def __init__(self, value):
        self.value = value

class StateMonad:
    def __init__(self, func: Callable[['State'], Tuple[Any, 'State']]):
        self.func = func

    # Соединяет текущую монаду с следующей
    def bind(self, next_func: Callable[[Any], 'StateMonad']) -> 'StateMonad':
        def bound(state: State) -> Tuple[Any, State]:
            # Выполняем текущую функцию монады над состоянием
            current_value, next_state = self.func(state)

            # Создаём следующую монаду на основе результата текущей
            next_monad = next_func(current_value)

            # Выполняем следующую монаду уже на обновлённом состоянии
            return next_monad.func(next_state)
        return StateMonad(bound)

    # Добавляет следующую монаду в цепочку, игнорируя значение предыдущей
    def then(self, next_monad: 'StateMonad') -> 'StateMonad':
        return self.bind(lambda _: next_monad)

    # Запускает монаду с заданным состоянии
    def run(self, state: State) -> Tuple[Any, State]:
        return self.func(state)

    # Создаёт монаду, которая ничего не меняет и возвращает value
    @staticmethod
    def pure(value: Any) -> 'StateMonad':
        return StateMonad(lambda state: (value, state))

class RobotStateMonad:
    def __init__(self, monad: StateMonad = StateMonad.pure(None)):
        self.monad = monad

    def _add_step(self, step):
        return RobotStateMonad(self.monad.then(StateMonad(step)))

    def move(self, distance: int) -> 'RobotStateMonad':
        def step(state: State):
            new_state = pure_robot.move(fake_transfer, distance, state.value)
            return None, State(new_state)
        return self._add_step(step)

    def turn(self, angle: int) -> 'RobotStateMonad':
        def step(state: State):
            new_state = pure_robot.turn(fake_transfer, angle, state.value)
            return None, State(new_state)
        return self._add_step(step)

    def set_state(self, new_internal_state) -> 'RobotStateMonad':
        def step(state: State):
            new_state = pure_robot.set_state(fake_transfer, new_internal_state, state.value)
            return None, State(new_state)
        return self._add_step(step)

    def start(self) -> 'RobotStateMonad':
        def step(state: State):
            new_state = pure_robot.start(fake_transfer, state.value)
            return None, State(new_state)
        return self._add_step(step)

    def stop(self) -> 'RobotStateMonad':
        def step(state: State):
            new_state = pure_robot.stop(fake_transfer, state.value)
            return None, State(new_state)
        return self._add_step(step)

    def run(self, state: State):
        return self.monad.run(state)

robot_state = pure_robot.RobotState(x=0.0, y=0.0, angle=0, state=pure_robot.WATER)
initial_state = State(robot_state)

program = RobotStateMonad().move(10).turn(90).set_state('soap').start().move(50).stop()
result, final_state = program.run(initial_state)

print(final_state.value)  # RobotState(x=10.0, y=50.0, angle=90, state=pure_robot.SOAP)
