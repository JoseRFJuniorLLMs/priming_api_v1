from fastapi import APIRouter, HTTPException, Depends, status
from datetime import timedelta

from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import RedirectResponse

from src.Model.Login import Login
from src.Service.LoginService import LoginService
from src.Handler.GoogleHandler import GoogleHandler

# Create APIRouter instance
router = APIRouter()

# Configure CORS middleware
origins = ["*"]
router.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Define route handlers
@router.post("/login")
async def login(login_data: Login, request: Request):
    # Authenticate user
    user = await LoginService.login(login_data)
    if user:
        # Generate access token
        access_token_expires = timedelta(days=LoginService().ACCESS_TOKEN_EXPIRE_DAYS)
        access_token = LoginService().create_access_token(data={"sub": login_data.username},
                                                          expires_delta=access_token_expires)
        return {"access_token": access_token, "token_type": "bearer"}
    else:
        # Unauthorized login
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

@router.get("/logout")
async def logout(request: Request):
    # Logout user
    return await LoginService.logout(request=request)

@router.get("/auth")
async def start_google_auth(request: Request):
    # Start Google OAuth authentication process
    authorization_url, state = GoogleHandler.FLOW.authorization_url()
    request.session["state"] = state
    return RedirectResponse(authorization_url)

@router.get("/callback")
async def google_auth_callback(request: Request, state: str, code: str):
    # Callback for Google OAuth authentication
    if state != request.session.get("state"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid state",
        )

    GoogleHandler.FLOW.fetch_token(code=code)
    credentials = GoogleHandler.FLOW.credentials

    request.session["token"] = credentials.to_json()

    return {"message": "Authentication successful"}

@router.get("/")
async def index():
    # Root route
    return {"message": "hello world"}
