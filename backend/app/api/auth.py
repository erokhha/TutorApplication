from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, HTTPException

from app.db.session import get_db
from app.models.user import User
from app.models.tutor import Tutor
from app.core.security import hash_value
from app.schemas.auth import TutorRegisterIn, AuthOut


@router.post("/register/tutor", response_model=AuthOut)
async def register_tutor(
    data: TutorRegisterIn,
    db: AsyncSession = Depends(get_db),
):
    # проверка телефона
    existing_user = await db.scalar(
        User.__table__.select().where(User.phone == data.phone)
    )
    if existing_user:
        raise HTTPException(400, "Пользователь с таким телефоном уже существует")

    user = User(
        first_name=data.first_name,
        last_name=data.last_name,
        phone=data.phone,
        role="tutor",
        password_hash=hash_value(data.password),
    )
    db.add(user)
    await db.flush()  # получаем user.id

    tutor = Tutor(
        user_id=user.id,
        email=data.email,
        inn_hash=hash_value(data.inn),
        tax_password_hash=hash_value(data.tax_password),
    )
    db.add(tutor)

    await db.commit()

    return {
        "access_token": f"fake-token-user-{user.id}",
        "token_type": "bearer",
    }
