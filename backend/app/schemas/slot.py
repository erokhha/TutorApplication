from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class SlotCreate(BaseModel):
    start_time: datetime
    end_time: datetime

    recurrence: Optional[str] = None


    repeat_until: Optional[datetime] = None


class SlotItem(BaseModel):
    id: int
    start_time: datetime
    end_time: datetime
    status: str

    model_config = {
        "from_attributes": True
    }
