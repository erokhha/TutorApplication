from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.db.session import engine
from app.db.base import Base


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # shutdown (пока ничего не делаем)


app = FastAPI(lifespan=lifespan)
