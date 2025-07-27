from decimal import Decimal

from tronpy import AsyncTron

from infra.tron.gateways.base import BaseGateway
from infra.tron.handlers import handle_tronpy_errors
from share.custom_types import WalletAddress


class GetBalanceTrxTronGateway(BaseGateway):
    tron: AsyncTron

    @handle_tronpy_errors
    async def act(self, address: WalletAddress) -> Decimal:
        balance_txr: Decimal = await self.tron.get_account_balance(addr=address)

        return balance_txr