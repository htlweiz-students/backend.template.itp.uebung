from typing import override

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from ._base import Base


class Entity(Base):
    """Represents an entity with a unique id, name, and type. This class is a part of the polymorphic inheritance scheme where entities can be of different types.

    Attributes:
        id (int): The unique identifier for the entity.
        name (str): The name of the entity.
        type (str): The type of the entity.
    """

    __tablename__: str = "entities"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(length=255))
    type: Mapped[str] = mapped_column(String())

    @override
    def __repr__(self) -> str:
        return f"Entity(id={self.id}, name='{self.name}')"

    __mapper_args__: dict[str, str] = {
        "polymorphic_identity": "entities",
        "polymorphic_on": "type",
    }

