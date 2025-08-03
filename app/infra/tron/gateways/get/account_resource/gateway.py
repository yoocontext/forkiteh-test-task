from dataclasses import dataclass

from infra.tron.base import IAsyncTron
from infra.tron.gateways.base import BaseGateway
from infra.tron.gateways.get.account_resource.mappers import account_resource_response_retort
from infra.tron.gateways.get.account_resource.schemas import GetAccountResourceResponseSchema
from share.custom_types import WalletAddress


@dataclass
class GetAccountResourceTronGateway(BaseGateway):
    tron: IAsyncTron

    async def act(self, address: WalletAddress) -> GetAccountResourceResponseSchema:
        account_resource: dict = await self.tron.get_account_resource(addr=address)
        account_resource_response: GetAccountResourceResponseSchema = (
            account_resource_response_retort.load(account_resource, GetAccountResourceResponseSchema)
        )

        return account_resource_response
