from dishka import (
    Provider,
    Scope,
    provide,
)

from infra.tron.base import IAsyncTron
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
    def energy(self, tron: IAsyncTron) -> GetEnergyTronGateway:
        gateway = GetEnergyTronGateway(tron=tron)

        return gateway

    @provide
    def bandwidth(self, tron: IAsyncTron) -> GetBandwidthTronGateway:
        gateway = GetBandwidthTronGateway(tron=tron)

        return gateway

    @provide
    def balance_trx(self, tron: IAsyncTron) -> GetBalanceTrxTronGateway:
        gateway = GetBalanceTrxTronGateway(tron=tron)

        return gateway

    @provide
    def account(self, tron: IAsyncTron) -> GetAccountTronGateway:
        gateway = GetAccountTronGateway(tron=tron)

        return gateway

    @provide
    def account_resource(self, tron: IAsyncTron) -> GetAccountResourceTronGateway:
        gateway = GetAccountResourceTronGateway(tron=tron)

        return gateway
    