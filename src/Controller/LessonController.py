from fastapi import APIRouter
from starlette import status

from src.Service.LessonService import LessonService

app = APIRouter()


@app.get("/list", status_code=status.HTTP_501_NOT_IMPLEMENTED)
async def lessons_by_course():
    return
