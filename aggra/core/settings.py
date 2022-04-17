from typing import List
from pydantic import BaseSettings, AnyUrl


class CeleryConfig(BaseSettings):
    broker_url: AnyUrl
    result_backend: AnyUrl
    include: List[str] = []

    class Config:
        env_prefix = 'AGGRA_CELERY_'
        env_file = '.env'


class Settings(BaseSettings):
    db_uri: AnyUrl = "postgresql://postgres:aggra@localhost:5432/aggra"
    redis_uri: AnyUrl = "redis://:aggra@localhost:6379"
    rabbitmq_uri: AnyUrl = "amqp://admin:aggra@localhost:5672"
    database_uri: AnyUrl = "postgresql://postgres:aggra@localhost:5432/postgres"
    # jwt token expire time
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 7 * 24 * 60
    # password salt
    SECRET_KEY: str = "aggra"
    version = "0.0.1"

    class Config:
        env_prefix = 'AGGRA_'
        env_file = '.env'


settings = Settings()
