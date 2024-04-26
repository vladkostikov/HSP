class ksort:
    def __init__(self):
        a, m, n = 8, 10, 10
        self.items = [None] * a * m * n

    def index(self, string: str) -> int:
        if len(string) != 3:
            return -1

        if (ord(string[0]) not in range(97, 105)
                or ord(string[1]) not in range(48, 58)
                or ord(string[2]) not in range(48, 58)):
            return -1

        hundreds = ord(string[0]) - 97
        tens = ord(string[1]) - 48
        number = ord(string[2]) - 48

        return (hundreds * 100) + (tens * 10) + number

    def add(self, string: str) -> bool:
        index = self.index(string)
        if index == -1:
            return False

        self.items[index] = string
        return True
