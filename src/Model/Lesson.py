from datetime import datetime
from typing import Optional, List
from beanie import Document, PydanticObjectId
from bson import ObjectId
from pydantic import Field


class Lesson(Document):

    _id: Optional[PydanticObjectId] = None
    lesson_id: Optional[str] = Field(alias="_id")

    name: str
    prime: ObjectId = ObjectId
    youtubeUrl: ObjectId = ObjectId
    text: ObjectId = ObjectId
    pharse: ObjectId = ObjectId
    dictionary: ObjectId = ObjectId
    list_word_text: List[ObjectId] = []
    start: datetime
    end: datetime
    status: str
    date: datetime
    duration_minutes: int
    course: [ObjectId]

    class Settings:
        name = "LessonCollection"
        arbitrary_types_allowed = True
        json_encoders = {
            PydanticObjectId: str
        }
        id_field = "lesson_id"