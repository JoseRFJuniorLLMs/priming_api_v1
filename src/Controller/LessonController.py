from fastapi import APIRouter, Depends
from starlette.middleware.cors import CORSMiddleware

from src.Service.LoginService import LoginService

from src.Service.LessonService import LessonService

app = APIRouter()

origins = ["http://localhost:4200"];

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,  # If your API allows cookies
    allow_methods=["*"],  # Adjust for allowed methods (e.g., GET, POST, PUT, DELETE)
    allow_headers=["*"])  # Adjust for allowed headers (e.g., Content-Type, Authorization)

def get_current_user(token: str = Depends(LoginService().oauth2_scheme)):
    return LoginService().get_current_user(token)


@app.get("/course/{course_id}", status_code=200)
async def lessons_by_course(course_id, current_user: str = Depends(get_current_user)):
    lessons = await LessonService.get_lessons_by_course(course_id)
    for lesson in lessons:
        lesson["lesson_id"] = str(lesson["lesson_id"])

    return lessons


@app.get("/{lesson_id}", status_code=200)
async def lesson_by_id(lesson_id, current_user: str = Depends(get_current_user)):
    lessons = await LessonService.get_lesson_by_id(lesson_id)
    for lesson in lessons:
        lesson["lesson_id"] = str(lesson["lesson_id"])

    return lessons
