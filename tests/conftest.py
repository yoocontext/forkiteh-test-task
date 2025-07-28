import asyncio
import pytest
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from your_project.models import Base  # импортируй Base из своего проекта
from your_project.main import get_db  # зависимость FastAPI для замены

# URL тестовой базы, обычно указывают отдельную БД типа "postgresql+asyncpg://..."
TEST_DATABASE_URL = "postgresql+asyncpg://postgres:password@localhost:5432/test_db"

# Создаём движок и фабрику сессий
engine_test = create_async_engine(TEST_DATABASE_URL, echo=False)
AsyncTestingSessionLocal = async_sessionmaker(
    bind=engine_test,
    class_=AsyncSession,
    expire_on_commit=False,
)

# Создание и удаление таблиц перед и после всех тестов
@pytest.fixture(scope="session", autouse=True)
async def prepare_database():
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture()
async def async_db_session():
    async with AsyncTestingSessionLocal() as session:
        yield session


@pytest.fixture()
def override_get_db(async_db_session):
    async def _override_get_db():
        yield async_db_session
    return _override_get_db


@pytest.fixture(autouse=True)
def apply_db_override(override_get_db):
    from your_project.main import app  # импортируй FastAPI приложение
    app.dependency_overrides[get_db] = override_get_db