from datetime import datetime
from uuid import UUID

from fastapi import APIRouter, Query
from dishka.integrations.fastapi import (
    DishkaRoute,
    FromDishka,
    inject,
)
from starlette.status import HTTP_201_CREATED, HTTP_200_OK

from application.usecase.tron.wallet.fetch import (
    FetchWalletTronCommand,
    FetchWalletTronResult,
    FetchWalletTronUseCase,
)
from application.usecase.tron.wallet.get.usecase import (
    GetWalletTronCommand,
    GetWalletTronResult,
    GetWalletTronUseCase,
)
from presentation.api.v1.tron.wallet.mappers import result_to_out_schema
from presentation.api.v1.tron.wallet.schemas import (
    FetchWalletTronOutSchema,
    FetchWalletTronInSchema,
    GetWalletTronOutSchema,
    WalletTronOutSchema,
)

router = APIRouter(
    prefix="/wallet",
    route_class=DishkaRoute,
)


@router.post(
    path="",
    response_model=FetchWalletTronOutSchema,
    status_code=HTTP_201_CREATED,
    summary="""
Get Tron address details: bandwidth, energy, and TRX balance.
Logs each request with the queried wallet address.
"""
)
@inject
async def fetch(
    use_case: FromDishka[FetchWalletTronUseCase],
    schema: FetchWalletTronInSchema,
) -> FetchWalletTronOutSchema:
    command = FetchWalletTronCommand(address=schema.address)

    result: FetchWalletTronResult = await use_case.act(command=command)

    out_schema = FetchWalletTronOutSchema(
        address=result.address,
        bandwidth=result.bandwidth,
        energy=result.energy,
        balance_trx=result.balance_trx,
    )

    return out_schema


@router.get(
    path="",
    response_model=GetWalletTronOutSchema,
    status_code=HTTP_200_OK,
    summary="""
Retrieve a paginated list of the latest wallet query records from the database,
including details such as Tron address, bandwidth, energy, and TRX balance.
Supports filtering by date and wallet UID.
"""
)
@inject
async def get(
    use_case: FromDishka[GetWalletTronUseCase],
    page_size: int = Query(..., ge=1, le=100),
    wallet_uid_last: UUID | None = Query(default=None),
    created_at_last: datetime | None = Query(default=None),
) -> GetWalletTronOutSchema:
    command = GetWalletTronCommand(
        page_size=page_size,
        wallet_uid_last=wallet_uid_last,
        created_at_last=created_at_last,
    )

    result: GetWalletTronResult = await use_case.act(command=command)

    wallets: list[WalletTronOutSchema] = result_to_out_schema(wallets_results=result.wallets)

    out_schema = GetWalletTronOutSchema(
        wallets=wallets,
        created_at_last=result.created_at_last,
        wallet_uid_last=result.wallet_uid_last,
    )

    return out_schema