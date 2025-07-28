from application.usecase.tron.wallet.get.schemas import GetWalletTronSchema
from infra.pg.models import WalletQueryOrm


def orm_to_use_case_schemas_mapper(
    wallets_orm: list[WalletQueryOrm]
) -> list[GetWalletTronSchema]:

    result: list[GetWalletTronSchema] = []

    for wallet_orm in wallets_orm:

        schema = GetWalletTronSchema(
            address=wallet_orm.address,
            bandwidth=wallet_orm.bandwidth,
            energy=wallet_orm.energy,
            balance_trx=wallet_orm.balance_trx,
        )

        result.append(schema)

    return result