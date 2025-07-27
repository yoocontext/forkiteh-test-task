from fastapi import APIRouter
from dishka.integrations.fastapi import DishkaRoute

from presentation.api.v1.tron.wallet.handlers import router as wallet_router


router = APIRouter(
    prefix="/tron",
    route_class=DishkaRoute,
)

router.include_router(wallet_router)


