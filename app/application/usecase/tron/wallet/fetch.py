from dataclasses import dataclass
from decimal import Decimal

from sqlalchemy.ext.asyncio import AsyncSession
from tronpy import AsyncTron

from application.usecase.base import (
    BaseResult,
    BaseCommand,
    BaseUseCase,
)
from infra.pg.models.tron.wallet_query import WalletQueryOrm
from share.custom_types import WalletAddress


@dataclass
class FetchWalletTronCommand(BaseCommand):
    address: WalletAddress


@dataclass
class FetchWalletTronResult(BaseResult):
    address: str
    bandwidth: int
    energy: int
    balance_trx: Decimal


@dataclass
class FetchWalletTronUseCase(BaseUseCase):
    session: AsyncSession
    tron: AsyncTron

    async def act(
        self,
        command: FetchWalletTronCommand,
    ) -> FetchWalletTronResult:

        bandwidth: int = await self.tron.get_bandwidth(addr=command.address)
        energy: int = await self.tron.get_energy(address=command.address)
        balance_trx: Decimal = await self.tron.get_account_balance(addr=command.address)

        wallet_query_orm = WalletQueryOrm(
            address=command.address,
            bandwidth=bandwidth,
            energy=energy,
            balance_trx=balance_trx,
        )

        self.session.add(wallet_query_orm)
        await self.session.commit()

        fetch_wallet_tron_result = FetchWalletTronResult(
            address=command.address,
            bandwidth=bandwidth,
            energy=energy,
            balance_trx=balance_trx,
        )

        return fetch_wallet_tron_result