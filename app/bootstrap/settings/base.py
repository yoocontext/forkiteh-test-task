from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class CommonSettings(BaseSettings):
    pg: "PgSettings"
    tron: "TronSettings"


class PgSettings(BaseSettings):
    model_config = SettingsConfigDict(extra="allow")

    db: str = Field(alias="POSTGRES_DB", default="POSTGRES_DB")
    user: str = Field(alias="POSTGRES_USER", default="POSTGRES_USER")
    password: str = Field(alias="POSTGRES_PASSWORD", default="POSTGRES_PASSWORD")
    host: str = Field(alias="POSTGRES_HOST", default="POSTGRES_HOST")
    port: str = Field(alias="POSTGRES_PORT", default="POSTGRES_PORT")

    @property
    def postgres_url(self) -> str:
        return rf"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.db}"


class TronSettings(BaseSettings):
    model_config = SettingsConfigDict(extra="allow")

    network: str = Field(alias="TRON_NETWORK", default="NETWORK")
    api_key: str = Field(alias="TRON_API_KEY", default="API_KEY")
    endpoint_url: str = Field(alias="TRON_ENDPOINT_URL", default="ENDPOINT_URL")
