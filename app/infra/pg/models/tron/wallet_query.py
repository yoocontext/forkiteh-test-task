from decimal import Decimal

from sqlalchemy import BigInteger, String, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from infra.pg.models.common.base import BaseOrm
from infra.pg.models.common.mixins import (
    UidPkMixin,
    CreateAtMixin,
    UpdateAtMixin,
)


class WalletQueryOrm(
    BaseOrm,
    UidPkMixin,
    CreateAtMixin,
    UpdateAtMixin,
):
    __tablename__ = 'wallet_queries'

    address: Mapped[str] = mapped_column(String(64), index=True)
    bandwidth: Mapped[int] = mapped_column(BigInteger)
    energy: Mapped[int] = mapped_column(BigInteger)
    balance_trx: Mapped[Decimal] = mapped_column(Numeric(20, 8))

    def __repr__(self):
        return f"<WalletQuery(address={self.address}, balance_trx={self.balance_trx})>"