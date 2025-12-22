from pydantic import BaseModel, ConfigDict
from datetime import datetime
from pydantic import BaseModel, ConfigDict
from datetime import datetime


class LessonForTutor(BaseModel):
    id: int
    subject: str
    grade: int
    start_time: datetime
    end_time: datetime
    price: float
    status: str

    student_name: str

    model_config = ConfigDict(from_attributes=True)


class LessonForStudent(BaseModel):
    id: int
    subject: str
    grade: int
    start_time: datetime
    end_time: datetime
    price: float
    status: str

    tutor_name: str

    model_config = ConfigDict(from_attributes=True)



class LessonListItem(BaseModel):
    id: int
    subject: str
    grade: int
    start_time: datetime
    end_time: datetime
    price: float
    status: str

    student_name: str
    tutor_name: str

    model_config = ConfigDict(from_attributes=True)

class LessonCreate(BaseModel):
    relation_id: int
    subject: str
    grade: int
    start_time: datetime
    end_time: datetime
    price: float

class LessonItem(BaseModel):
    id: int
    subject: str
    grade: int
    start_time: datetime
    end_time: datetime
    price: float
    status: str

    student_name: str
    tutor_name: str

    model_config = ConfigDict(from_attributes=True)
# app/schemas/lesson.py

class LessonCreated(BaseModel):
    id: int
    subject: str
    grade: int
    start_time: datetime
    end_time: datetime
    price: float
    status: str

    model_config = ConfigDict(from_attributes=True)
class LessonCalendarItem(BaseModel):
    id: int
    subject: str
    grade: int
    start_time: datetime
    end_time: datetime
    price: float
    status: str

    student_name: str
    tutor_name: str

    model_config = ConfigDict(from_attributes=True)