from fastapi import APIRouter
from dishka.integrations.fastapi import (
    DishkaRoute,
    FromDishka,
    inject,
)
from starlette.status import HTTP_201_CREATED

from application.usecase.tron.wallet.fetch import (
    FetchWalletTronCommand,
    FetchWalletTronResult,
    FetchWalletTronUseCase,
)
from presentation.api.v1.tron.wallet.schemas import FetchWalletTronOutSchema, FetchWalletTronInSchema

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
    schema: FetchWalletTronInSchema,
    use_case: FromDishka[FetchWalletTronUseCase],
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
