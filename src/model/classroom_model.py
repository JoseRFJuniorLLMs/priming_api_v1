from typing import List, Optional

from bson import ObjectId
from bson.errors import InvalidId
from pydantic import Field, validator

from src.model.mongodb_model import MongoModel


class Classroom(MongoModel):
    id: Optional[ObjectId] = Field(None)
    audioUrls: List[str] = Field()
    course: str = Field()
    imageUrls: List[str] = Field()
    module: str = Field()
    phrases: List[str] = Field()
    prime: str = Field()
    studentId: str = Field()
    target: str = Field()
    text: str = Field()
    videoUrls: List[str] = Field()

    @validator('id', pre=True)
    def convert_id_to_objectid(cls, v):
        if isinstance(v, str):
            try:
                return ObjectId(v)
            except InvalidId:
                raise ValueError("Not a valid ObjectId")
        return v
