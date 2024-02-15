from datetime import timedelta, datetime
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

from Model.Status import Status
from Model.Student import Student
from Service.StudentService import StudentService


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
        student = await Student.validate_login(login_data.username, login_data.password)
        if student.status == Status.INACTIVE:
            student.status = "ACTIVE"
            await student.save()
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

        # Aqui você pode fazer a lógica para buscar o usuário no banco de dados, por exemplo
        student = await StudentService.get_student_by_login(payload["sub"])
        return student.__str__()
