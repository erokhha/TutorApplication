from pydantic import BaseModel
from datetime import date
from typing import List
from app.schemas.lesson import LessonItem


class CalendarDay(BaseModel):
    date: date
    lessons: List[LessonItem]


class CalendarWeek(BaseModel):
    start_date: date
    end_date: date
    days: List[CalendarDay]
