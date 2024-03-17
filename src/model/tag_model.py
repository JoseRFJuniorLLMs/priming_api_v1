from typing import Optional, List

from bson import ObjectId
from bson.errors import InvalidId
from pydantic import Field, validator

from src.model import MongoModel


class Tag(MongoModel):
    id: Optional[ObjectId] = Field(default=None)
    name: str = Field()
    description: str | None = Field(default=None)
    student_id: ObjectId = Field()

    @validator('id', 'student_id', pre=True)
    def convert_id_to_objectid(cls, v):
        if isinstance(v, str):
            try:
                return ObjectId(v)
            except InvalidId:
                raise ValueError("Not a valid ObjectId")
        return v
