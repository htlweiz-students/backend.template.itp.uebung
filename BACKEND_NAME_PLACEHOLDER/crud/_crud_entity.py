from sqlalchemy import delete, select
from sqlalchemy.orm import Session

from ..config import get_logger
from ..model import Entity
from ..schema import EntityBase, EntityFilter, EntityFull
from ._crud_base import CrudBase

log = get_logger()


class CrudEntity(CrudBase):

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

    def _create_entity(self, session: Session, new_entity: EntityBase) -> Entity:
        entity = Entity(name=new_entity.name)
        session.add(entity)
        return entity
