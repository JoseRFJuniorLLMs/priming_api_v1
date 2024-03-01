from datetime import datetime
from typing import Optional, List
from beanie import Document, PydanticObjectId
from bson import ObjectId


class Lesson(Document):
    _id: Optional[PydanticObjectId] = None
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
