from abc import (
    ABC,
    abstractmethod,
)


class CustomException(Exception, ABC):
    @property
    @abstractmethod
    def message(self) -> str:
        return "Custom exception"
