from fastapi import APIRouter
from starlette.requests import Request

from src.Service.LessonService import LessonService

app = APIRouter()


@app.get("/{course_id}", status_code=200)
async def lessons_by_course(course_id):
    lessons = LessonService.get_lessons_by_course(course_id)
    return lessons
