from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass

from share.custom_types import WalletAddress
from share.exceptions import CustomException


class TronExceptions(
    CustomException,
    ABC,
):
    @property
    @abstractmethod
    def message(self) -> str:
        return "Tron Exceptions"


@dataclass
class AddressNotFoundTronException(TronExceptions):
    address: WalletAddress | None

    @property
    def message(self) -> str:
        return fr"Tron address not found: {self.address}"


@dataclass
class BadAddressTronException(TronExceptions):
    address: WalletAddress | None

    @property
    def message(self) -> str:
        return fr"Bad Tron address: {self.address} format or checksum: address is invalid or malformed."
