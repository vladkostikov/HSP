class BloomFilter:
    def __init__(self, filter_len: int):
        self.__filter_len = filter_len
        self.__bitmap = 0

    # Постусловие: указанное значение добавлено в фильтр
    def put(self, value: str) -> None:
        hash1 = self.__hash1(value)
        hash2 = self.__hash2(value)

        bitmask1 = 1 << hash1
        bitmask2 = 1 << hash2

        self.__bitmap = self.__bitmap | bitmask1 | bitmask2

        return None

    # Находится ли указанное значение в фильтре, возможны ложноположительные срабатывания
    def is_value(self, value: str) -> bool:
        hash1 = self.__hash1(value)
        hash2 = self.__hash2(value)

        bitmask1 = 1 << hash1
        bitmask2 = 1 << hash2

        return (self.__bitmap & bitmask1 == bitmask1) and (self.__bitmap & bitmask2 == bitmask2)

    def __hash1(self, value: str) -> int:
        rand_number = 17
        result = 0
        for i, char in enumerate(value):
            result *= i
            result *= ord(char)
            result += rand_number
            result %= self.__filter_len
        return result

    def __hash2(self, value: str) -> int:
        rand_number = 223
        result = 0
        for i, char in enumerate(value):
            result += i
            result += rand_number
            result *= ord(char)
            result %= self.__filter_len
        return result
