from application.usecase.tron.wallet.get.schemas import GetWalletTronSchema
from presentation.api.v1.tron.wallet.schemas import WalletTronOutSchema


def result_to_out_schema(
    wallets_results: list[GetWalletTronSchema]
) -> list[WalletTronOutSchema]:

    result: list[WalletTronOutSchema] = []

    for wallet_result in wallets_results:

        schema = WalletTronOutSchema(
            address=wallet_result.address,
            bandwidth=wallet_result.bandwidth,
            energy=wallet_result.energy,
            balance_trx=wallet_result.balance_trx,
        )

        result.append(schema)

    return result