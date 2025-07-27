from abc import ABC

from sqlalchemy.ext.asyncio import AsyncSession


class BaseDm(ABC):
    session: AsyncSession
