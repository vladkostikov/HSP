class Queue:
    DEQUEUE_OK = 1  # из начала очереди успешно удалено значение
    DEQUEUE_ERR = 2  # очередь пуста

    HEAD_OK = 1  # успешно получен первый элемент очереди
    HEAD_ERR = 2  # очередь пуста

    def __init__(self):
        self.data = []
        self.dequeue_status = self.DEQUEUE_ERR
        self.head_status = self.HEAD_ERR

    # Команды

    # Постусловие: в конец очереди добавлено указанное значение
    def enqueue(self, value) -> None:
        self.data.append(value)
        return None

    enq = enqueue

    # Предусловие: очередь не пуста
    # Постусловие: из начала очереди удалено значение
    def dequeue(self) -> None:
        if len(self.data) == 0:
            self.dequeue_status = self.DEQUEUE_ERR
            return None

        self.data.pop(0)
        self.dequeue_status = self.DEQUEUE_OK
        return None

    deq = dequeue

    # Постусловие: очередь очищена
    def clear(self) -> None:
        self.data = []
        self.dequeue_status = self.DEQUEUE_ERR
        self.head_status = self.HEAD_ERR
        return None

    # Запросы

    # Предусловие: очередь не пуста
    def head(self):
        if len(self.data) == 0:
            self.head_status = self.HEAD_ERR
            return None
        self.head_status = self.HEAD_OK
        return self.data[0]

    def size(self) -> int:
        return len(self.data)

    # Статусы

    def get_dequeue_status(self) -> int:
        return self.dequeue_status

    def get_head_status(self) -> int:
        return self.head_status
