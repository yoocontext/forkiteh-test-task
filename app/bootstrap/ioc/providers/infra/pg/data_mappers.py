from dishka import (
    Provider,
    Scope,
    provide,
)
from sqlalchemy.ext.asyncio import AsyncSession

from infra.pg.data_mappers.wallet_query import WalletQueryDm


class DataMapperProvider(Provider):
    scope = Scope.REQUEST

    @provide
    def wallet_query(self, session: AsyncSession) -> WalletQueryDm:
        dm = WalletQueryDm(session=session)

        return dm