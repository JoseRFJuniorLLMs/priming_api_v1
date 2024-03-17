from fastapi import APIRouter, Depends, Body
from starlette import status

from src.auth.jwt_bearer import JWTBearer
from src.service import phrase_servicer as service
from src.model import Phrase

api = APIRouter(prefix='/phrase')


@api.get('/', dependencies=[Depends(JWTBearer())])
async def get_phrases(prime: str | None = None):
    if prime:
        return service.get_phrases_by_prime(prime)
    return service.get_phrase_list()


@api.get('/{id}', dependencies=[Depends(JWTBearer())])
async def get_phrase(id: str):
    phrase = service.get_phrase_by_id(id)
    return phrase


@api.post('/', status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(JWTBearer())])
async def create_phrase(phrase: Phrase = Body(...)):
    service.create_phrase(phrase)


@api.patch('/', status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(JWTBearer())])
async def update_phrase(phrase: Phrase = Body(...)):
    service.update_phrase(phrase)


@api.delete('/{phrase_id}', status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(JWTBearer())])
async def delete_phrase(phrase_id: str):
    service.delete_by_id(phrase_id)
