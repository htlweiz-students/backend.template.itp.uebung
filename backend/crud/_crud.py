from sqlalchemy import Engine, and_, or_, select
from sqlalchemy.orm import Session

from backend.model import Entity, Person, Todo, User
from backend.schema import (
    EntityBase,
    EntityFilter,
    EntityFull,
    UserBase,
    UserFilter,
    UserFull,
)


class Crud:
    def __init__(self, engine: Engine):
        self._engine: Engine = engine

    # --- entity operations ---

    def create_entity(self, new_entity: EntityBase) -> EntityFull:
        with Session(self._engine) as session:
            entity = Entity()
            entity.name = new_entity.name
            entity.type = "entities"
            session.add(entity)
            session.commit()
            session.refresh(entity)
            return EntityFull(id=entity.id, name=entity.name)

    def get_entities(
        self, filter: EntityFilter | None = None
    ) -> list[EntityFull]:
        with Session(self._engine) as session:
            stmt = select(Entity)
            if filter is not None:
                conditions = []
                if filter.name is not None:
                    conditions.append(Entity.name.like(filter.name))
                if filter.id is not None:
                    conditions.append(Entity.id == filter.id)
                if conditions:
                    stmt = stmt.where(and_(*conditions))
            entities = session.execute(stmt).scalars().all()
            return [EntityFull(id=e.id, name=e.name) for e in entities]

    def delete_entity(self, entity_id: int) -> None:
        with Session(self._engine) as session:
            db_entity = session.get(Entity, entity_id)
            if db_entity is None:
                raise AttributeError(f"No such Entity(id: {entity_id}, ...)!")
            session.delete(db_entity)
            session.commit()

    def change_entity(self, entity: EntityFull) -> EntityFull:
        with Session(self._engine) as session:
            db_entity = session.get(Entity, entity.id)
            if db_entity is None:
                raise AttributeError(f"No such Entity(id: {entity.id}, ...)!")
            db_entity.name = entity.name
            session.commit()
            return EntityFull(id=db_entity.id, name=db_entity.name)

    # --- user operations ---

    def create_user(
        self, user_base: UserBase, entity: EntityFull | None = None
    ) -> UserFull:
        with Session(self._engine) as session:
            if entity is not None:
                db_entity = session.get(Entity, entity.id)
                if db_entity is None:
                    raise AttributeError(
                        f"No such Entity(id: {entity.id}, ...)!"
                    )
                if user_base.name:
                    db_entity.name = user_base.name
                    session.flush()
            else:
                db_entity = Entity()
                db_entity.name = user_base.name
                db_entity.type = "entities"
                session.add(db_entity)
                session.flush()

            user = User()
            user.user_name = user_base.user_name
            user.password_hash = user_base.password_hash
            user.entity_id = db_entity.id
            session.add(user)
            session.commit()
            session.refresh(db_entity)
            return UserFull(
                id=db_entity.id,
                user_name=user.user_name,
                name=db_entity.name,
                password_hash=user.password_hash,
            )

    def get_users(
        self, filter: UserFilter | None = None
    ) -> list[UserFull]:
        with Session(self._engine) as session:
            stmt = select(User, Entity).join(
                Entity, User.entity_id == Entity.id
            )
            if filter is not None:
                conditions = []
                if filter.user_name is not None:
                    conditions.append(User.user_name.like(filter.user_name))
                if filter.name is not None:
                    conditions.append(Entity.name.like(filter.name))
                if filter.id is not None:
                    conditions.append(Entity.id == filter.id)
                if conditions:
                    clause = (
                        and_(*conditions)
                        if filter.use_and
                        else or_(*conditions)
                    )
                    stmt = stmt.where(clause)
            results = session.execute(stmt).all()
            return [
                UserFull(
                    id=entity.id,
                    user_name=user.user_name,
                    name=entity.name,
                    password_hash=user.password_hash,
                )
                for user, entity in results
            ]

    def delete_user(self, user_id: int) -> None:
        with Session(self._engine) as session:
            user = session.execute(
                select(User).where(User.entity_id == user_id)
            ).scalar_one_or_none()
            if user:
                session.delete(user)
                session.commit()

    def change_user(self, user: UserFull) -> UserFull | None:
        with Session(self._engine) as session:
            db_entity = session.get(Entity, user.id)
            if not db_entity:
                return None
            db_entity.name = user.name
            db_user = session.execute(
                select(User).where(User.entity_id == user.id)
            ).scalar_one_or_none()
            if not db_user:
                return None
            session.commit()
            return UserFull(
                id=db_entity.id,
                user_name=db_user.user_name,
                name=db_entity.name,
                password_hash=db_user.password_hash,
            )

    def get_user(self, user_name: str) -> User | None:
        with Session(self._engine) as session:
            return session.get(User, user_name)

    def get_persons(self, filter: str | None = None) -> list[Person]:
        if not filter:
            return []
        return []

    # --- todo operations ---

    def get_todos(self, user_name: str) -> list[Todo]:
        with Session(self._engine) as session:
            return list(
                session.query(Todo).filter(Todo.user_name == user_name).all()
            )

    def create_todo(self, title: str, user_name: str) -> Todo:
        with Session(self._engine) as session:
            todo = Todo()
            todo.title = title
            todo.done = False
            todo.user_name = user_name
            session.add(todo)
            session.commit()
            session.refresh(todo)
            return todo

    def update_todo(self, todo_id: int, title: str, done: bool) -> Todo | None:
        with Session(self._engine) as session:
            todo = session.get(Todo, todo_id)
            if not todo:
                return None
            todo.done = done
            todo.title = title
            session.commit()
            session.refresh(todo)
            return todo

    def delete_todo(self, todo_id: int) -> Todo | None:
        with Session(self._engine) as session:
            todo = session.get(Todo, todo_id)
            if not todo:
                return None
            session.delete(todo)
            session.commit()
            return todo
