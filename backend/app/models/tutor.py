# app/models/tutor.py
from sqlalchemy import String, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Tutor(Base):
    __tablename__ = "tutors"

    inn: Mapped[str] = mapped_column(String, primary_key=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    fns_password_hash: Mapped[str] = mapped_column(String, nullable=False)
    self_employed: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    user = relationship("User")
