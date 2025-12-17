from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.schemas.auth import TutorRegisterRequest
from app.models.user import User
from app.models.user_contacts import UserContacts
from app.models.tutor import Tutor
from app.core.security import hash_password

from app.models.user import User
from app.models.user_contacts import UserContacts
from app.models.student import Student
from app.models.student_tutor import StudentTutor
from app.models.tutor import Tutor


async def register_tutor(
    data: TutorRegisterRequest,
    db: AsyncSession
):
    # 1. Проверка: ИНН уже зарегистрирован?
    result = await db.execute(
        select(Tutor).where(Tutor.inn == data.inn)
    )
    if result.scalar_one_or_none():
        raise ValueError("Репетитор с таким ИНН уже зарегистрирован")

    # 2. Создаём пользователя
    user = User(
        role="tutor",
        password_hash=hash_password(data.password)
    )
    db.add(user)
    await db.flush()  # получаем user.id

    # 3. Контакты пользователя
    contacts = UserContacts(
        user_id=user.id,
        full_name=data.full_name,
        phone=data.phone,
        email=data.email
    )
    db.add(contacts)

    # 4. Репетитор
    tutor = Tutor(
        inn=data.inn,
        user_id=user.id,
        fns_password_hash=hash_password(data.fns_password),
        self_employed=True
    )
    db.add(tutor)

    # 5. Сохраняем всё
    await db.commit()

    return {
        "status": "ok",
        "user_id": user.id,
        "inn": tutor.inn
    }

async def register_student(data, db):
    # 1. Проверяем, что репетитор существует
    tutor = await db.scalar(
        select(Tutor).where(Tutor.inn == data.tutor_inn)
    )
    if not tutor:
        raise ValueError("Репетитор с таким ИНН не найден")

    # 2. User
    user = User(role="student", password_hash=None)
    db.add(user)
    await db.flush()

    # 3. Контакты
    contacts = UserContacts(
        user_id=user.id,
        full_name=data.full_name,
        phone=data.phone,
        email=None,
    )
    db.add(contacts)

    # 4. Student
    student = Student(
        user_id=user.id,
        grade=data.grade,
        parent_phone=None,
    )
    db.add(student)
    await db.flush()

    # 5. Связь ученик–репетитор
    relation = StudentTutor(
        student_id=student.id,
        tutor_inn=data.tutor_inn,
    )
    db.add(relation)

    await db.commit()

    return {
        "status": "ok",
        "student_id": student.id,
        "tutor_inn": data.tutor_inn,
    }