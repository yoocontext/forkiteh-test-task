import os
import sys
from functools import lru_cache

from dishka import AsyncContainer, make_async_container

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'app')))

from app.bootstrap.ioc.container import DEV_PROVIDERS
from app.bootstrap.ioc.providers.infra import AlchemyProvider
from tests.ioc.providers.infra import MockClientTronProvider


@lru_cache(1)
def get_test_container(connection_string: str) -> AsyncContainer:
    container: AsyncContainer = make_async_container(
        *DEV_PROVIDERS,
        MockClientTronProvider(),
        AlchemyProvider(connection_string=connection_string),
    )

    return container