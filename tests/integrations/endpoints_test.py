import pytest
from dishka import AsyncContainer
from httpx import Response, AsyncClient

from infra.pg.data_mappers.wallet_query import WalletQueryDm
from infra.pg.models import WalletQueryOrm
from share.custom_types import WalletAddress


@pytest.mark.integration
async def test_wallet_fetch(
    client: AsyncClient,
    ioc_container: AsyncContainer,
):
    address: WalletAddress = "TXLAQ63Xg1NAzckPwKHvzw7CSEmLMEqcdj"
    json_schema: dict = {"address": address}
    response: Response = await client.post("/api/v1/tron/wallet", json=json_schema)
    data: dict = response.json()

    assert response.status_code == 201
    assert data["address"] == json_schema["address"]
    assert len(data["address"]) == 34

    async with ioc_container() as cont:
        wallet_dm: WalletQueryDm = await cont.get(WalletQueryDm)
        wallets_orm: list[WalletQueryOrm] = await wallet_dm.get_by_address(address=address)

        assert wallets_orm
