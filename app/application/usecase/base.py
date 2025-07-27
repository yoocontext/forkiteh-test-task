from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass


@dataclass
class BaseCommand(ABC):
    ...


@dataclass
class BaseResult(ABC):
    ...


@dataclass
class BaseUseCase(ABC):
    async def act(self, command: BaseCommand) -> BaseResult:
        ...
