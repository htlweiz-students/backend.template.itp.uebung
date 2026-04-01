from ..model import Person
from ._crud_entity import CrudEntity


class CrudPerson(CrudEntity):

    def get_persons(self, filter: str | None = None) -> list[Person]:
        if not filter:
            return []
        return []
