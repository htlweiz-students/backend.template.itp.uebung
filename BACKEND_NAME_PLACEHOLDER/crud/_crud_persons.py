from ..model import Person
from ._crud_entity import CrudEntity


"""
CrudPerson class for managing a database of Person entities.

This class provides methods to create, read, update, and delete Person objects from the database.
The database is abstracted away, making it easy to switch between different databases or data storage solutions.

Methods:
    - get_persons(filter: str | None = None) -> list[Person]: Retrieves a list of Person entities based on a provided filter (optional). If no filter is provided, returns an empty list.
"""
class CrudPerson(CrudEntity):

    def get_persons(self, filter: str | None = None) -> list[Person]:
        if not filter:
            return []
        return []

