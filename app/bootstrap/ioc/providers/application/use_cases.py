from dishka import (
    Provider,
    Scope,
    provide,
)
from sqlalchemy.ext.asyncio import AsyncSession
from tronpy import AsyncTron

from application.usecase.tron import FetchWalletTronUseCase
from infra.tron.gateways.get import (
    GetBalanceTrxTronGateway,
    GetBandwidthTronGateway,
    GetEnergyTronGateway,
)


class UseCaseProvider(Provider):
    scope = Scope.APP

    @provide
    def tron_wallet_fetch(
        self,
        get_balance_trx_gateway: GetBalanceTrxTronGateway,
        get_bandwidth_gateway: GetBandwidthTronGateway,
        get_energy_tron_gateway: GetEnergyTronGateway,
        session: AsyncSession,
    tron: AsyncTron
    ) -> FetchWalletTronUseCase:
        use_case = FetchWalletTronUseCase(
            get_balance_trx_gateway=get_balance_trx_gateway,
            get_bandwidth_gateway=get_bandwidth_gateway,
            get_energy_tron_gateway=get_energy_tron_gateway,
            session=session,
            tron=tron,
        )

        return use_case