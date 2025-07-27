from fastapi import FastAPI
from dishka import AsyncContainer
from dishka.integrations.fastapi import setup_dishka

from bootstrap.ioc.container import get_container
from presentation.lifespan import lifespan
from presentation.api import v1_router
from presentation.exceptions.handler import register_exception_handlers


def create_app() -> FastAPI:
    app = FastAPI(
        debug=False,
        lifespan=lifespan,
        title="forkiteh",
        summary="Microservice built with FastAPI to retrieve TRON address information",
        docs_url="/docs",
        root_path="/api",
    )
    app.include_router(v1_router)
    register_exception_handlers(app=app)

    container: AsyncContainer = get_container()
    setup_dishka(container=container, app=app)

    return app