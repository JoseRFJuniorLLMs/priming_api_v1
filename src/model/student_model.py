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
    status: str | None = Field(default=StudentStatus.ACTIVE)
    city: Optional[str] | None = Field(None)
    country: Optional[str] | None = Field(None)
    tax_ident_number: Optional[str] | None = Field(None)
    personal_ident_number: Optional[str] | None = Field(None)
    date_create: Optional[str] | None = Field(None)
    facebook: Optional[str] | None = Field(None)
    x: Optional[str] | None = Field(None)
    tiktok: Optional[str] | None = Field(None)
    instagram: Optional[str] | None = Field(None)
    linkedin: Optional[str] | None = Field(None)
    phone: Optional[str] | None = Field(None)
    spoken_language: Optional[str] | None = Field(None)
    image_url: Optional[str] | None = Field(None)
    bitcoin: List[ObjectId] | None = Field(default=[])
    lessons_done: List[ObjectId] | None = Field(default=[])
    books: List[ObjectId] | None = Field(default=[])
    courses: List[ObjectId] | None = Field(default=[])
    scheduled_lessons: List[ObjectId] | None = Field(default=[])
    list_word_text: List[ObjectId] | None = Field(default=[])

    @validator(
        'bitcoin',
        'lessons_done',
        'books',
        'courses',
        'scheduled_lessons',
        'list_word_text', pre=True)
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


class StudentLogin(BaseModel):
    email: str = Field(default=None)
    password: str = Field(default=None)
