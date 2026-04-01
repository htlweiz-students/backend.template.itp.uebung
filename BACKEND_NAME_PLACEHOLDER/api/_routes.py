from fastapi import FastAPI, HTTPException

from ..crud import Crud
from ..schema import EntityBase, EntityFilter, EntityFull


def define_routes(app: FastAPI, crud: Crud) -> None:

    @app.get("/")
    def get_root():
        return {""}

    assert get_root

    @app.get(path="/entity/")
    def get_entities(search_string: str | None = None) -> list[EntityFull]:
        filter = EntityFilter(name=search_string, id=None)
        return crud.get_entities(filter)

    assert get_entities

    @app.get(path="/entity/{id}/")
    def get_entity(id: int):
        filter = EntityFilter(name=None, id=id)
        result = crud.get_entities(filter)
        if len(result) == 1:
            return result[0]
        raise HTTPException(404, f"No entity found for {id}")

    assert get_entity

    @app.post(path="/entity/")
    def post_entity(entity: EntityBase) -> EntityFull:
        return crud.create_entity(entity)

    assert post_entity

    @app.delete(path="/entity/{id}/")
    def delete_entity(id: int):
        crud.delete_entity(id)

    assert delete_entity
