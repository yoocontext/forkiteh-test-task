from decimal import Decimal
from itertools import cycle
from collections.abc import Iterator

from infra.tron.base import IAsyncTron


class MockAsyncTron(IAsyncTron):
    def __init__(
        self,
        balances: list[Decimal],
        bandwidths: list[int],
        energies: list[int],
    ) -> None:
        self._balances: Iterator[Decimal] = cycle(balances)
        self._bandwidth: Iterator[int] = cycle(bandwidths)
        self._energies: Iterator[int] = cycle(energies)

    async def get_account_balance(self, addr: str) -> Decimal:
        return next(self._balances)

    async def get_bandwidth(self, addr: str) -> int:
        return next(self._bandwidth)

    async def get_energy(self, address: str) -> int:
        return next(self._energies)

    async def get_account(self, addr: str) -> dict:
        ...

    async def get_account_resource(self, addr: str) -> dict:
        ...