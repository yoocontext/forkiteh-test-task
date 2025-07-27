from functools import wraps
from tronpy.exceptions import (
    AddressNotFound,
    BadAddress,
)

from infra.tron.exceptions import (
    BadAddressTronException,
    AddressNotFoundTronException,
)
from share.custom_types import WalletAddress


def handle_tronpy_errors(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        address: WalletAddress | None = kwargs.get("address")

        try:
            return await func(*args, **kwargs)

        except AddressNotFound:
            raise AddressNotFoundTronException(address=address)

        except BadAddress:
            raise BadAddressTronException(address=address)

    return wrapper