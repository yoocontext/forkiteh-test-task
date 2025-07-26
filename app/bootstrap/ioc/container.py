from functools import lru_cache

from dishka import (
    AsyncContainer,
    make_async_container,
)

from bootstrap.ioc.providers.infra import (
    AlchemyProvider,
)


@lru_cache(1)
async def get_container() -> AsyncContainer:
    container: AsyncContainer = make_async_container(
        AlchemyProvider(),
    )

    return container