import datetime

from fastapi import APIRouter, Depends, Body, HTTPException
from bson import ObjectId
from starlette import status

from src.auth.jwt_bearer import JWTBearer
from src.service import note_servicer as service
from src.model import Note

api = APIRouter(prefix='/note')


@api.get('/{student_id}')
async def get_notes_by_student(student_id: str = None):
    return service.get_notes_by_student(student_id)


@api.get('/')
async def get_notes(title: str = None):
    if title:
        return service.get_note_by_title(title)
    return HTTPException(status_code=404, detail='Sem paramêtros válidos!')


@api.post('/', status_code=status.HTTP_204_NO_CONTENT)
async def create_note(note: Note = Body(...)):
    note.created_at = str(datetime.datetime.now())
    service.create_note(note)


@api.patch('/', status_code=status.HTTP_204_NO_CONTENT)
async def update_note(note: Note = Body(...)):
    note.updated_at = str(datetime.datetime.now())
    note.student_id = ObjectId(note.student_id)
    service.update_note(note)


@api.delete('/{note_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_note(note_id: str):
    service.delete_by_id(note_id)
