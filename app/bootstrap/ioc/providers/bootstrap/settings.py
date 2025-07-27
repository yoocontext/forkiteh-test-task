from dishka import (
    Provider,
    Scope,
    provide,
)

from bootstrap.settings.base import CommonSettings
from bootstrap.settings.dev import DevSettings


class SettingsProvider(Provider):
    scope = Scope.APP

    @provide
    def common(self) -> CommonSettings:
        settings = DevSettings()

        return settings