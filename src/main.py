from fastapi import FastAPI

from src.crud import student_routes, course_routes, lesson_routes, user_routes, phrase_routes
from src.logger import config_log

app = FastAPI()
app.include_router(student_routes.api)
app.include_router(course_routes.api)
app.include_router(lesson_routes.api)
app.include_router(user_routes.api)
app.include_router(phrase_routes.api)

config_log()
