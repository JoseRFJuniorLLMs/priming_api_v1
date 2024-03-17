from typing import Optional

from bson import ObjectId
from bson.errors import InvalidId
from pydantic import Field, validator

from src.model.mongodb_model import MongoModel


class Lesson(MongoModel):
    id: Optional[ObjectId] = Field(None)
    name: str = Field()
    dictionary: ObjectId | None = Field(None)
    phrase: ObjectId | None = Field(None)
    prime: ObjectId | None = Field(None)
    text: ObjectId | None = Field(None)
    youtubeUrl: ObjectId | None = Field(None)

    @validator(
        'id',
        'dictionary',
        'phrase',
        'prime',
        'text',
        'youtubeUrl',
        pre=True,
        check_fields=False)
    def convert_id_to_objectid(cls, v):
        if isinstance(v, str):
            try:
                return ObjectId(v)
            except InvalidId:
                raise ValueError("Not a valid ObjectId")
        return v
