from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Настройки приложения.

    Attributes:
        app_title (str): Название приложения.
        DB_HOST (str): адрес бд.
        DB_PORT (int): порт бд.
        DB_USER (str): имя пользователя бд.
        DB_PASS (str): пароль пользователя бд.
        DB_NAME (str): имя бд.
        model_config (SettingsConfigDict): Конфигурация модели.
    """
    app_title: str

    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    @property
    def DATABASE_URL(self):
        return (
            f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@'
            f'{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'
        )

    model_config = SettingsConfigDict(env_file='.env')


settings = Settings()
