from pydantic import BaseModel, Field, model_validator
from typing import Optional



# Регистрация репетитора

class TutorRegisterIn(BaseModel):
    first_name: str = Field(..., min_length=1)
    last_name: str = Field(..., min_length=1)
    phone: str = Field(..., min_length=10)
    email: Optional[str] = None

    password: str = Field(..., min_length=6)
    password_confirm: str = Field(..., min_length=6)

    @model_validator(mode="after")
    def passwords_match(self):
        if self.password != self.password_confirm:
            raise ValueError("Passwords do not match")
        return self



# Доп. регистрация репетитора

class TutorExtraRegisterIn(BaseModel):
    inn: str = Field(..., min_length=10)
    tax_password: str = Field(..., min_length=4)



# Регистрация ученика

class StudentRegisterIn(BaseModel):
    first_name: str = Field(..., min_length=1)
    last_name: str = Field(..., min_length=1)
    phone: str = Field(..., min_length=10)

    grade: str = Field(..., min_length=1)
    tutor_inn: str = Field(..., min_length=10)



# Логин (только репетитор)

class LoginIn(BaseModel):
    phone: str = Field(..., min_length=10)
    password: str = Field(..., min_length=6)



class AuthOut(BaseModel):
    access_token: str
    token_type: str = "bearer"

