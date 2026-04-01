"""
Module containing User data models for application.

This module defines two classes: UserBase and UserFull, both derived from Pydantic's BaseModel.
These classes represent the structure of user data in the application, with UserBase as a base model
containing common attributes like user_name, name, and password_hash, and UserFull extending it by
adding an id attribute.
"""

from pydantic import BaseModel

class UserBase(BaseModel):
    """
    Represents the base structure of a User object in the application.

    Attributes:
        user_name (str): The username for the user.
        name (str): The full name of the user.
        password_hash (str): The hashed password of the user.
    """
    user_name: str
    name: str
    password_hash: str

class UserFull(UserBase):
    """
    Represents a complete User object in the application, inheriting from UserBase and adding an
    id attribute.

    Attributes:
        id (int): The unique identifier for the user.
    """
    id: int

