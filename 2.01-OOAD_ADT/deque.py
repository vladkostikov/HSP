class ParentQueue:
    REMOVE_FRONT_OK = 1  # успешно удалён первый элемент очереди
    REMOVE_FRONT_ERR = 2  # очередь пуста

    GET_HEAD_OK = 1  # успешно получен первый элемент очереди
    GET_HEAD_ERR = 2  # очередь пуста

    def __init__(self):
        pass

    # Команды

    # Постусловие: в конец очереди добавлен новый элемент
    def add_tail(self, value) -> None:
        pass

    enqueue = add_tail
    enq = add_tail

    # Предусловие: очередь не пуста
    # Постусловие: из очереди удалён первый элемент
    def remove_front(self, value) -> None:
        pass

    dequeue = remove_front
    deq = remove_front

    # Запросы

    def size(self) -> int:
        pass

    # Предусловие: очередь не пуста
    def get_head(self):
        pass

    # Статусы

    def get_remove_front_status(self) -> int:
        pass

    get_dequeue_status = get_remove_front_status
    get_deq_status = get_remove_front_status

    def get_head_status(self) -> int:
        pass


class Queue(ParentQueue):
    def __init__(self):
        super().__init__()

    # Запросы

    def get(self):
        return super().get_head()

    # Статусы

    def get_get_status(self) -> int:
        return super().get_head_status()


class Deque(ParentQueue):
    REMOVE_TAIL_OK = 1  # успешно удалён последний элемент очереди
    REMOVE_TAIL_ERR = 2  # очередь пуста

    GET_TAIL_OK = 1  # успешно получен последний элемент очереди
    GET_TAIL_ERR = 2  # очередь пуста

    def __init__(self):
        super().__init__()

    # Постусловие: в начало очереди добавлен новый элемент
    def add_front(self, value) -> None:
        pass

    # Предусловие: очередь не пуста
    # Постусловие: из очереди удалён последний элемент
    def remove_tail(self, value) -> None:
        pass

    # Запросы

    # Предусловие: очередь не пуста
    def get_tail(self):
        pass

    # Статусы

    def get_remove_tail_status(self) -> int:
        pass

    def get_get_tail_status(self) -> int:
        pass
