from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    settlebridge_api_url: str = "http://localhost:8000"
    settlebridge_api_key: str = ""
    anthropic_api_key: str = ""
    openai_api_key: str = ""
    log_level: str = "INFO"
    env: str = "development"


settings = Settings()
