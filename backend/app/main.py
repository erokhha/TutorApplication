from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.db.session import engine
from app.db.base import Base

from app.api import auth, users, lessons, relations
from app.api import calendar
from app.api import slots





@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield


app = FastAPI(lifespan=lifespan)

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(relations.router)
app.include_router(lessons.router)
app.include_router(calendar.router)


app.include_router(slots.router)


