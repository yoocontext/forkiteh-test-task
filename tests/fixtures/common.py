import os
import sys

from fastapi import FastAPI
from httpx import ASGITransport, AsyncClient

from tests.ioc.container import get_test_container

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'app')))

from collections.abc import Generator

import pytest
from alembic.command import upgrade
from alembic.config import Config as AlembicConfig
from dishka import AsyncContainer
from dishka.integrations.fastapi import setup_dishka
from testcontainers.postgres import PostgresContainer

from app.bootstrap.main import create_app


@pytest.fixture(scope="session")
def postgres_url() -> Generator[str, None, None]:
    postgres = PostgresContainer("postgres:16-alpine")
    if os.name == "nt":  # TODO: workaround from testcontainers/testcontainers-python#108
        postgres.get_container_host_ip = lambda: "localhost"
    try:
        postgres.start()
        postgres_url_ = postgres.get_connection_url().replace("psycopg2", "asyncpg")
        yield postgres_url_
    finally:
        postgres.stop()


@pytest.fixture(scope="session")
def alembic_config(postgres_url: str) -> AlembicConfig:
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # корень проекта
    alembic_ini_path = os.path.join(base_dir, "app/alembic.ini")

    alembic_cfg = AlembicConfig(alembic_ini_path)
    alembic_cfg.set_main_option("sqlalchemy.url", postgres_url)

    return alembic_cfg


@pytest.fixture(scope="session", autouse=True)
def _upgrade_schema_db(alembic_config: AlembicConfig) -> None:
    upgrade(alembic_config, "head")


@pytest.fixture(scope="session")
def ioc_container(postgres_url: str) -> AsyncContainer:
    test_container: AsyncContainer = get_test_container(connection_string=postgres_url)

    return test_container


@pytest.fixture(scope="session")
def app(
    postgres_url: str,
    ioc_container: AsyncContainer,
) -> FastAPI:
    app = create_app()

    setup_dishka(ioc_container, app)

    return app


@pytest.fixture(scope="session")
async def client(app: FastAPI):
    transport = ASGITransport(app=app)

    async with AsyncClient(transport=transport, base_url="http://test") as client:
        yield client


