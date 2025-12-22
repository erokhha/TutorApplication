from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.core.auth import get_current_user
from app.schemas.relation import RelationItem
from app.services.relations import get_relations

router = APIRouter(
    prefix="/relations",
    tags=["Relations"],
)


@router.get("", response_model=list[RelationItem])
async def relations_list(
    db: AsyncSession = Depends(get_db),
    user: dict = Depends(get_current_user),
):
    return await get_relations(user=user, db=db)
