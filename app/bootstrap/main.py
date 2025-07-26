from fastapi import FastAPI

from presentation.api import v1_router
from presentation.exceptions.handler import register_exception_handlers


async def create_app() -> FastAPI:
    app = FastAPI(
        debug=False,
        routes=[v1_router],
        title="forkiteh",
        summary="Microservice built with FastAPI to retrieve TRON address information",
        docs_url="/docs",
        root_path="/api",
    )
    register_exception_handlers(app=app)

    return app