from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Tutor Backend"

    class Config:
        env_file = ".env"


settings = Settings()
