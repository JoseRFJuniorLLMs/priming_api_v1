from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from datetime import timedelta

from src.Model.Login import Login
from src.Service.LoginService import LoginService

app = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


@app.post("/login")
async def login(login_data: Login):
    user = await LoginService.login(login_data)

    if user:
        access_token_expires = timedelta(days=LoginService().ACCESS_TOKEN_EXPIRE_DAYS)
        access_token = LoginService().create_access_token(data={"sub": login_data.username},
                                                          expires_delta=access_token_expires)
        return {"access_token": access_token, "token_type": "bearer"}

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )


@app.post("/logout")
async def logout():
    # !Todo
    pass


@app.post("/auth")
async def login_with_google(token: str = Depends(oauth2_scheme)):
    # !Todo
    pass

