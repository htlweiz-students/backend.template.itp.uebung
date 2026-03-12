from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from backend.api._auth import hash_password, verify_password
from backend.crud import Crud
from backend.engine import get_engine
from backend.schema import (
    TodoCreate,
    TodoResponse,
    TodoUpdate,
    UserRegister,
    UserResponse,
)

security = HTTPBasic()

_crud: Crud | None = None


def get_crud() -> Crud:
    global _crud
    if not _crud:
        _crud = Crud(get_engine("local_postgres_config.json"))
    return _crud


def get_current_user(
    credentials: HTTPBasicCredentials = Depends(security),
    crud: Crud = Depends(get_crud),
) -> str:
    user = crud.get_user(credentials.username)
    if not user or not user.password_hash:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Basic"},
        )
    if not verify_password(credentials.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


def define_routes(app: FastAPI) -> None:

    @app.get("/")
    def get_root():
        return {"/"}

    # --- auth ---

    @app.post("/auth/register", response_model=UserResponse)
    def register(body: UserRegister, crud: Crud = Depends(get_crud)):
        if crud.get_user(body.user_name):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already taken",
            )
        password_hash = hash_password(body.password)
        user = crud.create_user(body.user_name, password_hash, body.name)
        return user

    # --- todos ---

    @app.get("/todos", response_model=list[TodoResponse])
    def get_todos(
        user_name: str = Depends(get_current_user),
        crud: Crud = Depends(get_crud),
    ):
        return crud.get_todos(user_name)

    @app.post("/todos", response_model=TodoResponse)
    def create_todo(
        body: TodoCreate,
        user_name: str = Depends(get_current_user),
        crud: Crud = Depends(get_crud),
    ):
        return crud.create_todo(user_name, body.title)

    @app.put("/todos/{todo_id}", response_model=TodoResponse)
    def update_todo(
        todo_id: int,
        body: TodoUpdate,
        user_name: str = Depends(get_current_user),
        crud: Crud = Depends(get_crud),
    ):
        todos = crud.get_todos(user_name)
        if not any(t.id == todo_id for t in todos):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Todo not found",
            )
        return crud.update_todo(todo_id, body.done)

    @app.delete("/todos/{todo_id}", response_model=TodoResponse)
    def delete_todo(
        todo_id: int,
        user_name: str = Depends(get_current_user),
        crud: Crud = Depends(get_crud),
    ):
        todos = crud.get_todos(user_name)
        if not any(t.id == todo_id for t in todos):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Todo not found",
            )
        return crud.delete_todo(todo_id)
