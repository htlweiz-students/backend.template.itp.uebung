from sqlalchemy import Engine
from sqlalchemy.orm import Session

from backend.model import Entity, Person, Todo, User
from backend.schema import EntityBase


class Crud:
    def __init__(self, engine: Engine):
        self._engine: Engine = engine

    # --- existing stubs (kept for compatibility) ---

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

    def create_entity(self, new_entity: EntityBase):
        with Session(self._engine) as session:
            assert new_entity
            assert session

    # --- user operations ---

    def get_user(self, user_name: str) -> User | None:
        with Session(self._engine) as session:
            return session.get(User, user_name)

    def create_user(self, user_name: str, password_hash: str, name: str) -> User:
        with Session(self._engine) as session:
            entity = Entity()
            entity.name = name
            entity.type = "entities"
            session.add(entity)
            session.flush()

            user = User()
            user.user_name = user_name
            user.password_hash = password_hash
            user.entity_id = entity.id
            session.add(user)
            session.commit()
            session.refresh(user)
            return user

    # --- todo operations ---

    def get_todos(self, user_name: str) -> list[Todo]:
        with Session(self._engine) as session:
            return list(session.query(Todo).filter(Todo.user_name == user_name).all())

    def create_todo(self, user_name: str, title: str) -> Todo:
        with Session(self._engine) as session:
            todo = Todo()
            todo.title = title
            todo.done = False
            todo.user_name = user_name
            session.add(todo)
            session.commit()
            session.refresh(todo)
            return todo

    def update_todo(self, todo_id: int, done: bool) -> Todo | None:
        with Session(self._engine) as session:
            todo = session.get(Todo, todo_id)
            if not todo:
                return None
            todo.done = done
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
