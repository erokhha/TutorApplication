from datetime import date, datetime, timedelta
from datetime import date, timedelta
from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.lesson import Lesson
from app.models.student_tutor import StudentTutor
from app.models.student import Student
from app.models.user_contacts import UserContacts
from app.models.tutor import Tutor

async def get_lessons_for_day(
    *,
    day: date,
    tutor_user_id: int,
    db: AsyncSession,
):
    start_dt = datetime.combine(day, datetime.min.time())
    end_dt = start_dt + timedelta(days=1)

    stmt = (
        select(
            Lesson.id,
            Lesson.subject,
            Lesson.grade,
            Lesson.start_time,
            Lesson.end_time,
            Lesson.price,
            Lesson.status,
            UserContacts.full_name.label("student_name"),
            Tutor.inn.label("tutor_name"),  # временно, можно заменить
        )
        .join(StudentTutor, Lesson.relation_id == StudentTutor.id)
        .join(Student, StudentTutor.student_id == Student.id)
        .join(UserContacts, UserContacts.user_id == Student.user_id)
        .join(Tutor, Tutor.inn == StudentTutor.tutor_inn)
        .where(Lesson.start_time >= start_dt)
        .where(Lesson.start_time < end_dt)
    )

    result = await db.execute(stmt)
    return result.mappings().all()



async def get_week_calendar(
    *,
    start_date: date,
    user: dict,
    db: AsyncSession,
):
    end_date = start_date + timedelta(days=6)

    stmt = (
        select(Lesson)
        .join(StudentTutor)
        .join(Student)
        .join(UserContacts, UserContacts.user_id == Student.user_id)
        .join(Tutor, Tutor.inn == StudentTutor.tutor_inn)
        .where(
            and_(
                Lesson.start_time >= start_date,
                Lesson.start_time < end_date + timedelta(days=1),
            )
        )
    )

    # 🔐 разграничение ролей
    if user["role"] == "tutor":
        stmt = stmt.where(Tutor.user_id == user["user_id"])
    else:
        stmt = stmt.where(Student.user_id == user["user_id"])

    lessons = (await db.execute(stmt)).scalars().all()


    days = {}
    for lesson in lessons:
        day = lesson.start_time.date()
        days.setdefault(day, []).append(lesson)

    return {
        "start_date": start_date,
        "end_date": end_date,
        "days": [
            {
                "date": d,
                "lessons": lessons,
            }
            for d, lessons in sorted(days.items())
        ],
    }
