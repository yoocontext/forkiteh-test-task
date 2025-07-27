from fastapi import (
    FastAPI,
    HTTPException,
)
from starlette.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_500_INTERNAL_SERVER_ERROR,
)

from infra.tron.exceptions import (
    BadAddressTronException,
    AddressNotFoundTronException,
)
from share.exceptions import CustomException

exceptions_map: dict[type[CustomException], int] = {
    CustomException: HTTP_500_INTERNAL_SERVER_ERROR,
    BadAddressTronException: HTTP_400_BAD_REQUEST,
    AddressNotFoundTronException: HTTP_404_NOT_FOUND,
}

def register_exception_handlers(app: FastAPI):
    @app.exception_handler(Exception)
    async def handler(request, exc: CustomException):
        if exceptions_map.get(type(exc), None):
            status: int = exceptions_map.get(type(exc))
            raise HTTPException(status_code=status, detail=exc.message)
