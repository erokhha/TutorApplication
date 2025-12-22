from app.schemas.lesson import LessonCalendarItem
from app.services.calendar import get_lessons_for_day
from fastapi import APIRouter, Depends
from datetime import date
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.core.auth import get_current_user
from app.services.calendar import get_week_calendar
from app.schemas.calendar import CalendarWeek

router = APIRouter(
    prefix="/calendar",
    tags=["Calendar"],
)


@router.get("/day", response_model=list[LessonCalendarItem])
async def calendar_day(
    date: date,
    db: AsyncSession = Depends(get_db),
    user: dict = Depends(get_current_user),
):
    return await get_lessons_for_day(
        day=date,
        tutor_user_id=user["user_id"],
        db=db,
    )

router = APIRouter(
    prefix="/calendar",
    tags=["Calendar"],
)


@router.get("/week", response_model=CalendarWeek)
async def calendar_week(
    start_date: date,
    db: AsyncSession = Depends(get_db),
    user=Depends(get_current_user),
):
    return await get_week_calendar(
        start_date=start_date,
        user=user,
        db=db,
    )