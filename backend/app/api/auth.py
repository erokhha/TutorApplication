from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.schemas.auth import TutorRegisterRequest
from app.services.auth import register_tutor
from app.schemas.auth import StudentRegisterRequest
from app.services.auth import register_student

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register/tutor", status_code=status.HTTP_201_CREATED)
async def register_tutor_endpoint(
    data: TutorRegisterRequest,
    db: AsyncSession = Depends(get_db)
):
    try:
        return await register_tutor(data, db)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
@router.post("/register/student", status_code=201)
async def register_student_endpoint(
    data: StudentRegisterRequest,
    db: AsyncSession = Depends(get_db),
):
    return await register_student(data, db)
