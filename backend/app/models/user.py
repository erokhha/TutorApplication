from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    phone: Mapped[str] = mapped_column(unique=True)
    role: Mapped[str]

    password_hash: Mapped[str | None] = mapped_column(nullable=True)
