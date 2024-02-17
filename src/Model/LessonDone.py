import datetime
import time

from beanie import Document
from bson import ObjectId
from typing import List, Optional

from src.Model.StatusLesson import StatusLesson


class LessonDone(Document):
    id: Optional[int] = None
    start: time
    end: time
    status_lesson: StatusLesson = StatusLesson.PENDING
    lesson: [ObjectId]

    class Settings:
        name = "LessonDoneCollection"

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: dict
        }
