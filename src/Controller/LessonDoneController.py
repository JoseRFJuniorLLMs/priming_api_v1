from fastapi import APIRouter, Depends
from starlette.middleware.cors import CORSMiddleware

from src.Service.LessonDoneService import LessonDoneService
from src.Service.LoginService import LoginService

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


@app.get("/student/{student_id}")
async def get_lesson_done_by_student(student_id, current_user: str = Depends(get_current_user)):
    data = LessonDoneService.get_lesson_done_by_student(student_id)
    for item in data:
        item["_id"] = str(item["_id"])
        for i in item['lesson_done_details']:
            i["lesson_id"] = str(i["lesson_id"])

    return data
