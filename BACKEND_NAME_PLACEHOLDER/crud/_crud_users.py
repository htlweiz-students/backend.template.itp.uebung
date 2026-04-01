from sqlalchemy import select
from sqlalchemy.orm import Session

from ..model import User
from ..schema import EntityBase, UserBase, UserFull
from ._crud_entity import CrudEntity


class CrudUsers(CrudEntity):

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
