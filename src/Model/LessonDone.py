import datetime
import time

from beanie import Document, PydanticObjectId
from bson import ObjectId
from typing import List, Optional
from src.Model.StatusLesson import StatusLesson


class LessonDone(Document):
    _id: Optional[PydanticObjectId] = None
    start: time
    end: time
    status_lesson: StatusLesson = StatusLesson.PENDING
    lesson: [ObjectId]
    student: [ObjectId]

    class Settings:
        name = "LessonDoneCollection"

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: dict
        }
