from datetime import datetime, timedelta

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.student_tutor import StudentTutor
from app.models.slot import Slot
from app.models.lesson import Lesson


async def check_slot_overlap(
    *,
    tutor_inn: str,
    start_time: datetime,
    end_time: datetime,
    db: AsyncSession,
) -> bool:
    stmt = (
        select(Slot)
        .join(StudentTutor, Slot.relation_id == StudentTutor.id)
        .where(
            StudentTutor.tutor_inn == tutor_inn,
            Slot.start_time < end_time,
            Slot.end_time > start_time,
        )
    )

    result = await db.execute(stmt)
    return result.scalars().first() is not None


async def check_lesson_overlap(
    *,
    tutor_inn: str,
    start_time: datetime,
    end_time: datetime,
    db: AsyncSession,
) -> bool:
    stmt = (
        select(Lesson)
        .join(StudentTutor, Lesson.relation_id == StudentTutor.id)
        .where(
            StudentTutor.tutor_inn == tutor_inn,
            Lesson.start_time < end_time,
            Lesson.end_time > start_time,
        )
    )

    result = await db.execute(stmt)
    return result.scalars().first() is not None



async def create_slots(
    *,
    data,
    user: dict,
    db: AsyncSession,
):

    if user["role"] != "tutor":
        raise ValueError("Только репетитор может создавать слоты")

    tutor_inn = user["inn"]


    result = await db.execute(
        select(StudentTutor).where(StudentTutor.tutor_inn == tutor_inn)
    )
    relations = result.scalars().all()

    if not relations:
        raise ValueError("У репетитора нет учеников")

    created_slots: list[Slot] = []

    current_start = data.start_time
    current_end = data.end_time

    while True:

        if await check_slot_overlap(
            tutor_inn=tutor_inn,
            start_time=current_start,
            end_time=current_end,
            db=db,
        ):
            raise ValueError("Слот пересекается с другим слотом")

        if await check_lesson_overlap(
            tutor_inn=tutor_inn,
            start_time=current_start,
            end_time=current_end,
            db=db,
        ):
            raise ValueError("Слот пересекается с занятием")


        for relation in relations:
            slot = Slot(
                relation_id=relation.id,
                start_time=current_start,
                end_time=current_end,
                recurrence=data.recurrence,
                repeat_until=data.repeat_until,
            )
            db.add(slot)
            created_slots.append(slot)


        if not data.recurrence:
            break


        if data.recurrence == "daily":
            delta = timedelta(days=1)
        elif data.recurrence == "weekly":
            delta = timedelta(weeks=1)
        else:
            break

        current_start += delta
        current_end += delta

        if data.repeat_until and current_start > data.repeat_until:
            break

    await db.commit()
    return created_slots



async def book_slot(
    *,
    slot_id: int,
    user: dict,
    db: AsyncSession,
):

    if user["role"] != "student":
        raise ValueError("Только ученик может бронировать слот")


    slot = await db.get(Slot, slot_id)
    if not slot:
        raise ValueError("Слот не найден")

    relation = slot.relation


    if relation.student_id != user["user_id"]:
        raise ValueError("Этот слот не принадлежит ученику")

    # 4️⃣ Создаём занятие
    lesson = Lesson(
        relation_id=relation.id,
        subject="Урок",
        grade=relation.student.grade,
        start_time=slot.start_time,
        end_time=slot.end_time,
        price=relation.tutor.default_price if hasattr(relation.tutor, "default_price") else 0,
        status="unpaid",
    )

    db.add(lesson)


    await db.delete(slot)

    await db.commit()
    await db.refresh(lesson)

    return {
        "status": "ok",
        "lesson_id": lesson.id,
    }
