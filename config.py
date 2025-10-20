from enum import Enum

from pydantic import HttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Browser(str, Enum):
    CHROME = "chrome"
    EDGE = "edge"
    FIREFOX = "firefox"


class ChromiumConfig(BaseSettings):
    options: list[str]


class FirefoxConfig(BaseSettings):
    options: list[str]


class BrowsersConfig(BaseSettings):
    chromium_config: ChromiumConfig
    firefox_config: FirefoxConfig
    page_load_strategy: str
    page_load_timeout: int


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

    def get_base_url(self):
        return f"{self.base_url}"


settings = Settings()
