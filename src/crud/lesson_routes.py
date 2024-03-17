from fastapi import APIRouter, Body, Depends, HTTPException
from starlette import status

from src.auth.jwt_bearer import JWTBearer
from src.service import lesson_servicer as service
from src.model import Lesson


api = APIRouter(prefix='/lesson')


@api.get('/{id}', dependencies=[Depends(JWTBearer())])
async def get_lesson(id: str):
    student = service.get_lesson_by_id(id)
    return student


@api.get('/', dependencies=[Depends(JWTBearer())])
async def get_lessons(name: str | None = None):
    if name:
        return service.get_lesson_by_name(name)
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Parametros inválidos!')


@api.post('/', status_code=status.HTTP_201_CREATED, dependencies=[Depends(JWTBearer())])
async def create_lesson(lesson: Lesson = Body(...)):
    service.create_lesson(lesson)


@api.patch('/', dependencies=[Depends(JWTBearer())])
async def update_lesson(lesson: Lesson = Body(...)):
    service.update_lesson(lesson)


@api.delete('/{lesson_id}', status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(JWTBearer())])
async def delete_lesson(lesson_id: str):
    service.delete_by_id(lesson_id)
