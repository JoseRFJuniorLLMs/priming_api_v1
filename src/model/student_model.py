from datetime import datetime
from enum import Enum
from typing import List, Optional

from bson import ObjectId
from bson.errors import InvalidId
from pydantic import Field, validator, BaseModel

from src.model.mongodb_model import MongoModel


class StudentStatus(Enum):
    ACTIVE = "Active"
    INACTIVE = "Inactive"


class Student(MongoModel):
    id: Optional[ObjectId] = Field(None)

    name: str = Field()
    password: str = Field()
    login: str = Field()
    email: str = Field()
    status: str = Field(default=StudentStatus.ACTIVE)
    city: Optional[str] = Field(None)
    country: Optional[str] = Field(None)
    tax_ident_number: Optional[str] = Field(None)
    personal_ident_number: Optional[str] = Field(None)
    date_create: Optional[datetime] = Field(None)
    facebook: Optional[str] = Field(None)
    x: Optional[str] = Field(None)
    tiktok: Optional[str] = Field(None)
    instagram: Optional[str] = Field(None)
    linkedin: Optional[str] = Field(None)
    phone: Optional[str] = Field(None)
    spoken_language: Optional[str] = Field(None)
    image_url: Optional[str] = Field(None)
    bitcoin: List[ObjectId] = Field(default=[])
    lessons_done: List[ObjectId] = Field(default=[])
    books: List[ObjectId] = Field(default=[])
    courses: List[ObjectId] = Field(default=[])
    scheduled_lessons: List[ObjectId] = Field(default=[])
    list_word_text: List[ObjectId] = Field(default=[])

    @validator('id', pre=True)
    def convert_id_to_objectid(cls, v):
        if isinstance(v, str):
            try:
                return ObjectId(v)
            except InvalidId:
                raise ValueError("Not a valid ObjectId")
        return v


class StudentLogin(BaseModel):
    email: str = Field(default=None)
    password: str = Field(default=None)
