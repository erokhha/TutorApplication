# app/db/init_db.py
import asyncio

from app.db.base import Base
from app.db.session import engine

# ВАЖНО: импортируем все модели
from app.models.user import User
from app.models.user_contacts import UserContacts
from app.models.student import Student
from app.models.tutor import Tutor
from app.models.student_tutor import StudentTutor
from app.models.lesson import Lesson
from app.models.payment import Payment
from app.models.receipt import Receipt


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


if __name__ == "__main__":
    asyncio.run(init_db())
