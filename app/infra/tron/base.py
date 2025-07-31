from decimal import Decimal
from typing import Protocol


class IAsyncTron(Protocol):
    async def get_account_balance(self, addr: str) -> Decimal:
        ...

    async def get_bandwidth(self, addr: str) -> int:
        ...

    async def get_energy(self, address: str) -> int:
        ...

    async def get_account(self, addr: str) -> dict:
        ...

    async def get_account_resource(self, addr: str) -> dict:
        ...

