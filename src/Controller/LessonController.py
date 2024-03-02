from fastapi import APIRouter
from starlette.requests import Request

from src.Service.LessonService import LessonService

app = APIRouter()


@app.get("/course/{course_id}", status_code=200)
async def lessons_by_course(course_id):
    lessons = await LessonService.get_lessons_by_course(course_id)
    for lesson in lessons:
        lesson["lesson_id"] = str(lesson["lesson_id"])

    return lessons


@app.get("/{lesson_id}", status_code=200)
async def lesson_by_id(lesson_id):
    lessons = await LessonService.get_lesson_by_id(lesson_id)
    for lesson in lessons:
        lesson["lesson_id"] = str(lesson["lesson_id"])

    return lessons
