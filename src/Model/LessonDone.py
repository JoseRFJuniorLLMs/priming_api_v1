from typing import List, Optional
from beanie import Document


class LessonDone(Document):
    id: Optional[int] = None
    lesson: List[ObjectId] = []


class Settings:
    name = "LessonDoneCollection"


class Config:
    arbitrary_types_allowed = True
    json_encoders = {
        ObjectId: dict
    }