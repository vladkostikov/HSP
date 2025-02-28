# Категории наследования-2

## Наследования вариаций
### Наследование с функциональной вариацией (functional variation inheritance)
```python
class Logger:
    def log(self, message):
        print(f"LOG: {message}")

class ErrorLogger(Logger):
    def log(self, message):
        print(f"ERROR: {message}")
        with open("error_log.txt", "a") as file:
            file.write(f"ERROR: {message}\n")
```

### Наследование с вариацией типа (type variation inheritance)
```python
class Logger:
    def log(self, message):
        print(f"LOG: {message}")

    def error(self, message):
        print(f"ERROR: {message}")

class LevelLogger(Logger):
    def log(self, message, level="INFO"):
        print(f"{level}: {message}")

    def error(self, message, level="ERROR"):
        print(f"{level}: {message}")
```

## Наследование с конкретизацией (reification inheritance)
```python
from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def log(self, message):
        pass

    @abstractmethod
    def error(self, message):
        pass

class ConsoleLogger(Logger):
    def log(self, message):
        print(f"LOG: {message}")

    def error(self, message):
        print(f"ERROR: {message}")
```

## Структурное наследование (structure inheritance)
```python
from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def log(self, message):
        pass

class FilteredLogger(Logger):
    @abstractmethod
    def filter(self, message):
        pass

class ConsoleLogger(FilteredLogger):
    def filter(self, message):
        forbidden_expressions = ["secret", "password", "token"]
        message_lower = message.lower()
        for expression in forbidden_expressions:
            if expression in message_lower:
                return False
        return True
            
    def log(self, message):
        if self.filter(message):
            print(f"LOG: {message}")
```
