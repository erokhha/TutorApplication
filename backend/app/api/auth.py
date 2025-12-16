from fastapi import APIRouter, HTTPException
from app.schemas.auth import (
    TutorRegisterIn,
    TutorExtraRegisterIn,
    StudentRegisterIn,
    LoginIn,
    AuthOut,
)
from app.schemas.user import UserRole

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


# Регистрация репетитора (шаг 1)
@router.post("/register/tutor", response_model=AuthOut)
def register_tutor(data: TutorRegisterIn):
    # 🔹 тут позже будет создание User + TutorProfile
    # 🔹 сейчас делаем заглушку

    return {
        "access_token": "fake-token-for-tutor",
        "token_type": "bearer"
    }



# Доп. регистрация репетитора (шаг 2)

@router.post("/register/tutor/extra")
def register_tutor_extra(data: TutorExtraRegisterIn):
    # тут позже будет сохранение ИНН и пароля налоговой
    return {
        "status": "ok"
    }



# Регистрация ученика

@router.post("/register/student", response_model=AuthOut)
def register_student(data: StudentRegisterIn):
    # 🔹 тут позже будет:
    # - создание User (role=student)
    # - привязка к репетитору по tutor_inn

    return {
        "access_token": "fake-token-for-student",
        "token_type": "bearer"
    }



# Логин (только репетитор)

@router.post("/login", response_model=AuthOut)
def login(data: LoginIn):

    if data.phone.startswith("+700"):
        raise HTTPException(status_code=403, detail="Students do not have password login")

    return {
        "access_token": "fake-login-token",
        "token_type": "bearer"
    }
