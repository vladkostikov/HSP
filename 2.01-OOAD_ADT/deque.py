class ParentQueue:
    REMOVE_FRONT_OK = 1  # успешно удалён первый элемент очереди
    REMOVE_FRONT_ERR = 2  # очередь пуста

    GET_HEAD_OK = 1  # успешно получен первый элемент очереди
    GET_HEAD_ERR = 2  # очередь пуста

    def __init__(self):
        self.head_storage = []  # элементы располагаем в обратном порядке, последний элемент первый в очереди
        self.tail_storage = []

        self.remove_front_status = self.REMOVE_FRONT_ERR
        self.get_head_status = self.GET_HEAD_ERR

    # Команды

    # Постусловие: в конец очереди добавлен новый элемент
    def add_tail(self, value) -> None:
        self.tail_storage.append(value)
        return None

    enqueue = add_tail
    enq = add_tail

    # Предусловие: очередь не пуста
    # Постусловие: из очереди удалён первый элемент
    def remove_front(self) -> None:
        if self.is_empty():
            self.remove_front_status = self.REMOVE_FRONT_ERR
            return None

        if len(self.head_storage) == 0:
            self.__move_half_tail_to_head()

        self.head_storage.pop()
        self.remove_front_status = self.REMOVE_FRONT_OK
        return None

    dequeue = remove_front
    deq = remove_front

    # Запросы

    def size(self) -> int:
        return len(self.head_storage) + len(self.tail_storage)

    def is_empty(self) -> bool:
        return len(self.head_storage) == 0 and len(self.tail_storage) == 0

    # Предусловие: очередь не пуста
    def get_head(self):
        if self.is_empty():
            self.get_head_status = self.GET_HEAD_ERR
            return None

        if len(self.head_storage) == 0:
            self.__move_half_tail_to_head()

        self.get_head_status = self.GET_HEAD_OK
        return self.head_storage[-1]

    first = get_head

    # Статусы

    def get_remove_front_status(self) -> int:
        return self.remove_front_status

    get_dequeue_status = get_remove_front_status
    get_deq_status = get_remove_front_status

    def get_get_head_status(self) -> int:
        return self.get_head_status

    def __move_half_tail_to_head(self):
        self.head_storage = self.tail_storage[0:(len(self.tail_storage) // 2 + 1)]
        self.head_storage.reverse()
        self.tail_storage = self.tail_storage[(len(self.tail_storage) // 2 + 1):]
        return None


class Queue(ParentQueue):
    def __init__(self):
        super().__init__()

    # Запросы

    def get(self):
        return super().get_head()

    # Статусы

    def get_get_status(self) -> int:
        return super().get_get_head_status()


class Deque(ParentQueue):
    REMOVE_TAIL_OK = 1  # успешно удалён последний элемент очереди
    REMOVE_TAIL_ERR = 2  # очередь пуста

    GET_TAIL_OK = 1  # успешно получен последний элемент очереди
    GET_TAIL_ERR = 2  # очередь пуста

    def __init__(self):
        super().__init__()

        self.remove_tail_status = self.REMOVE_TAIL_ERR
        self.get_tail_status = self.GET_HEAD_ERR

    # Постусловие: в начало очереди добавлен новый элемент
    def add_front(self, value) -> None:
        self.head_storage.append(value)
        return None

    # Предусловие: очередь не пуста
    # Постусловие: из очереди удалён последний элемент
    def remove_tail(self) -> None:
        if self.is_empty():
            self.remove_tail_status = self.REMOVE_TAIL_ERR
            return None

        if len(self.tail_storage) == 0:
            self.__move_half_head_to_tail()

        self.tail_storage.pop()
        self.remove_tail_status = self.REMOVE_TAIL_OK
        return None

    # Запросы

    # Предусловие: очередь не пуста
    def get_tail(self):
        if self.is_empty():
            self.get_tail_status = self.GET_TAIL_ERR
            return None

        if len(self.tail_storage) == 0:
            self.__move_half_head_to_tail()

        self.get_tail_status = self.GET_HEAD_OK
        return self.tail_storage[-1]

    last = get_tail

    # Статусы

    def get_remove_tail_status(self) -> int:
        return self.remove_tail_status

    def get_get_tail_status(self) -> int:
        return self.get_tail_status

    def __move_half_head_to_tail(self) -> None:
        self.tail_storage = self.head_storage[0:(len(self.head_storage) // 2 + 1)]
        self.tail_storage.reverse()
        self.head_storage = self.head_storage[(len(self.head_storage) // 2 + 1):]
        return None
