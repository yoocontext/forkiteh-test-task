from decimal import Decimal

from dishka import Provider, provide, Scope

from infra.tron.base import IAsyncTron
from tests.mocs.tron import MockAsyncTron


class MockClientTronProvider(Provider):
    @provide(scope=Scope.APP)
    def torn(self) -> IAsyncTron:
        tron = MockAsyncTron(
            balances=[Decimal(4373478)],
            bandwidths=[0, 12, 334],
            energies=[11, 222, 0]
        )

        return tron
