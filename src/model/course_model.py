from typing import List, Optional

from bson import ObjectId
from bson.errors import InvalidId
from pydantic import Field, validator

from src.model.mongodb_model import MongoModel


class Course(MongoModel):
    id: Optional[ObjectId] = Field(None)
    name: str = Field()
    category: str = Field()
    level: str = Field()
    price: str = Field()
    status: str = Field()
    objective: str = Field()
    content: List[str] = Field()
    lessons: List[ObjectId] = Field(None)

    @validator('id', pre=True)
    def convert_id_to_objectid(cls, v):
        if isinstance(v, str):
            try:
                return ObjectId(v)
            except InvalidId:
                raise ValueError("Not a valid ObjectId")
        return v
