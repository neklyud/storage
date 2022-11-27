import logging

from pydantic import BaseSettings, AnyUrl
from functools import lru_cache

logger = logging.getLogger('uvicorn')


class Settings(BaseSettings):
    environment: str = 'dev'
    testing: bool = False
    database_url: AnyUrl = None


@lru_cache()
def get_settings():
    return Settings()