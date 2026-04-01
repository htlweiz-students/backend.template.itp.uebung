from fastapi import FastAPI

from ..crud import Crud
from ._entity_routes import define_routes as define_entity_routes


def define_routes(app: FastAPI, crud: Crud) -> None:
    """Defines the routes for the application."""

    @app.get("/")
    async def get_root():
        """
        This function returns an empty dictionary, representing the root of the API.

        Returns:
            A dictionary with one key "/" and value "api_root".

        Example:
            >>> await get_root()
            {'/': 'api_root'}
        """
        return {"": {"/": "api_root"}}

    assert get_root

    define_entity_routes(app, crud)

