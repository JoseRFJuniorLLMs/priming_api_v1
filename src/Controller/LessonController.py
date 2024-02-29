from fastapi import APIRouter

from src.Service.LessonService import LessonService

app = APIRouter()


@app.get("/")
async def lessons_by_course():
    return {"lessons": LessonService.get_lessons()}
