from fastapi import APIRouter, Depends, HTTPException
from app.schemas.lesson import LessonCreate, LessonCreated
from app.services.lessons import create_lesson
from app.services.lessons import get_lessons
from app.schemas.lesson import LessonListItem
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import date

from app.db.session import get_db
from app.core.auth import get_current_user
from app.services.lessons import get_lessons_for_day

router = APIRouter(
    prefix="/lessons",
    tags=["Lessons"],
)


@router.post("", response_model=LessonCreated)
async def create_lesson_endpoint(
    data: LessonCreate,
    db: AsyncSession = Depends(get_db),
    user: dict = Depends(get_current_user),
):
    try:
        return await create_lesson(
            data=data,
            user=user,
            db=db,
        )
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )


@router.get("", response_model=list[LessonListItem])
async def list_lessons_endpoint(
    db: AsyncSession = Depends(get_db),
    user: dict = Depends(get_current_user),
):
    return await get_lessons(user=user, db=db)



router = APIRouter(
    prefix="/calendar",
    tags=["Calendar"],
)


@router.get("/day")
async def calendar_day(
    date: date,
    db: AsyncSession = Depends(get_db),
    user: dict = Depends(get_current_user),
):
    return await get_lessons_for_day(
        day=date,
        user=user,
        db=db,
    )
