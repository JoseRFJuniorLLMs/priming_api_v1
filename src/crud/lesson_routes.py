from fastapi import APIRouter, Body, Depends
from starlette import status

from src.auth.jwt_bearer import JWTBearer
from src.service import lesson_servicer as service
from src.model import Lesson


api = APIRouter(prefix='/lesson')


@api.get('/{name}')
async def get_lesson(name: str):
    student = service.get_lesson_by_name(name)
    return student


@api.get('/')
async def get_lessons():
    courses = service.get_lesson_list()
    return courses


@api.post('/', status_code=status.HTTP_201_CREATED, dependencies=[Depends(JWTBearer())])
async def create_lesson(lesson: Lesson = Body(...)):
    service.create_lesson(lesson)


@api.patch('/', dependencies=[Depends(JWTBearer())])
async def update_lesson(lesson: Lesson = Body(...)):
    service.update_lesson(lesson)


