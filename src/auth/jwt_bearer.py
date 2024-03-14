import time

from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jwt import ExpiredSignatureError, InvalidTokenError
import jwt
from decouple import config

from src.auth.jwt_handler import decodeJWT

JWT_SECRET_KEY = config('SECRET_JWT_KEY')
JWT_ALGORITHM = config('ALGORITHM_JWT')

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        credentials = await super().__call__(request)
        if credentials:
            if not credentials.scheme == 'Bearer':
                raise HTTPException(status_code=403, detail='Invalid token scheme. Use Bearer')
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=403, detail='Invalid token')
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail='Invalid token')

    def verify_jwt(self, token: str):
        try:
            payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
            expiry = payload.get('expiry', 0)
            if expiry >= time.time():
                return True
            else:
                return False
        except ExpiredSignatureError:
            raise HTTPException(status_code=403, detail='Token expired')
        except InvalidTokenError:
            raise HTTPException(status_code=403, detail='Invalid token')
