from datetime import timedelta, datetime
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

from src.Model.StatusOnline import StatusOnline
from src.Model.Status import Status
from src.Model.Student import Student
from src.Service.StudentService import StudentService


class LoginService:
    ACCESS_TOKEN_EXPIRE_DAYS = 30
    SECRET_KEY = "your-secret-key"
    ALGORITHM = "HS256"

    # Função para criar um token JWT
    def create_access_token(self, data: dict, expires_delta: timedelta):
        to_encode = data.copy()
        expire = datetime.utcnow() + expires_delta
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)
        return encoded_jwt

    @staticmethod
    async def login(login_data):
        student = StudentRepository().validate_login(login_data.username, login_data.password)

        if not student:
            raise HTTPException(status_code=401, detail="Invalid credentials")

        return student

    @staticmethod
    async def get_current_user(token: str = Depends(OAuth2PasswordBearer(tokenUrl="login"))):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, LoginService().SECRET_KEY, algorithms=[LoginService().ALGORITHM])
            if payload is None:
                raise credentials_exception
        except JWTError:
            raise credentials_exception

        username = payload["sub"]
        student = await StudentService.get_student_by_login(username)

        if not student:
            raise credentials_exception

        return student

    def validate_login_or_google(func):
        @wraps(func)
        async def wrapper(request: Request, *args, **kwargs):
            # Check for login token
            if "Authorization" in request.headers:
                token = request.headers["Authorization"].split(" ")[1]
                try:
                    await LoginService().get_current_user(token)
                except Exception:
                    raise HTTPException(
                        status_code=status.HTTP_401_UNAUTHORIZED,
                        detail="Invalid login token",
                    )

            # Check for Google token
            elif request.session:
                try:
                    GoogleHandler.verify_token(request.session)
                except Exception:
                    raise HTTPException(
                        status_code=status.HTTP_401_UNAUTHORIZED,
                        detail="Invalid Google authentication token",
                    )

            # If no token is provided, raise an error
            else:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="No authentication token provided",
                )

            return await func(request, *args, **kwargs)  # Ajuste aqui

        return wrapper
