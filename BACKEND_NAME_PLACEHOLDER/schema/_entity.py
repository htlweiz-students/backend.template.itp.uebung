from pydantic import BaseModel


class EntityBase(BaseModel):
    name: str


class EntityFull(EntityBase):
    id: int


class EntityFilter(BaseModel):
    name: str | None
    id: int | None
