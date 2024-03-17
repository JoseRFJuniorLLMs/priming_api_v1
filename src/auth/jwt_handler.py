import time
import jwt
from decouple import config
from dotenv import load_dotenv
from os import getenv

load_dotenv()

JWT_SECRET_KEY = config('SECRET_JWT_KEY')
JWT_ALGORITHM = config('ALGORITHM_JWT')


def token_response(token: str):
    return {
        'access token': token
    }


def signJWT(userID: str):
    payload = {
        'userId': userID,
        'expiry': time.time() + 2592000
    }
    token = jwt.encode(payload, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
    return token_response(token)


def decodeJWT(token: str):
    if not token or not token.startswith("Bearer "):
        return None
    try:
        decode_token = jwt.decode(token, JWT_SECRET_KEY, algorithms=JWT_ALGORITHM)
        return decode_token if decode_token['exp'] >= time.time() else None
    except jwt.ExpiredSignatureError:
        raise "Token expirado"
    except jwt.InvalidTokenError:
        raise "Token inválido"

