from fastapi import APIRouter, Depends, Body, HTTPException
from starlette import status

from src.auth.jwt_bearer import JWTBearer
from src.service import phrase_servicer as service
from src.model import Phrase

api = APIRouter(prefix='/phrase')


@api.get('/')
async def get_phrases(prime: str | None = None):
    if prime:
        return service.get_phrases_by_prime(prime)
    return service.get_phrase_list()


@api.get('/{id}')
async def get_phrase(id: str):
    try:
        phrase = service.get_phrase_by_id(id)
        return phrase
    except:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Id não encontrado!')


@api.post('/', status_code=status.HTTP_204_NO_CONTENT)
async def create_phrase(phrase: Phrase = Body(...)):
    service.create_phrase(phrase)


@api.patch('/', status_code=status.HTTP_204_NO_CONTENT)
async def update_phrase(phrase: Phrase = Body(...)):
    service.update_phrase(phrase)


@api.delete('/{phrase_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_phrase(phrase_id: str):
    try:
        service.delete_by_id(phrase_id)
    except:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Id não encontrado!')
