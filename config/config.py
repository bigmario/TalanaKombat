from pydantic import BaseSettings


class Settings(BaseSettings):
    host: str
    log_level: str
    reload: int

    class Config:
        env_file = ".env"
