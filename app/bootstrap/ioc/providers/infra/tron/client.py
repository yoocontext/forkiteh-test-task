from dishka import (
    Provider,
    Scope,
    provide,
)
from tronpy import AsyncTron
from tronpy.providers import AsyncHTTPProvider

from bootstrap.settings.base import CommonSettings


class ClientTronProvider(Provider):
    @provide(scope=Scope.APP)
    def torn(self, settings: CommonSettings) -> AsyncTron:
        provider = AsyncHTTPProvider(
            endpoint_uri=settings.tron.endpoint_url,
            api_key=settings.tron.api_key,
        )
        tron = AsyncTron(
            provider=provider,
            network=settings.tron.network,
        )

        return tron
