# app/services/lessons.py
from app.schemas.lesson import LessonCreate
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from datetime import date, datetime, timedelta
from app.models.lesson import Lesson
from app.models.student_tutor import StudentTutor
from app.models.student import Student
from app.models.tutor import Tutor
from app.models.user_contacts import UserContacts


async def create_lesson(
    data: LessonCreate,
    user: dict,
    db: AsyncSession,
):

    relation = await db.scalar(
        select(StudentTutor).where(StudentTutor.id == data.relation_id)
    )
    if not relation:
        raise ValueError("Связь ученик–репетитор не найдена")


    lesson = Lesson(
        relation_id=data.relation_id,
        subject=data.subject,
        grade=data.grade,
        start_time=data.start_time,
        end_time=data.end_time,
        price=data.price,
        status="unpaid",
    )

    db.add(lesson)
    await db.commit()
    await db.refresh(lesson)

    return lesson


async def get_lessons(
    user: dict,
    db: AsyncSession,
):
    stmt = (
        select(
            Lesson,
            UserContacts.full_name.label("student_name"),
            UserContacts.full_name.label("tutor_name"),
        )
        .join(StudentTutor, Lesson.relation_id == StudentTutor.id)
        .join(Student, StudentTutor.student_id == Student.id)
        .join(Tutor, StudentTutor.tutor_inn == Tutor.inn)
        .join(UserContacts, UserContacts.user_id == Student.user_id)
    )


    if user["role"] == "student":
        stmt = stmt.where(Student.user_id == user["user_id"])
    elif user["role"] == "tutor":
        stmt = stmt.where(Tutor.user_id == user["user_id"])

    result = await db.execute(stmt)
    rows = result.all()

    lessons = []
    for lesson, student_name, tutor_name in rows:
        lessons.append({
            "id": lesson.id,
            "subject": lesson.subject,
            "grade": lesson.grade,
            "start_time": lesson.start_time,
            "end_time": lesson.end_time,
            "price": lesson.price,
            "status": lesson.status,
            "student_name": student_name,
            "tutor_name": tutor_name,
        })

    return lessons



async def get_lessons_for_day(
    day: date,
    user: dict,
    db,
):
    start_dt = datetime.combine(day, datetime.min.time())
    end_dt = start_dt + timedelta(days=1)

    stmt = (
        select(
            Lesson,
            StudentTutor,
            Student,
            Tutor,
        )
        .join(StudentTutor, Lesson.relation_id == StudentTutor.id)
        .join(Student, StudentTutor.student_id == Student.id)
        .join(Tutor, StudentTutor.tutor_inn == Tutor.inn)
        .where(Lesson.start_time >= start_dt)
        .where(Lesson.start_time < end_dt)
    )

    result = await db.execute(stmt)
    rows = result.all()

    lessons = []

    for lesson, relation, student, tutor in rows:
        if user["role"] == "tutor":
            lessons.append({
                "id": lesson.id,
                "subject": lesson.subject,
                "grade": lesson.grade,
                "start_time": lesson.start_time,
                "end_time": lesson.end_time,
                "price": lesson.price,
                "status": lesson.status,
                "student_name": student.user.contacts.full_name,
            })

        elif user["role"] == "student":
            lessons.append({
                "id": lesson.id,
                "subject": lesson.subject,
                "grade": lesson.grade,
                "start_time": lesson.start_time,
                "end_time": lesson.end_time,
                "price": lesson.price,
                "status": lesson.status,
                "tutor_name": tutor.user.contacts.full_name,
            })

    return lessons

