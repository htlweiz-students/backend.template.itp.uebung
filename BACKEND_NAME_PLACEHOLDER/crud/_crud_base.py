"""
A base class for CRUD (Create, Read, Update, Delete) operations using SQLAlchemy's Engine.

Attributes:
    _engine (Engine): The SQLAlchemy engine instance used for database connections.
"""

from sqlalchemy import Engine


class CrudBase:
    def __init__(self, engine: Engine):
        """
        Initializes the CRUDBase object with the given SQLAlchemy engine instance.

        Args:
            engine (Engine): The SQLAlchemy engine instance used for database connections.
        """
        self._engine: Engine = engine
