from fastapi import FastAPI

from ..config import get_logger
from ..crud import Crud
from ..schema import UserBase, UserFilter, UserFull

log = get_logger()

def define_routes(app: FastAPI, crud: Crud) -> None:
    pass
    @app.get(path="/user/")
    async def get_user(filter: str | None = None):
        return crud.get_users(UserFilter(name=filter))
    assert get_user

    @app.post(path="/user/")
    async def post_user(user: UserBase)->UserFull:
        return crud.create_user(user)
    assert post_user
