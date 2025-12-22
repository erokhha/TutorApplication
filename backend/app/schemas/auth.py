from pydantic import BaseModel, EmailStr, Field



# REGISTRATION


class TutorRegisterRequest(BaseModel):
    full_name: str = Field(min_length=3)
    phone: str = Field(min_length=10)
    email: EmailStr
    password: str = Field(min_length=6)
    inn: str = Field(min_length=10, max_length=12)
    fns_password: str = Field(min_length=6)


class StudentRegisterRequest(BaseModel):
    full_name: str = Field(min_length=3)
    phone: str = Field(min_length=10)
    password: str = Field(min_length=6)
    grade: int
    tutor_inn: str



# LOGIN

class TutorLoginRequest(BaseModel):
    phone: str = Field(min_length=10)
    password: str = Field(min_length=6)


class StudentLoginRequest(BaseModel):
    phone: str = Field(min_length=10)
    password: str = Field(min_length=6)


class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user_id: int
    role: str
