from fastapi import APIRouter, HTTPException, Depends, status
from datetime import timedelta

from starlette.requests import Request
from starlette.responses import RedirectResponse

from src.Model.Login import Login
from src.Service.LoginService import LoginService
from src.Handler.GoogleHandler import GoogleHandler

app = APIRouter()


@app.post("/login")
async def login(login_data: Login, request: Request):
    user = await LoginService.login(login_data)

    if user:
        access_token_expires = timedelta(days=LoginService().ACCESS_TOKEN_EXPIRE_DAYS)
        access_token = LoginService().create_access_token(data={"sub": login_data.username},
                                                          expires_delta=access_token_expires)
        request.session["Authorization"] = access_token
        return {"access_token": access_token, "token_type": "bearer"}

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )


@app.get("/logout")
async def logout(request: Request):
    return await LoginService.logout(request=request)


@app.get("/auth")
async def start_google_auth(request: Request):
    authorization_url, state = GoogleHandler.FLOW.authorization_url()
    request.session["state"] = state
    return RedirectResponse(authorization_url)


@app.get("/callback")
async def google_auth_callback(request: Request, state: str, code: str):
    if state != request.session.get("state"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid state",
        )

    GoogleHandler.FLOW.fetch_token(code=code)
    credentials = GoogleHandler.FLOW.credentials

    request.session["token"] = credentials.to_json()

    return {"message": "Authentication successful"}


@app.get("/")
async def index():
    return {"message": "hello world"}
