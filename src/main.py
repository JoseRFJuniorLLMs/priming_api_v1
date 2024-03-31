from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.crud import (
    student_routes,
    course_routes,
    lesson_routes,
    user_routes,
    phrase_routes,
    note_routes,
    tag_routes,
    list_word_routes,
    files_routes)
from src.logger import config_log

app = FastAPI()
app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])

app.include_router(student_routes.api)
app.include_router(course_routes.api)
app.include_router(lesson_routes.api)
app.include_router(user_routes.api)
app.include_router(phrase_routes.api)
app.include_router(note_routes.api)
app.include_router(tag_routes.api)
app.include_router(list_word_routes.api)
app.include_router(files_routes.api)

config_log()
