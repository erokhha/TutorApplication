from fastapi import FastAPI
from app.api import auth, lessons, tutor, student, wallet, stats, users


app = FastAPI(
    title="Tutor Backend",
    version="0.1.0"
)


@app.get("/health")
def health_check():
    return {"status": "ok"}


# подключаем роутеры
app.include_router(auth.router)
app.include_router(lessons.router)
app.include_router(tutor.router)
app.include_router(student.router)
app.include_router(wallet.router)
app.include_router(stats.router)
app.include_router(users.router)


