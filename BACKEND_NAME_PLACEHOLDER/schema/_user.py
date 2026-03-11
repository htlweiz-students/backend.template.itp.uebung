
from pydantic import BaseModel


class UserBase(BaseModel):
    user_name: str
    name: str
    password_hash: str


class UserFull(UserBase):
    id: int
