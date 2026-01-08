from pydantic_settings import BaseSettings
from typing import Optional
from functools import lru_cache


class Settings(BaseSettings):
    """Application setting using pydantic"""

    # API
    OPENAI_API_KEY: str
    ANTHROPIC_API_KEY: Optional[str] = None
    SENDGRID_API_KEY: Optional[str] = None
    APIFY_API_TOKEN: Optional[str] = None

    # DATABASE
    DATABASE_URL: str

    # RADIS
    RADIS_URL: str

    # APPLICATION
    APP_ENV: str = "development"
    SECRET_KEY: str
    API_VERSION: str = "v1"
    LOG_LEVEL: str = "INFO"

    # SCRAPING
    SCRAPING_RATE_LIMIT: int = 3
    SCRAPPING_TIMEOUT: int = 30
    USE_PROXIES: bool = False
    PROXY_URL: Optional[str] = None

    # MATCHING
    MIN_MATCH_SCORE: float = 70.0

    #EMAIL
    SENDER_EMAIL: str
    SENDER_NAME: str= "SHAIKE Partnerships"

    # FRONTEND
    FRONTEND_URL: str = "http://localhost:3000"

    class Config:
        env_file = ".env"
        case_sensitive= True
@lru_cache
def get_settings() -> Settings:
    """Get cache settings instance"""
    return Settings()

