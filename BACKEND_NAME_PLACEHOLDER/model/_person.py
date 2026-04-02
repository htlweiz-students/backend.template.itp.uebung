from typing import override

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from ._entity import Entity


class Person(Entity):
    """
    Represents a person in the database.

    Attributes:
        id (int): The unique identifier of the person.
        first_name (str): The first name of the person.
        last_name (str, property): The last name of the person.
            This is also accessible as the 'name' attribute.

    Methods:
        __repr__(self): Returns a string representation of the person.

    """

    __tablename__: str = "persons"

    id: Mapped[int] = mapped_column(ForeignKey(column=Entity.id), primary_key=True)
    first_name: Mapped[str] = mapped_column(String(length=255))

    @property
    def last_name(self) -> str:
        """
        The last name of the person.
        This is also accessible as the 'name' attribute.

        Returns:
            str: The last name of the person.
        """
        return self.name

    @last_name.setter
    def last_name(self, value: str) -> None:
        """
        Sets the last name of the person.
        This also updates the 'name' attribute.

        Args:
            value (str): The new last name of the person.
        """
        self.name = value  # pyright: ignore [reportUnannotatedClassAttribute]

    @override
    def __repr__(self):
        return f"Person(id={self.id}, last_name='{self.name}', first_name='{self.first_name}')"

    __mapper_args__: dict[str, str] = {
        "polymorphic_identity": "persons",
    }
