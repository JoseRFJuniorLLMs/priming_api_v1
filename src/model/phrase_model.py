from typing import List, Optional

from bson import ObjectId
from bson.errors import InvalidId
from pydantic import Field, validator

from src.model.mongodb_model import MongoModel


class Phrase(MongoModel):
    id: Optional[ObjectId] = Field(None)
    prime: str = Field()
    target: str = Field()
    phrase: List[str] = Field()
    imagem: List[str] | None = Field(default=None)
    url: List[str] | None = Field(default=None)

    @validator('id', pre=True)
    def convert_id_to_objectid(cls, v):
        if isinstance(v, str):
            try:
                return ObjectId(v)
            except InvalidId:
                raise ValueError("Not a valid ObjectId")
        return v
