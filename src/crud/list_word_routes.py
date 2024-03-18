from fastapi import APIRouter, Depends, Body, HTTPException
from starlette import status

from src.auth.jwt_bearer import JWTBearer
from src.service import list_word_servicer as service
from src.model import ListWord

api = APIRouter(prefix='/list-word')


@api.get('/{id}', dependencies=[Depends(JWTBearer())])
async def get_list_word(id: str):
    try:
        list_word = service.get_list_word_by_id(id)
        return list_word
    except:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id não encontrado!")


@api.get('/', dependencies=[Depends(JWTBearer())])
async def get_list_words(prime: str = None):
    if prime:
        return service.get_list_word_by_text_prime(prime)
    raise HTTPException(status_code=404, detail='Parâmetros inválidos!')


@api.post('/', status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(JWTBearer())])
async def create_list_word(list_word: ListWord = Body(...)):
    service.create_word_list(list_word)


@api.patch('/', status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(JWTBearer())])
async def update_list_word(list_word: ListWord = Body(...)):
    service.update_list_word(list_word)


@api.delete('/{list_word_id}', status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(JWTBearer())])
async def delete_list_word(list_word_id: str):
    service.delete_by_id(list_word_id)
