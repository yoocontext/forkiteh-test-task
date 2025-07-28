from datetime import datetime
from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel


class FetchWalletTronInSchema(BaseModel):
    address: str


class FetchWalletTronOutSchema(BaseModel):
    address: str
    bandwidth: int
    energy: int
    balance_trx: Decimal


class GetWalletTronOutSchema(BaseModel):
    wallet_uid_last: UUID | None
    created_at_last: datetime | None
    wallets: list["WalletTronOutSchema"]


class WalletTronOutSchema(BaseModel):
    address: str
    bandwidth: int
    energy: int
    balance_trx: Decimal