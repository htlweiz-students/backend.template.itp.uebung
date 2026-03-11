from sqlalchemy import Engine
from sqlalchemy.orm import Session

from BACKEND_NAME_PLACEHOLDER.model import Entity, Person, User
from BACKEND_NAME_PLACEHOLDER.schema import EntityBase, EntityFull, UserBase, UserFull


class Crud:
    def __init__(self, engine: Engine):
        self._engine: Engine = engine

    def get_users(self, filter: str | None = None) -> list[User]:
        if not filter:
            return []
        return []

    def get_persons(self, filter: str | None = None) -> list[Person]:
        if not filter:
            return []
        return []

    def get_entities(self, filter: str | None = None) -> list[Entity]:
        if not filter:
            return []
        return []

    def create_entity(self, new_entity: EntityBase, session: Session|None=None) -> EntityFull:
        with Session(bind=self._engine) as session:
            entity = self._create_entity(session, new_entity)
            session.commit()
            entity_full = EntityFull(id=entity.id, name=entity.name)
            return entity_full


    def create_user(self, new_user: UserBase) -> UserFull:
        with Session(bind=self._engine) as session:
            new_entity = EntityBase(name=new_user.name)
            entity = self._create_entity(session, new_entity)
            user = User()
            user.user_name = new_user.user_name
            user.password_hash = new_user.password_hash
            user.entity = entity
            session.add(user)
            session.commit()
            user_full = UserFull(
                                 user_name=user.user_name,
                                 name=entity.name,
                                 password_hash=user.password_hash,
                                 id=user.entity_id)
            return user_full

    def _create_entity(self, session : Session, new_entity : EntityBase) -> Entity:
        entity= Entity(name=new_entity.name)
        session.add(entity)
        return entity
