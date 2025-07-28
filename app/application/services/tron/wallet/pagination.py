from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from sqlalchemy import and_, select, or_
from sqlalchemy.ext.asyncio import AsyncSession

from application.services.base import BaseService
from infra.pg.models import WalletQueryOrm


@dataclass
class WalletPaginationTronService(BaseService):
    session: AsyncSession

    async def act(
        self,
        page_size: int,
        wallet_uid_last: UUID,
        created_at_last: datetime,
    ) -> list[WalletQueryOrm]:
        stmt = select(WalletQueryOrm)

        if created_at_last is not None and wallet_uid_last is not None:
            stmt = stmt.where(
                or_(
                    WalletQueryOrm.created_at < created_at_last,
                    and_(
                        WalletQueryOrm.created_at == created_at_last,
                        WalletQueryOrm.uid < wallet_uid_last,
                    )
                )
            )

        stmt = (
            stmt
            .order_by(
                WalletQueryOrm.created_at.desc(),
                WalletQueryOrm.uid.desc(),
            )
            .limit(page_size)
        )

        result = await self.session.execute(stmt)

        wallets_orm: list[WalletQueryOrm] = list(result.scalars().all())

        return wallets_orm