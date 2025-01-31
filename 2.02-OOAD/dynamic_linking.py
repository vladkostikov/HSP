# Базовый класс для всех виртуальных серверов.
# Для добавления новой реализации достаточно наследоваться от VirtualMachine и добавить методы согласно контракту.
class VirtualMachine:
    def start(self):
        raise NotImplementedError

    def stop(self):
        raise NotImplementedError


# Реализация для серверов на Linux.
class LinuxVM(VirtualMachine):
    def start(self):
        pass

    def stop(self):
        pass


# Реализация для серверов на Windows.
class WindowsVM(VirtualMachine):
    def start(self):
        pass

    def stop(self):
        pass


# Класс для управления виртуальными серверами.
# Получает в качестве параметра одного из предков VirtualMachine и вызывает
# его методы с помощью динамического связывания.
class VirtualMachineManager:
    def __init__(self, machine: VirtualMachine):
        self.__machine = machine

    def reboot(self):
        self.__machine.stop()
        self.__machine.start()
