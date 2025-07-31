from dataclasses import dataclass

from infra.tron.base import IAsyncTron
from infra.tron.gateways.base import BaseGateway
from infra.tron.handlers import handle_tronpy_errors
from share.custom_types import WalletAddress


@dataclass
class GetEnergyTronGateway(BaseGateway):
    tron: IAsyncTron

    @handle_tronpy_errors
    async def act(self, address: WalletAddress) -> int:
        energy: int = await self.tron.get_energy(address=address)

        return energy