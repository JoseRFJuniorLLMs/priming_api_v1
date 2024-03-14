from typing import List, Optional

from bson import ObjectId
from bson.errors import InvalidId
from pydantic import Field, validator

from src.model.mongodb_model import MongoModel


class Bitcoin(MongoModel):
    id: Optional[ObjectId] = Field(None)
    bitcoinValue: str = Field()
    creationDate: str = Field()
    genre: str = Field()
    isbn: str = Field()
    pages: int = Field()
    price: float = Field()
    publication_year: str = Field()
    title: str = Field()
    url: Optional[str] = Field()
    availability:  bool = Field()
    publisher: str = Field()

    @validator('id', pre=True)
    def convert_id_to_objectid(self, v):
        if isinstance(v, str):
            try:
                return ObjectId(v)
            except InvalidId:
                raise ValueError("Not a valid ObjectId")
        return v
