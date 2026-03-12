from pydantic import BaseModel
from typing import Optional


class TodoCreate(BaseModel):
    title: str


class TodoUpdate(BaseModel):
    title: Optional[str] | None
    done: Optional[bool] | None


class TodoResponse(BaseModel):
    id: int
    title: str
    done: bool

    model_config = {"from_attributes": True}


class UserRegister(BaseModel):
    user_name: str
    password: str
    name: str


class UserResponse(BaseModel):
    user_name: str

    model_config = {"from_attributes": True}
