from typing import List, Optional

from bson import ObjectId
from bson.errors import InvalidId
from pydantic import Field, validator

from src.model.mongodb_model import MongoModel


class Course(MongoModel):
    id: Optional[ObjectId] = Field(None)
    name: str = Field()
    category: str | None = Field(default=None)
    level: str = Field()
    price: str = Field()
    status: str = Field(default='ACTIVE')
    objective: str = Field()
    content: List[str] | None = Field(default=None)
    lessons: List[ObjectId] | None = Field(None)

    @validator('lessons', pre=True)
    def foreach_list(cls, v):
        if isinstance(v, list):
            a = []
            for i in v:
                a.append(ObjectId(i))
            return a

    @validator('id', pre=True)
    def convert_id_to_objectid(cls, v):
        if isinstance(v, str):
            try:
                return ObjectId(v)
            except InvalidId:
                raise ValueError("Not a valid ObjectId")
        return v
