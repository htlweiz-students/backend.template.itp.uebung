from fastapi import FastAPI

from ..crud import Crud
from ..engine import get_engine
from ._routes import define_routes

_app: FastAPI | None = None
_crud: Crud | None = None


"""
Function to build and initialize the application. This function sets up the CRUD object and FastAPI
instance, and defines the routes if they haven't been defined yet. If environment variable
'CONFIG_FILE' is set, it uses that file for configuration.

Returns:
    The initialized FastAPI application instance.
"""


def build_app():

    global _crud
    """
    Initialize the CRUD object with the given database engine. If no CRUD object has been
    initialized yet, it reads the config file from environment variable 'CONFIG_FILE' and
    creates an engine using that.
    """
    if not _crud:
        engine = get_engine()
        _crud = Crud(engine)

    global _app
    """
    Initialize the FastAPI instance and define the routes if no such instance has been initialized
    yet.
    """
    if not _app:
        _app = FastAPI()
        define_routes(_app, _crud)

    return _app
