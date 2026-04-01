from sqlalchemy import Engine


class CrudBase:
    def __init__(self, engine: Engine):
        self._engine: Engine = engine
