from typing import List, Optional

from bson import ObjectId
from bson.errors import InvalidId
from pydantic import Field, validator

from src.model.mongodb_model import MongoModel


class StatusLesson:
    DONE = 'Done'
    PENDING = 'Pending'


class LessonDone(MongoModel):
    id: Optional[ObjectId] = Field(None)
    start: str = Field()
    end: str = Field()
    status_lesson: str = Field()
    lesson: ObjectId = Field()
    student: ObjectId = Field()

    @validator('id', 'lesson', 'student', pre=True)
    def convert_id_to_objectid(cls, v):
        if isinstance(v, str):
            try:
                return ObjectId(v)
            except InvalidId:
                raise ValueError("Not a valid ObjectId")
        return v
