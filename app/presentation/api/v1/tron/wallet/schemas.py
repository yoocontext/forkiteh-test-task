from decimal import Decimal

from pydantic import BaseModel


class FetchWalletTronInSchema(BaseModel):
    address: str


class FetchWalletTronOutSchema(BaseModel):
    address: str
    bandwidth: int
    energy: int
    balance_trx: Decimal
