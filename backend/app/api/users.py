from fastapi import APIRouter, Depends
from app.core.auth import get_current_user
from app.schemas.user import CurrentUserResponse

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/me", response_model=CurrentUserResponse)
async def me(user=Depends(get_current_user)):
    return {
        "user_id": user["user_id"],
        "role": user["role"],
    }
