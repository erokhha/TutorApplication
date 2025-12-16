from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base


class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    student_class: Mapped[str] = mapped_column(String, nullable=False)
    tutor_inn: Mapped[str] = mapped_column(String, nullable=False)

    user = relationship("User")
