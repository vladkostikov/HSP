# Категории наследования-3

## Наследование реализации (implementation inheritance)
```python
class Device:
    def __init__(self, name):
        self.name = name

    def connect(self):
        print(f"{self.name} connected")

    def disconnect(self):
        print(f"{self.name} disconnected")

    def send_data(self, data):
        print(f"Sending data to {self.name}: {data}")

class Printer(Device):
    def __init__(self, name, paper_level):
        super().__init__(name)
        self.paper_level = paper_level

    def print_document(self, document):
        if self.paper_level > 0:
            print(f"Printing document: {document}")
            self.paper_level -= 1
        else:
            print("Cannot print: out of paper")
```

## Льготное наследование (facility inheritance)
```python
class Config:
    def __init__(self):
        self.settings = {
            "language": "en",
            "timeout": 30,
            "debug": False
        }

    def get(self, key):
        return self.settings.get(key, None)

    def set(self, key, value):
        self.settings[key] = value

class AdminConfig(Config):
    def __init__(self):
        super().__init__()
        self.settings["timeout"] = 10
        self.settings["debug"] = True

class UserConfig(Config):
    def __init__(self):
        super().__init__()
        self.settings["language"] = "ru"
```
