from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from backend.api._auth import (
    create_access_token,
    decode_token,
    hash_password,
    verify_password,
)
from backend.crud import Crud
from backend.engine import get_engine
from backend.schema import (
    TodoCreate,
    TodoResponse,
    TodoUpdate,
    Token,
    UserLogin,
    UserRegister,
)

security = HTTPBearer()

_crud: Crud | None = None


def get_crud() -> Crud:
    global _crud
    if not _crud:
        # For PostgreSQL: get_engine("local_postgres_config.json")
        _crud = Crud(get_engine())
    return _crud


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    crud: Crud = Depends(get_crud),
) -> str:
    user_name = decode_token(credentials.credentials)
    if not user_name:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        )
    user = crud.get_user(user_name)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
        )
    return user_name


def define_routes(app: FastAPI) -> None:

    @app.get("/")
    def get_root():
        return {"/"}

    # --- auth ---

    @app.post("/auth/register", response_model=Token)
    def register(body: UserRegister, crud: Crud = Depends(get_crud)):
        if crud.get_user(body.user_name):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already taken",
            )
        password_hash = hash_password(body.password)
        crud.create_user(body.user_name, password_hash, body.name)
        token = create_access_token(body.user_name)
        return Token(access_token=token, token_type="bearer")

    @app.post("/auth/login", response_model=Token)
    def login(body: UserLogin, crud: Crud = Depends(get_crud)):
        user = crud.get_user(body.user_name)
        if not user or not user.password_hash:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials",
            )
        if not verify_password(body.password, user.password_hash):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials",
            )
        token = create_access_token(body.user_name)
        return Token(access_token=token, token_type="bearer")

    # --- todos ---

    @app.get("/todos", response_model=list[TodoResponse])
    def get_todos(
        user_name: str = Depends(get_current_user),
        crud: Crud = Depends(get_crud),
    ):
        return crud.get_todos(user_name)

    @app.post("/todos", response_model=TodoResponse, status_code=201)
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
        todo = crud.update_todo(todo_id, body.done)
        return todo

    @app.delete("/todos/{todo_id}", status_code=204)
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
        crud.delete_todo(todo_id)
