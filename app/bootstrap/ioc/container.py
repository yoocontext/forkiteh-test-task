from functools import lru_cache

from dishka import (
    AsyncContainer,
    Provider,
    make_async_container,
)
from dishka.integrations.fastapi import FastapiProvider

from bootstrap.ioc.providers.application import (
    WalletTronServiceProvider,
    UseCaseProvider,
)
from bootstrap.ioc.providers.infra import (
    AlchemyProvider,
    ClientTronProvider,
    MockClientTronProvider,
    GetTronGatewaysProvider,
)
from bootstrap.ioc.providers.bootstrap import SettingsProvider


DEV_PROVIDERS: list[Provider] = [
    WalletTronServiceProvider(),
    UseCaseProvider(),
    AlchemyProvider(),
    ClientTronProvider(),
    GetTronGatewaysProvider(),
    SettingsProvider(),
    FastapiProvider(),
]


@lru_cache(1)
def get_container() -> AsyncContainer:
    container: AsyncContainer = make_async_container(*DEV_PROVIDERS)

    return container


@lru_cache(1)
def get_test_container() -> AsyncContainer:
    container: AsyncContainer = make_async_container(
        MockClientTronProvider(),
        *DEV_PROVIDERS,
    )

    return container