from fastapi import APIRouter, Depends, Body, HTTPException
from src.auth.jwt_bearer import JWTBearer
from starlette import status

from src.service import course_servicer as service
from src.model import Course

api = APIRouter(prefix='/course')


@api.get('/{id}')
async def get_course(id: str):
    try:
        student = service.get_course_by_id(id)
        return student
    except:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Id não encontrado!')


@api.get('/')
async def get_courses(level: str | None = None, name: str | None = None):
    if name:
        return service.get_courses_by_param('name', name)
    if level:
        return service.get_courses_by_param('level', level)
    return service.get_course_list()


# @api.get('/{course_id}/lessons')
# async def get_lessons_by_course(course_id: str):
#     return service.get_course_by_id(course_id).lessons
# TODO: Fazer retornar os dados de lessons formatados!!!

@api.post('/', status_code=status.HTTP_204_NO_CONTENT)
async def create_course(course: Course = Body(...)):
    service.create_course(course)


@api.patch('/', status_code=status.HTTP_204_NO_CONTENT)
async def update_course(course: Course = Body(...)):
    service.update_course(course)


@api.delete('/{course_id}')
async def delete_course(course_id: str):
    service.delete_by_id(course_id)
