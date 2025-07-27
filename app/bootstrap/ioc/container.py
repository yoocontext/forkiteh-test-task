from functools import lru_cache

from dishka import (
    AsyncContainer,
    make_async_container,
)
from dishka.integrations.fastapi import FastapiProvider

from bootstrap.ioc.providers.infra import (
    AlchemyProvider,
    ClientTronProvider,
    GetTronGatewaysProvider,
)


@lru_cache(1)
async def get_container() -> AsyncContainer:
    container: AsyncContainer = make_async_container(
        AlchemyProvider(),
        ClientTronProvider(),
        GetTronGatewaysProvider(),
        FastapiProvider(),
    )

    return container