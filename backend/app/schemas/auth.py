from pydantic import BaseModel, Field, EmailStr



# Регистрация репетитора

class TutorRegisterRequest(BaseModel):
    full_name: str = Field(
        ...,
        min_length=3,
        description="ФИО репетитора одной строкой"
    )
    phone: str = Field(
        ...,
        min_length=10,
        description="Номер телефона"
    )
    email: EmailStr = Field(
        ...,
        description="Почта репетитора"
    )
    password: str = Field(
        ...,
        min_length=6,
        description="Пароль для входа"
    )
    inn: str = Field(
        ...,
        min_length=10,
        max_length=12,
        description="ИНН репетитора (используется как код)"
    )
    fns_password: str = Field(
        ...,
        min_length=6,
        description="Пароль от ФНС"
    )



# Регистрация ученика

class StudentRegisterRequest(BaseModel):
    full_name: str = Field(min_length=3)
    phone: str = Field(min_length=10)
    grade: int = Field(ge=1, le=11)
    tutor_inn: str = Field(min_length=10, max_length=12)