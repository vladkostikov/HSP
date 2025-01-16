# Базовый класс.
class Downloader:
    def __init__(self, url):
        self.url = url

    def download(self):
        return f"Загрузка файла с {self.url}."


# Расширение родительского класса.
class AdvancedDownloader(Downloader):
    # Добавляем повторные попытки и таймаут.
    def __init__(self, url, retries=3, timeout=10):
        super().__init__(url)
        self.retries = retries
        self.timeout = timeout

    def download_with_retries(self):
        attempts = 0
        while attempts < self.retries:
            attempts += 1
            self.download()
        return f"Загрузка завершена после {attempts} попыток."

    def set_timeout(self, timeout):
        self.timeout = timeout
        return f"Таймаут изменён на {self.timeout} секунд."


# Специализация родительского класса для работы с видео.
class VideoDownloader(AdvancedDownloader):
    # Добавляем свойство разрешение, которое специфично именно для видео.
    def __init__(self, url, retries=3, timeout=10, resolution="1080p"):
        super().__init__(url, retries, timeout)
        self.resolution = resolution

    # Специализированный метод для загрузки видео.
    def download(self):
        return f"Загрузка видео с {self.url} в разрешении {self.resolution}."

    # Специализированный метод для изменения разрешения.
    def set_resolution(self, resolution):
        self.resolution = resolution
        return f"Разрешение изменено на {self.resolution}."
