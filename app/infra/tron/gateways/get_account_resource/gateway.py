from dataclasses import dataclass

from tronpy import AsyncTron

from infra.tron.gateways.base import BaseGateway
from infra.tron.gateways.get_account_resource.mappers import account_resource_response_retort
from infra.tron.gateways.get_account_resource.schemas import GetAccountResourceResponseSchema
from share.custom_types import WalletAddress


@dataclass
class GetAccountResourceGateway(BaseGateway):
    tron: AsyncTron

    async def act(self, address: WalletAddress) -> GetAccountResourceResponseSchema:
        account_resource: dict = await self.tron.get_account_resource(addr=address)
        account_resource_response: GetAccountResourceResponseSchema = (
            account_resource_response_retort.load(account_resource, GetAccountResourceResponseSchema)
        )

        return account_resource_response


import asyncio


async def main():
    tron = AsyncTron()

    g = GetAccountResourceGateway(tron=tron)
    addr: WalletAddress = "TXLAQ63Xg1NAzckPwKHvzw7CSEmLMEqcdj"

    r = await g.act(address=addr)

    print(r)


asyncio.run(main())