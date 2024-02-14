from fastapi import FastAPI, Depends
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from src.Model.Student import Student
from src.Model.Login import Login
from src.Controller import LoginController, StudentController
from src.Service.LoginService import LoginService

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    client = AsyncIOMotorClient("mongodb+srv://junior:debian23@prime.0zjimdw.mongodb.net/?retryWrites=true&w=majority")
    await init_beanie(database=client['primeDB'], document_models=[Login, Student])


# Include student routes
app.include_router(StudentController.app, prefix="/student", tags=["students"],
                   dependencies=[Depends(LoginService.get_current_user)])

# Include login routes
app.include_router(LoginController.app, prefix="", tags=["login"])
