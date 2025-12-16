from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base


class Tutor(Base):
    __tablename__ = "tutors"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    email: Mapped[str]
    inn_hash: Mapped[str] = mapped_column(unique=True)
    tax_password_hash: Mapped[str]

    balance: Mapped[int] = mapped_column(default=0)

    user = relationship("User")
