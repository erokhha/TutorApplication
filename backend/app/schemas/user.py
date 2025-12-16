from enum import Enum
from pydantic import BaseModel, EmailStr


class UserRole(str, Enum):
    tutor = "tutor"
    student = "student"


class UserOut(BaseModel):
    id: int
    email: EmailStr
    role: UserRole
