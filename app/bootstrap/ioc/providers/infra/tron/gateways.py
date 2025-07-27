from dishka import (
    Provider,
    Scope,
    provide,
)
from tronpy import AsyncTron

from infra.tron.gateways.get import (
    GetEnergyTronGateway,
    GetBandwidthTronGateway,
    GetBalanceTrxTronGateway,
    GetAccountTronGateway,
    GetAccountResourceTronGateway,
)


class GetTronGatewaysProvider(Provider):
    scope = Scope.REQUEST

    @provide
    def energy(self, tron: AsyncTron) -> GetEnergyTronGateway:
        gateway = GetEnergyTronGateway(tron=tron)

        return gateway

    @provide
    def bandwidth(self, tron: AsyncTron) -> GetBandwidthTronGateway:
        gateway = GetBandwidthTronGateway(tron=tron)

        return gateway

    @provide
    def balance_trx(self, tron: AsyncTron) -> GetBalanceTrxTronGateway:
        gateway = GetBalanceTrxTronGateway(tron=tron)

        return gateway

    @provide
    def account(self, tron: AsyncTron) -> GetAccountTronGateway:
        gateway = GetAccountTronGateway(tron=tron)

        return gateway

    @provide
    def account_resource(self, tron: AsyncTron) -> GetAccountResourceTronGateway:
        gateway = GetAccountResourceTronGateway(tron=tron)

        return gateway
    