from sqlalchemy import Engine, delete
from sqlalchemy.orm import Session
from sqlalchemy.sql import select

from BACKEND_NAME_PLACEHOLDER.config import get_logger
from BACKEND_NAME_PLACEHOLDER.model import Entity, Person, User
from BACKEND_NAME_PLACEHOLDER.schema import (EntityBase, EntityFilter,
                                             EntityFull, UserBase, UserFull)

log = get_logger()


class Crud:
    def __init__(self, engine: Engine):
        self._engine: Engine = engine

    def get_users(self, filter: str | None = None) -> list[UserFull]:
        assert f"FIXXXME {filter} not yet used"
        with Session(bind=self._engine) as session:
            full_users: list[UserFull] = []
            stmt = select(User)
            for orm_user in session.execute(stmt).scalars().all():
                full_users.append(
                    UserFull(
                        id=orm_user.entity_id,
                        name=orm_user.entity.name,
                        user_name=orm_user.user_name,
                        password_hash=orm_user.password_hash,
                    )
                )
            return full_users

    def get_persons(self, filter: str | None = None) -> list[Person]:
        if not filter:
            return []
        return []

    def delete_entity(self, id: int) -> None:
        with Session(bind=self._engine) as session:
            stmt = delete(Entity).where(Entity.id.is_(id))
            result = session.execute(stmt)
            log.error(f"Result Type is: {type(result)}")
            if (
                not result.rowcount  # pyright: ignore[reportUnknownMemberType,reportAttributeAccessIssue]
            ):
                raise AttributeError(f"Entity id=={id} does not exist!")
            session.commit()

    def get_entities(self, filter: EntityFilter | None = None) -> list[EntityFull]:
        with Session(bind=self._engine) as session:
            full_entities: list[EntityFull] = []
            stmt = select(Entity)
            if filter and filter.name:
                stmt = stmt.filter(Entity.name.like(filter.name))
            if filter and filter.id:
                stmt = stmt.filter(Entity.id.is_(filter.id))
            for orm_entity in session.execute(stmt).scalars().all():
                full_entities.append(EntityFull(id=orm_entity.id, name=orm_entity.name))
            return full_entities

    def create_entity(self, new_entity: EntityBase) -> EntityFull:
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
                id=user.entity_id,
            )
            return user_full

    def _create_entity(self, session: Session, new_entity: EntityBase) -> Entity:
        entity = Entity(name=new_entity.name)
        session.add(entity)
        return entity
