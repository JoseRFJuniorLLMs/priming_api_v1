from typing import Optional, List

from bson import ObjectId
from bson.errors import InvalidId
from pydantic import Field, validator

from src.model import MongoModel


class Note(MongoModel):
    id: Optional[ObjectId] = Field(default=None)
    title: str = Field()
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)
    description: str | None = Field(default=None)
    student_id: ObjectId = Field()
    tags: List[ObjectId] | None = Field(default=None)

    @validator('tags', pre=True)
    def foreach_list(cls, v):
        if isinstance(v, list):
            a = []
            for i in v:
                a.append(ObjectId(i))
            return a

    @validator('id', 'student_id', pre=True)
    def convert_id_to_objectid(cls, v):
        if isinstance(v, str):
            try:
                return ObjectId(v)
            except InvalidId:
                raise ValueError("Not a valid ObjectId")
        return v


