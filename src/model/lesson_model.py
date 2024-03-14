from typing import Optional

from bson import ObjectId
from bson.errors import InvalidId
from pydantic import Field, validator

from src.model.mongodb_model import MongoModel


class Lesson(MongoModel):
    id: Optional[ObjectId] = Field(None)
    name: str = Field()
    dictionary: ObjectId = Field(None)
    phrase: ObjectId = Field(None)
    prime: ObjectId = Field(None)
    text: ObjectId = Field(None)
    youtubeUrl: ObjectId = Field(None)

    @validator('id', pre=True)
    def convert_id_to_objectid(cls, v):
        if isinstance(v, str):
            try:
                return ObjectId(v)
            except InvalidId:
                raise ValueError("Not a valid ObjectId")
        return v
