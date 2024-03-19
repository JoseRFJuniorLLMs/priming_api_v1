from fastapi import APIRouter, Body, Depends, HTTPException
from starlette import status

from src.auth.jwt_bearer import JWTBearer
from src.service import lesson_servicer as service
from src.model import Lesson


api = APIRouter(prefix='/lesson')


@api.get('/{id}')
async def get_lesson(id: str):
    try:
        student = service.get_lesson_by_id(id)
        return student
    except:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Id não encontrado!')


@api.get('/')
async def get_lessons(name: str | None = None):
    if name:
        return service.get_lesson_by_name(name)
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Parametros inválidos!')


@api.post('/', status_code=status.HTTP_201_CREATED)
async def create_lesson(lesson: Lesson = Body(...)):
    service.create_lesson(lesson)


@api.patch('/')
async def update_lesson(lesson: Lesson = Body(...)):
    service.update_lesson(lesson)


@api.delete('/{lesson_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_lesson(lesson_id: str):
    try:
        service.delete_by_id(lesson_id)
    except:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Id não encontrado!')
