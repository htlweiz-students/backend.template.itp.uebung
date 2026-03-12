import os

from fastapi import FastAPI

from BACKEND_NAME_PLACEHOLDER.crud import Crud
from BACKEND_NAME_PLACEHOLDER.engine import get_engine

from ._routes import define_routes

_app: FastAPI | None = None
_crud: Crud | None = None


def build_app():
    global _crud
    if not _crud:
        config_file = ""
        if "CONFIG_FILE" in os.environ:
            config_file = os.environ["CONFIG_FILE"]
        engine = get_engine(config_file)
        _crud = Crud(engine)

    global _app
    if not _app:
        _app = FastAPI()
        define_routes(_app, _crud)

    return _app
