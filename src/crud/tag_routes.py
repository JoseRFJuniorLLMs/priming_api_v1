from fastapi import APIRouter, Depends, Body
from starlette import status

from src.auth.jwt_bearer import JWTBearer
from src.service import tag_servicer as service
from src.model import Tag

api = APIRouter(prefix='/tag')


@api.get('/{tag_id}', dependencies=[Depends(JWTBearer())])
async def get_tag_by_id(tag_id):
    return service.get_tag_by_id(tag_id)


@api.get('/', dependencies=[Depends(JWTBearer())])
async def get_tag_by_student(student_id: str = None):
    return service.get_tag_by_student(student_id)


@api.post('/', status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(JWTBearer())])
async def create_tag(tag: Tag = Body(...)):
    service.create_tag(tag)


@api.patch('/', status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(JWTBearer())])
async def update_tag(tag: Tag = Body(...)):
    service.update_tag(tag)


@api.delete('/{tag_id}', status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(JWTBearer())])
async def delete_tag(tag_id: str):
    service.delete_by_id(tag_id)
