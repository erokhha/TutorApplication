from app.schemas.slot import SlotCreate, SlotItem
from app.services.slots import create_slots
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.core.auth import get_current_user
from app.services.slots import book_slot

router = APIRouter(
    prefix="/slots",
    tags=["Slots"],
)


@router.post("", response_model=list[SlotItem])
async def create_slot_endpoint(
    data: SlotCreate,
    db: AsyncSession = Depends(get_db),
    user=Depends(get_current_user),
):
    try:
        return await create_slots(
            data=data,
            user=user,
            db=db,
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
router = APIRouter(
    prefix="/slots",
    tags=["Slots"],
)


@router.post("/{slot_id}/book")
async def book_slot_endpoint(
    slot_id: int,
    db: AsyncSession = Depends(get_db),
    user: dict = Depends(get_current_user),
):
    try:
        return await book_slot(
            slot_id=slot_id,
            user=user,
            db=db,
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))