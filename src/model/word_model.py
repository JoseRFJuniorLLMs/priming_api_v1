from typing import List, Optional

from bson import ObjectId
from bson.errors import InvalidId
from pydantic import Field, validator

from src.model import MongoModel


class ListWord(MongoModel):
    id: Optional[ObjectId] = Field(None)
    list_word: List[str] = Field()
    text_prime: ObjectId | None = Field(None)
    total: int | None = Field(None)

    @validator('id', 'text_prime', pre=True)
    def convert_id_to_objectid(cls, v):
        if isinstance(v, str):
            try:
                return ObjectId(v)
            except InvalidId:
                raise ValueError("Not a valid ObjectId")
        return v

