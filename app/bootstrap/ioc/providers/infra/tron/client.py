from dishka import (
    Provider,
    Scope,
    provide,
)
from tronpy import AsyncTron
from tronpy.providers import AsyncHTTPProvider

from bootstrap.settings.base import CommonSettings
from infra.tron.base import IAsyncTron


class ClientTronProvider(Provider):
    @provide(scope=Scope.APP)
    def torn(self, settings: CommonSettings) -> IAsyncTron:
        provider = AsyncHTTPProvider(
            endpoint_uri=settings.tron.endpoint_url,
            api_key=settings.tron.api_key,
        )
        tron = AsyncTron(
            provider=provider,
            network=settings.tron.network,
        )

        return tron
