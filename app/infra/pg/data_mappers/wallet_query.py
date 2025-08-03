from dataclasses import dataclass
from uuid import UUID

from sqlalchemy import select

from infra.pg.data_mappers.base import BaseDm
from infra.pg.models import WalletQueryOrm
from share.custom_types import WalletAddress


@dataclass
class WalletQueryDm(BaseDm):
    async def get(self, uid: UUID) -> WalletQueryOrm | None:
        wallet_orm: WalletQueryOrm | None = await self.session.get(WalletQueryDm, uid)

        return wallet_orm

    async def get_by_address(self, address: WalletAddress) -> list[WalletQueryOrm]:
        result = await self.session.execute(
            select(WalletQueryOrm)
            .where(WalletQueryOrm.address == address)
        )
        wallets_orm: list[WalletQueryOrm] = list(result.scalars().all())

        return wallets_orm
