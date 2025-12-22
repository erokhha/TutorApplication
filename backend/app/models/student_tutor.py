# app/models/student_tutor.py
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class StudentTutor(Base):
    __tablename__ = "student_tutor"

    id: Mapped[int] = mapped_column(primary_key=True)

    student_id: Mapped[int] = mapped_column(
        ForeignKey("students.id"),
        nullable=False
    )
    tutor_inn: Mapped[str] = mapped_column(
        String,
        ForeignKey("tutors.inn"),
        nullable=False
    )

    student = relationship("Student")
    tutor = relationship("Tutor")
