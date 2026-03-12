from contextlib import asynccontextmanager

from fastapi import FastAPI

from backend.engine import get_engine

from ._routes import define_routes

_app: FastAPI | None = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    get_engine()
    yield


def build_app():
    global _app
    if not _app:
        _app = FastAPI(lifespan=lifespan)
        define_routes(_app)

    return _app
