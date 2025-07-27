from dishka import (
    Provider,
    Scope,
    provide,
)
from tronpy import AsyncTron

from bootstrap.settings.base import CommonSettings


class ClientTronProvider(Provider):
    @provide(scope=Scope.APP)
    def torn(self, settings: CommonSettings) -> AsyncTron:
        tron = AsyncTron(network=settings.tron.network)

        return tron
