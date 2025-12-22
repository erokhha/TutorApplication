from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.student_tutor import StudentTutor
from app.models.student import Student
from app.models.user_contacts import UserContacts
from app.models.tutor import Tutor


async def get_relations(
    user: dict,
    db: AsyncSession,
):
    role = user["role"]
    user_id = user["user_id"]

    if role == "tutor":
        tutor = await db.scalar(
            select(Tutor).where(Tutor.user_id == user_id)
        )
        if not tutor:
            return []

        rows = await db.execute(
            select(
                StudentTutor.id.label("relation_id"),
                Student.id.label("student_id"),
                UserContacts.full_name.label("student_name"),
                Student.grade.label("grade"),
                StudentTutor.tutor_inn.label("tutor_inn"),
            )
            .join(Student, Student.id == StudentTutor.student_id)
            .join(UserContacts, UserContacts.user_id == Student.user_id)
            .where(StudentTutor.tutor_inn == tutor.inn)
        )

        return rows.mappings().all()


    if role == "student":
        rows = await db.execute(
            select(
                StudentTutor.id.label("relation_id"),
                Student.id.label("student_id"),
                UserContacts.full_name.label("student_name"),
                Student.grade.label("grade"),
                StudentTutor.tutor_inn.label("tutor_inn"),
            )
            .join(Student, Student.id == StudentTutor.student_id)
            .join(UserContacts, UserContacts.user_id == Student.user_id)
            .where(Student.user_id == user_id)
        )

        return rows.mappings().all()

    return []
