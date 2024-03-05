from fastapi import FastAPI
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware

from src.Model.Student import Student
from src.Model.Login import Login
from src.Model.Course import Course
from src.Controller import LoginController, StudentController, LessonController, CourseController, LessonDoneController

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,  # Se a sua API permite cookies
    allow_methods=["*"],  # Ajuste para os métodos permitidos (por exemplo, GET, POST, PUT, DELETE)
    allow_headers=["*"]  # Ajuste para os cabeçalhos permitidos (por exemplo, Content-Type, Authorization)
)

app.add_middleware(SessionMiddleware, secret_key="secret")


@app.on_event("startup")
async def startup_event():
    client = AsyncIOMotorClient("mongodb+srv://junior:debian23@prime.0zjimdw.mongodb.net/?retryWrites=true&w=majority")
    await init_beanie(database=client['primeDB'], document_models=[Login, Student, Course])


# Inclua as rotas dos alunos
app.include_router(StudentController.app, prefix="/student", tags=["students"])

# Inclua as rotas de login
app.include_router(LoginController.app, prefix="", tags=["login"])

# Inclua as rotas de lições
app.include_router(LessonController.app, prefix="/lesson", tags=["lessons"])

# Inclua as rotas para cursos
app.include_router(CourseController.app, prefix="/course", tags=["courses"])

# Inclua as rotas de lições concluídas
app.include_router(LessonDoneController.app, prefix="/lessonDone", tags=["lessonsDone"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
