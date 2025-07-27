from functools import lru_cache

from dishka import (
    AsyncContainer,
    make_async_container,
)
from dishka.integrations.fastapi import FastapiProvider

from bootstrap.ioc.providers.application import UseCaseProvider
from bootstrap.ioc.providers.infra import (
    AlchemyProvider,
    ClientTronProvider,
    GetTronGatewaysProvider,
)
from bootstrap.ioc.providers.bootstrap import SettingsProvider

@lru_cache(1)
def get_container() -> AsyncContainer:
    container: AsyncContainer = make_async_container(
        UseCaseProvider(),
        AlchemyProvider(),
        ClientTronProvider(),
        GetTronGatewaysProvider(),
        SettingsProvider(),
        FastapiProvider(),
    )

    return container
