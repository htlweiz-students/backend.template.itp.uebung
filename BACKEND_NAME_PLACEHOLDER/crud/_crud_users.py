from sqlalchemy import select
from sqlalchemy.orm import Session

from ..model import User
from ..schema import EntityBase, UserBase, UserFull
from ._crud_entity import CrudEntity


"""
CrudUsers - CRUD operations for User entities.

This module provides methods for creating, retrieving, updating, and deleting User objects in a
database. The User objects are related to EntityBase objects through the CrudEntity class.
"""
class CrudUsers(CrudEntity):

    def create_user(self, new_user: UserBase) -> UserFull:
        """
        Creates a new UserFull object in the database by saving a new User object and associating it with an EntityBase.
        
        Args:
            new_user (UserBase): The new user to be created, containing user_name, password_hash, and name attributes.
        
        Returns:
            UserFull: A new UserFull object representing the newly created user, including user_name, name, password_hash, and id.
        """
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
        """
        Fetches a list of UserFull objects from the database. If a filter is provided, it filters
        the users based on the provided string in their user_name or name fields.

        Args:
            filter (str | None, optional): A string that can be used to filter users by user_name
                                           or name. Defaults to None which means no filtering.

        Returns:
            list[UserFull]: A list of UserFull objects representing the fetched users.
        """
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


