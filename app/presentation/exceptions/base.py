from abc import (
    ABC,
    abstractmethod,
)

from share.exceptions import CustomException


class PresentationException(CustomException, ABC):
    @property
    @abstractmethod
    def message(self) -> str:
        return "Presentation exception"