from fastapi import APIRouter
from dishka.integrations.fastapi import DishkaRoute

from presentation.api.v1.tron.handlers import router as tron_router


router = APIRouter(
    prefix="/v1",
    route_class=DishkaRoute,
)

router.include_router(tron_router)




