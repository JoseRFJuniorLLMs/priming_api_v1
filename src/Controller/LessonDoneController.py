from fastapi import APIRouter
from src.Service.LessonDoneService import LessonDoneService

app = APIRouter()


@app.get("/student/{student_id}")
async def get_lesson_done_by_student(student_id):
    data = LessonDoneService.get_lesson_done_by_student(student_id)
    for item in data:
        item["_id"] = str(item["_id"])
        for i in item['lesson_done_details']:
            print(i)
            i["lesson_id"] = str(i["lesson_id"])

    return data
