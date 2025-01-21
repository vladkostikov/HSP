# Внутренний класс, задаёт интерфейс(контракт), который отдельно реализуется для каждого провайдера.
# Открыт для расширения, требует изменения при добавлении новых функций.
class VirtualServerProvider:
    def create_server(self, params: dict) -> None:
        raise NotImplementedError


# Открытые классы для управления серверами у разных провайдеров.
# Реализация может меняться, но обязательно соблюдается интерфейс VirtualServerProvider.

class HetznerVirtualServer(VirtualServerProvider):
    def create_server(self, params: dict) -> None:
        pass


class OVHVirtualServer(VirtualServerProvider):
    def create_server(self, params: dict) -> None:
        pass


class SelectelVirtualServer(VirtualServerProvider):
    def create_server(self, params: dict) -> None:
        pass


# Класс для управления провайдерами.
# Является закрытым, не меняется при изменении функционала и добавлении новых провайдеров.
class ProviderFactory:
    _providers = {}  # Database

    @classmethod
    def register_provider(cls, name: str, provider_cls) -> None:
        pass

    @classmethod
    def get_provider(cls, name: str) -> VirtualServerProvider:
        pass


# Класс, с которым взаимодействует пользователь.
# Открыт для расширения, требует изменения при добавлении новых функций.
class VirtualServerManager:
    def __init__(self, provider_name: str) -> None:
        self.provider = ProviderFactory.get_provider(provider_name)

    def create_server(self, params: dict) -> None:
        self.provider.create_server(params)
