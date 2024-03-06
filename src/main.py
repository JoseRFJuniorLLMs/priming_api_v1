from fastapi import FastAPI, Depends
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware

from src.Model.Student import Student
from src.Model.Login import Login
from src.Model.Course import Course
from src.Controller import LoginController, StudentController, LessonController, CourseController, LessonDoneController

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="secret")
app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])


@app.on_event("startup")
async def startup_event():
    client = AsyncIOMotorClient("mongodb+srv://junior:debian23@prime.0zjimdw.mongodb.net/?retryWrites=true&w=majority")
    await init_beanie(database=client['primeDB'], document_models=[Login, Student, Course])


# Include student routes
app.include_router(StudentController.app, prefix="/student", tags=["students"])

# Include login routes
app.include_router(LoginController.app, prefix="", tags=["login"])

app.include_router(LessonController.app, prefix="/lesson", tags=["lessons"])

# Include your APIRouter for courses
app.include_router(CourseController.app, prefix="/course", tags=["courses"])

app.include_router(LessonDoneController.app, prefix="/lessonDone", tags=["lessonsDone"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
