from dishka import (
    Provider,
    Scope,
    provide,
)
from sqlalchemy.ext.asyncio import AsyncSession
from tronpy import AsyncTron

from application.services.tron.wallet.pagination import WalletPaginationTronService
from application.usecase.tron import FetchWalletTronUseCase
from application.usecase.tron.wallet.get.usecase import GetWalletTronUseCase
from infra.tron.gateways.get import (
    GetBalanceTrxTronGateway,
    GetBandwidthTronGateway,
    GetEnergyTronGateway,
)


class UseCaseProvider(Provider):
    scope = Scope.REQUEST

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

    @provide
    def tron_wallet_get(
        self,
        wallet_pagination_service: WalletPaginationTronService,
    ) -> GetWalletTronUseCase:
        use_case = GetWalletTronUseCase(
            wallet_pagination_service=wallet_pagination_service,
        )

        return use_case
