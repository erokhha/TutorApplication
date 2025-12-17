# app/models/student.py
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    parent_phone: Mapped[str | None] = mapped_column(
        String,
        nullable=True
    )
    grade: Mapped[int] = mapped_column(nullable=False)

    user = relationship("User")
