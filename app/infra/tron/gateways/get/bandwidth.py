from dataclasses import dataclass

from infra.tron.base import IAsyncTron
from infra.tron.gateways.base import BaseGateway
from infra.tron.handlers import handle_tronpy_errors
from share.custom_types import WalletAddress


@dataclass
class GetBandwidthTronGateway(BaseGateway):
    tron: IAsyncTron

    @handle_tronpy_errors
    async def act(self, address: WalletAddress) -> int:
        bandwidth: int = await self.tron.get_bandwidth(addr=address)

        return bandwidth