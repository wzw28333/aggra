from typing import ContextManager
from sqlmodel import Session
from fastapi import Request
from aggra.app.base import Aggra
from redis import Redis


def get_app(request: Request) -> Aggra:
    return request.app.state.aggra


def get_redis(request: Request) -> Redis:
    return request.app.state.aggra.redis


def get_session(request: Request) -> ContextManager[Session]:
    return request.app.state.aggra.get_session
