from dataclasses import dataclass

from tronpy import AsyncTron

from infra.tron.gateways.base import BaseGateway
from infra.tron.gateways.get.account.mappers import account_response_retort
from infra.tron.gateways.get.account.schemas import GetAccountResponseSchema
from share.custom_types import WalletAddress


@dataclass
class GetAccountTronGateway(BaseGateway):
    tron: AsyncTron

    async def act(self, address: WalletAddress) -> GetAccountResponseSchema:
        account: dict = await self.tron.get_account(address)
        account_schema: GetAccountResponseSchema = (
            account_response_retort.load(account, GetAccountResponseSchema)
        )

        return account_schema
