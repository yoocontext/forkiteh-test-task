from fastapi import APIRouter
from dishka.integrations.fastapi import DishkaRoute


router = APIRouter(
    prefix="/tron",
    route_class=DishkaRoute,
)


