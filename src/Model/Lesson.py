
from datetime import datetime
from typing import Optional, List
from beanie import Document
from bson import ObjectId

from typing import Optional
from beanie import Document

from src.Model.Course import Course



class Lesson(Document):
    id: Optional[int] = None
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

    youtubeUrl: str
    course: Course
    time: str

