from fastapi import APIRouter
from app.schemas.user import UserOut, UserRole

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/me", response_model=UserOut)
def get_me():
    # временная заглушка, потом заменим на реальную авторизацию
    return {
        "id": 1,
        "email": "tutor@example.com",
        "role": UserRole.tutor
    }
