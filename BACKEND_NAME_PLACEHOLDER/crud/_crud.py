from ._crud_person import CrudPerson
from ._crud_user import CrudUsers


class Crud(CrudUsers, CrudPerson):
    pass
