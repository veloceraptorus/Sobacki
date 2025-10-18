from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        extra='ignore',
        env_file='.env'
    )
    BASE_ROUTE_PATH: str = '/api/v1'
    # WELCOME_MSG: str = ''
    # OPTION_OF_SHIT: str = 'mocha'


settings = Settings()
