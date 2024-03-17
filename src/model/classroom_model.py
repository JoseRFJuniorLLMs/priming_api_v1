from typing import List, Optional

from bson import ObjectId
from bson.errors import InvalidId
from pydantic import Field, validator

from src.model.mongodb_model import MongoModel


class Classroom(MongoModel):
    id: Optional[ObjectId] = Field(None)
    audioUrls: List[str] | None = Field(default=None)
    course: str = Field()
    imageUrls: List[str] | None = Field(default=None)
    module: str = Field()
    phrases: List[str] | None = Field(default=None)
    prime: str = Field(default=None)
    students: List[ObjectId] | None = Field(default=None)
    target: str | None = Field(default=None)
    text: str | None = Field(default=None)
    videoUrls: List[str] | None = Field(default=None)

    @validator('students', pre=True)
    def foreach_list(cls, v):
        if isinstance(v, list):
            a = []
            for i in v:
                a.append(ObjectId(i))
            return a

    @validator('id', 'studentId', pre=True, check_fields=False)
    def convert_id_to_objectid(cls, v):
        if isinstance(v, str):
            try:
                return ObjectId(v)
            except InvalidId:
                raise ValueError("Not a valid ObjectId")
        return v
