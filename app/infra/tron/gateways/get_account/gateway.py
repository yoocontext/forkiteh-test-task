from dataclasses import dataclass

from tronpy import AsyncTron

from infra.tron.gateways.base import BaseGateway
from infra.tron.gateways.get_account.mappers import account_response_retort
from infra.tron.gateways.get_account.schemas import AccountResponseSchema
from share.custom_types import WalletAddress


@dataclass
class GetAccountTronGateway(BaseGateway):
    tron: AsyncTron

    async def act(self, address: WalletAddress) -> AccountResponseSchema:
        account: dict = await self.tron.get_account(address)
        account_schema: AccountResponseSchema = (
            account_response_retort.load(account, AccountResponseSchema)
        )

        return account_schema
