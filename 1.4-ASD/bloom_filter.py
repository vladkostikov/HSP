class BloomFilter:
    def __init__(self, f_len):
        self.filter_len = f_len
        self.filter = 0

    def hash1(self, string: str) -> int:
        result = 0
        for char in string:
            result *= 17
            result += ord(char)
        return result % self.filter_len

    def hash2(self, string: str) -> int:
        result = 0
        for char in string:
            result *= 223
            result += ord(char)
        return result % self.filter_len

    # Добавление строки в фильтр.
    def add(self, string: str) -> str:
        bit_index1 = self.hash1(string)
        bit_index2 = self.hash2(string)

        bit1 = 1 << bit_index1
        bit2 = 1 << bit_index2

        self.filter = self.filter | bit1 | bit2

        return string

    # Проверка наличия строки в фильтре.
    def is_value(self, string: str) -> bool:
        bit_index1 = self.hash1(string)
        bit_index2 = self.hash2(string)

        bit1 = 1 << bit_index1
        bit2 = 1 << bit_index2

        return (self.filter & bit1 == bit1) and (self.filter & bit2 == bit2)
