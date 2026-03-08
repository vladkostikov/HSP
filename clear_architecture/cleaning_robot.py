# Задача: реализовать программу для дистанционного управления роботом.
# Робот должен поддерживать следующие команды(DSL): Move, Turn, Set, Start, Stop.
class CleaningRobot:
    CLEANING_STATES = ['water', 'soap', 'brush']
    def __init__(self):
        self._position_x = 0
        self._position_y = 0
        self._angle = 0
        self._cleaning_state = 'water'
        self._status = "stop"
        self._commands = {
            "move": self._handle_move,
            "turn": self._handle_turn,
            "set": self._handle_set,
            "start": self._handle_start,
            "stop": self._handle_stop,
        }

    # Основной метод для обработки команд
    def call(self, command: str) -> str:
        parts = command.strip().lower().split()
        if not parts:
            return "Error"

        cmd = parts[0]
        handler = self._commands.get(cmd)
        if handler:
            return handler(parts)
        return "Error"

    # Обработка команд
    def _handle_move(self, parts) -> str:
        if len(parts) != 2:
            return "Error"

        try:
            distance = int(parts[1])
            self._move(distance)
            return self._format_position()
        except:
            return "Error"

    def _handle_turn(self, parts) -> str:
        if len(parts) != 2:
            return "Error"

        try:
            angle = int(parts[1])
            if angle % 90 != 0:
                return "AngleError"
            self._turn(angle)
            return self._format_angle()
        except:
            return "Error"

    def _handle_set(self, parts) -> str:
        if len(parts) != 2:
            return "Error"

        state = parts[1]
        if state not in self.CLEANING_STATES:
            return "Error"

        self.set_cleaning_state(state)
        return self._format_cleaning_state()

    def _handle_start(self, _parts) -> str:
        self._start()
        return f"START WITH {self._cleaning_state}"

    def _handle_stop(self, _parts):
        self._stop()
        return "STOP"

    # Форматирование вывода
    def _format_position(self) -> str:
        return f"POS {self._position_x},{self._position_y}"

    def _format_angle(self) -> str:
        return f"ANGLE {self._angle}"

    def _format_cleaning_state(self) -> str:
        return f"STATE {self._cleaning_state}"

    # Действия робота
    def _move(self, distance: int):
        if self._angle == 0:
            self._position_y += distance
        if self._angle == 90:
            self._position_x += distance
        if self._angle == 180:
            self._position_y -= distance
        if self._angle == 270:
            self._position_x -= distance

    def _turn(self, angle: int):
        self._angle = (self._angle + angle) % 360

    def set_cleaning_state(self, cleaning_state: str):
        self._cleaning_state = cleaning_state

    def _start(self):
        self._status = "start"

    def _stop(self):
        self._status = "stop"
