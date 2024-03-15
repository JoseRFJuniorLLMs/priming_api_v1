from fastapi import APIRouter, Depends, Body
from starlette import status

from src.auth.jwt_bearer import JWTBearer
from src.service import phrase_servicer as service

api = APIRouter(prefix='/phrase')


@api.get('/', dependencies=[Depends(JWTBearer())])
async def get_phrases():
    phrase = service.get_phrase_list()
    return phrase


@api.get('/{prime}', dependencies=[Depends(JWTBearer())])
async def get_phrase_prime(prime: str):
    phrases = service.get_phrases_by_prime(prime)
    return phrases
