from typing import override

from sqlalchemy import Boolean, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from ._base import Base
from ._user import User


class Todo(Base):
    __tablename__: str = "todos"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(255))
    done: Mapped[bool] = mapped_column(Boolean, default=False)
    user_name: Mapped[str] = mapped_column(ForeignKey(column=User.user_name))

    @override
    def __repr__(self) -> str:
        return f"Todo(id={self.id}, title='{self.title}', done={self.done}, user_name='{self.user_name}')"
