from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.user import User
from app.models.user_contacts import UserContacts
from app.models.tutor import Tutor
from app.models.student import Student
from app.models.student_tutor import StudentTutor

from app.schemas.auth import (
    TutorRegisterRequest,
    StudentRegisterRequest,
    TutorLoginRequest,
    StudentLoginRequest,
    LoginResponse,
)

from app.core.security import (
    hash_password,
    hash_long_secret,
    verify_password,
    create_access_token,
)

# ==================================================
# REGISTRATION
# ==================================================

async def register_tutor(
    data: TutorRegisterRequest,
    db: AsyncSession,
):
    # Проверка ИНН
    exists = await db.scalar(
        select(Tutor).where(Tutor.inn == data.inn)
    )
    if exists:
        raise ValueError("Репетитор с таким ИНН уже зарегистрирован")

    # User
    user = User(
        role="tutor",
        password_hash=hash_password(data.password),
    )
    db.add(user)
    await db.flush()

    # Контакты
    contacts = UserContacts(
        user_id=user.id,
        full_name=data.full_name,
        phone=data.phone,
        email=data.email,
    )
    db.add(contacts)

    # Tutor
    tutor = Tutor(
        inn=data.inn,
        user_id=user.id,
        fns_password_hash=hash_long_secret(data.fns_password),
        self_employed=True,
    )
    db.add(tutor)

    await db.commit()

    return {
        "status": "ok",
        "user_id": user.id,
        "inn": tutor.inn,
    }


async def register_student(
    data: StudentRegisterRequest,
    db: AsyncSession,
):
    # Проверяем репетитора
    tutor = await db.scalar(
        select(Tutor).where(Tutor.inn == data.tutor_inn)
    )
    if not tutor:
        raise ValueError("Репетитор с таким ИНН не найден")

    # User
    user = User(
        role="student",
        password_hash=hash_password(data.password),
    )
    db.add(user)
    await db.flush()

    # Контакты
    contacts = UserContacts(
        user_id=user.id,
        full_name=data.full_name,
        phone=data.phone,
        email=None,
    )
    db.add(contacts)

    # Student
    student = Student(
        user_id=user.id,
        grade=data.grade,
        parent_phone=None,
    )
    db.add(student)
    await db.flush()

    # Связь student → tutor
    relation = StudentTutor(
        student_id=student.id,
        tutor_inn=data.tutor_inn,
    )
    db.add(relation)

    await db.commit()

    return {
        "status": "ok",
        "student_id": student.id,
    }


# ==================================================
# LOGIN
# ==================================================

async def login_tutor(
    data: TutorLoginRequest,
    db: AsyncSession,
) -> LoginResponse:

    user = await db.scalar(
        select(User)
        .join(UserContacts)
        .where(UserContacts.phone == data.phone)
        .where(User.role == "tutor")
    )

    if not user or not user.password_hash:
        raise ValueError("Неверный телефон или пароль")

    if not verify_password(data.password, user.password_hash):
        raise ValueError("Неверный телефон или пароль")

    token = create_access_token(
        user_id=user.id,
        role=user.role,
    )

    return {
        "access_token": token,
        "token_type": "bearer",
        "user_id": user.id,
        "role": user.role,
    }


async def login_student(
    data: StudentLoginRequest,
    db: AsyncSession,
) -> LoginResponse:

    user = await db.scalar(
        select(User)
        .join(UserContacts)
        .join(Student)
        .where(UserContacts.phone == data.phone)
        .where(User.role == "student")
    )

    if not user or not user.password_hash:
        raise ValueError("Неверный телефон или пароль")

    if not verify_password(data.password, user.password_hash):
        raise ValueError("Неверный телефон или пароль")

    token = create_access_token(
        user_id=user.id,
        role=user.role,
    )

    return {
        "access_token": token,
        "token_type": "bearer",
        "user_id": user.id,
        "role": user.role,
    }
