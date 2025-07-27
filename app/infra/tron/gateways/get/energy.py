from dataclasses import dataclass

from tronpy import AsyncTron

from infra.tron.gateways.base import BaseGateway
from infra.tron.handlers import handle_tronpy_errors
from share.custom_types import WalletAddress


@dataclass
class GetEnergyTronGateway(BaseGateway):
    tron: AsyncTron

    @handle_tronpy_errors
    async def act(self, address: WalletAddress) -> int:
        energy: int = await self.tron.get_energy(address=address)

        return energy