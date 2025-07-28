from dishka import (
    Provider,
    Scope,
    provide,
)
from sqlalchemy.ext.asyncio import AsyncSession

from application.services.tron.wallet.pagination import WalletPaginationTronService


class WalletTronServiceProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def pagination(self, session: AsyncSession) -> WalletPaginationTronService:
        service = WalletPaginationTronService(session=session)

        return service
