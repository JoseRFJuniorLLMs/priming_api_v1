import datetime
from typing import Optional, List
from beanie import Document
from bson import ObjectId
from datetime import time  # Importe time do módulo datetime

class Lesson(Document):
    id: Optional[int] = None
    name: str
    prime: ObjectId = ObjectId()
    youtubeUrl: ObjectId = ObjectId()
    text: ObjectId = ObjectId()
    pharse: ObjectId = ObjectId()
    dictionary: ObjectId = ObjectId()
    list_word_text: List[ObjectId] = []
    start: time
    end: time
    status: str
    date: datetime
    duration_minutes: int
    course: ObjectIdField

    class Settings:
        name = "LessonCollection"
