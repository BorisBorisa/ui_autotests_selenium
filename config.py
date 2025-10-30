from enum import Enum

from pydantic import HttpUrl, BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

from tools.schemas.test_data_model import TestData


class Browser(str, Enum):
    CHROME = "chrome"
    EDGE = "edge"
    FIREFOX = "firefox"


class ChromiumConfig(BaseModel):
    options: list[str]


class FirefoxConfig(BaseModel):
    options: list[str]


class BrowsersConfig(BaseModel):
    chromium_config: ChromiumConfig
    firefox_config: FirefoxConfig
    page_load_strategy: str
    page_load_timeout: int
    wait_timeout: float
    wait_poll_frequency: float


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        extra="allow",
        env_file=".env.example",
        env_file_encoding="utf-8",
        env_nested_delimiter=".",
    )

    browsers: list[Browser]
    base_url: HttpUrl
    browsers_config: BrowsersConfig
    test_data: TestData

    def get_base_url(self):
        return f"{self.base_url}"


settings = Settings()
