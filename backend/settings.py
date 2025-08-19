from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SECRET_KEY: str = '0f2963b4573016418f474d9398ed6776afa7e2c0baa1b9edefd711c99f0e8ca9'
    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    class Config:
        env_file = ".env"

settings = Settings()