from ._crud_persons import CrudPerson
from ._crud_users import CrudUsers


class Crud(CrudUsers, CrudPerson):
    pass
