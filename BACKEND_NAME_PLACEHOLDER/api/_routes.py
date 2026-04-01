from fastapi import FastAPI, HTTPException

from ..crud import Crud
from ..schema import EntityBase, EntityFilter, EntityFull


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


    @app.get(path="/entity/", response_model=list[EntityFull])
    async def get_entities(search_string: str | None = None) -> list[EntityFull]:
        """
        Retrieves a list of full entities based on the provided search string.
        If no search string is provided, all entities are returned.

        Args:
            search_string (str, optional): The keyword to filter the entities by name or id. Defaults to None.

        Returns:
            list[EntityFull]: A list of full entities based on the given search string.
        """
        if search_string is not None:
            filter = EntityFilter(name=search_string, id=None)
        else:
            filter = EntityFilter(name=None, id=None)
        return crud.get_entities(filter)

    assert get_entities

    @app.get(path="/entity/{id}/", response_model=EntityFull)
    async def get_entity(id: int):
        """Retrieves a single entity based on the provided ID.

        If an entity with the given id is not found, raises an HTTPException with status 404 and message "No entity found for {id}"

        Args:
            id (int): The unique identifier of the entity to retrieve.

        Returns:
            Entity: The retrieved entity object.

        Raises:
            HTTPException: When no entity is found with the provided id, with status 404 and message "No entity found for {id}".
        """
        filter = EntityFilter(name=None, id=id)
        result = crud.get_entities(filter)
        if len(result) == 1:
            return result[0]
        raise HTTPException(404, f"No entity found for {id}")

    assert get_entity

    @app.post(path="/entity/", response_model=EntityFull)
    async def post_entity(entity: EntityBase) -> EntityFull:
        """
        Creates a new entity based on the provided entity base and returns the created entity's response object.
    
        Args:
            entity (EntityBase): The entity to be created with required fields filled.
    
        Returns:
            EntityResponse: Response object containing details of the created entity.
        """
        return crud.create_entity(entity)

    assert post_entity

    @app.delete(path="/entity/{id}/")
    async def delete_entity(id: int) -> None:
        """
        Deletes an entity based on the provided ID. This function utilizes the CRUD (Create, Read, Update, Delete) operations
        to perform deletion of the specified entity.
    
        :param id: The unique identifier of the entity to be deleted.
        :return: None, as this function does not return a value upon successful execution.
        """
        crud.delete_entity(id)

    assert delete_entity
