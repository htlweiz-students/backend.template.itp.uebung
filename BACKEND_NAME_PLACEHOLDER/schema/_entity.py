"""
A module containing Pydantic models for managing entities.
"""

from pydantic import BaseModel

__all__ = ['EntityBase', 'EntityFull', 'EntityFilter']

"""
Base model for an entity, containing the name attribute.
"""
class EntityBase(BaseModel):
    """
    A Pydantic base model for an entity with a required `name` attribute of type string.

    Attributes:
        name (str): The name of the entity.
    """
    name: str

"""
A full entity model, extending EntityBase and adding an `id` attribute.
"""
class EntityFull(EntityBase):
    """
    A Pydantic model for a full entity, inheriting from EntityBase and adding an `id` attribute of
    type integer.

    Attributes:
        id (int): The unique identifier of the entity.
        name (str): The name of the entity.
    """
    id: int

"""
A filter model for entities, allowing optional `name` and `id` attributes.
"""
class EntityFilter(BaseModel):
    """
    A Pydantic model for a filter on entities, allowing optional `name` and `id` attributes. Both
    can be of type string or integer.

    Attributes:
        name (str | None): The optional name to filter by.
        id (int | None): The optional identifier to filter by.
    """
    name: str | None
    id: int | None

