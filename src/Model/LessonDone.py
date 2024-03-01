import datetime
import time

from beanie import Document, PydanticObjectId
from bson import ObjectId
from typing import List, Optional

from pydantic import Field

from src.Model.StatusLesson import StatusLesson


class LessonDone(Document):

    _id: Optional[PydanticObjectId] = None
    lesson_done_id: Optional[str] = Field(alias="_id")

    start: time
    end: time
    status_lesson: StatusLesson = StatusLesson.PENDING
    lesson: [ObjectId]
    student: [ObjectId]

    class Settings:
        name = "LessonDoneCollection"
        arbitrary_types_allowed = True
        json_encoders = {
            PydanticObjectId: str
        }
        id_field = "lesson_done_id"