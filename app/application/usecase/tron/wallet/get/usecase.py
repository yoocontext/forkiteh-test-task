from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from application.services.tron.wallet.pagination import WalletPaginationTronService
from application.usecase.base import (
    BaseCommand,
    BaseResult,
    BaseUseCase,
)
from application.usecase.tron.wallet.get.mappers import orm_to_use_case_schemas_mapper
from application.usecase.tron.wallet.get.schemas import GetWalletTronSchema
from infra.pg.models import WalletQueryOrm


@dataclass
class GetWalletTronCommand(BaseCommand):
    page_size: int
    wallet_uid_last: UUID | None
    created_at_last: datetime | None


@dataclass
class GetWalletTronResult(BaseResult):
    wallet_uid_last: UUID | None
    created_at_last: datetime | None
    wallets: list[GetWalletTronSchema]


@dataclass
class GetWalletTronUseCase(BaseUseCase):
    wallet_pagination_service: WalletPaginationTronService

    async def act(self, command: GetWalletTronCommand) -> GetWalletTronResult:
        wallets_orm: list[WalletQueryOrm] = await self.wallet_pagination_service.act(
            page_size=command.page_size,
            wallet_uid_last=command.wallet_uid_last,
            created_at_last=command.created_at_last,
        )

        wallet_uid_last: UUID | None = None
        created_at_last: datetime | None = None

        if wallets_orm:
            wallet_uid_last = wallets_orm[-1].uid
            created_at_last = wallets_orm[-1].created_at

        schemas: list[GetWalletTronSchema] = orm_to_use_case_schemas_mapper(
            wallets_orm=wallets_orm,
        )

        result = GetWalletTronResult(
            wallet_uid_last=wallet_uid_last,
            created_at_last=created_at_last,
            wallets=schemas,
        )

        return result