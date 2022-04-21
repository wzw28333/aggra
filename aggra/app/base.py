from contextlib import contextmanager

import redis
import uvicorn
from celery import Celery
from fastapi import FastAPI
from sqlmodel import create_engine, Session

from aggra.core.settings import settings, CeleryConfig
from aggra.utils.logger import logger


class Aggra:
    def __init__(
            self,
            debug: bool = False
    ):
        self._debug = debug
        self._celery_config = CeleryConfig(
            broker_url=settings.rabbitmq_uri,
            result_backend=settings.redis_uri,
        )

        self._version = settings.version
        self._redis_pool = self.setup_redis_pool()
        self._sqlmodel_engine = self.setup_sqlmodel_engine()
        self.celery = self.setup_celery()
        self.server = self.setup_fastapi()

    def setup_redis_pool(self) -> redis.ConnectionPool:
        logger.debug("Setting up Redis Pool")
        redis_pool = redis.ConnectionPool.from_url(settings.redis_uri)
        return redis_pool

    @property
    def redis_conn(self) -> redis.Redis:
        return redis.Redis(connection_pool=self._redis_pool)

    @contextmanager
    def get_session(self):
        logger.debug("Getting Session")
        session = Session(bind=self._sqlmodel_engine)
        try:
            yield session
        except Exception as e:
            logger.error(e)
            session.rollback()
            raise
        finally:
            session.close()

    def setup_sqlmodel_engine(self):
        logger.debug("Setting up SQLModel Engine")
        return create_engine(settings.database_uri, echo=self._debug)

    def get_version(self):
        return self._version

    def setup_celery(self) -> Celery:
        logger.debug("Setting up Celery")
        app = Celery("aggra", config_source=self._celery_config)
        return app

    def setup_fastapi(self) -> FastAPI:
        from aggra.app.api.api import router
        logger.debug("Setting up FastAPI")
        app = FastAPI(
            debug=self._debug,
            title="Aggra",
            description="Aggra is a microservice for managing and monitoring",
            version=self._version
        )
        app.include_router(router)

        @app.on_event("startup")
        def startup():
            logger.debug("Starting up")
            app.state.aggra = self

        return app
