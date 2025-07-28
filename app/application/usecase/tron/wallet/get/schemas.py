from dataclasses import dataclass
from decimal import Decimal


@dataclass
class GetWalletTronSchema:
    address: str
    bandwidth: int
    energy: int
    balance_trx: Decimal
