from pydantic import BaseModel


class TodoCreate(BaseModel):
    title: str


class TodoUpdate(BaseModel):
    done: bool


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
