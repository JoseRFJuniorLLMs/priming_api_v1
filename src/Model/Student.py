from beanie import Document
from beanie import PydanticObjectId
from typing import List, Optional
from pydantic import Field

from src.Model.StatusOnline import StatusOnline


class Student(Document):
    _id: PydanticObjectId()
    student_id: Optional[str] = Field(alias='_id')

    name: str
    email: str
    tax_ident_number: str
    personal_ident_number: str
    login: str
    password: str
    status: StatusOnline = StatusOnline.ACTIVE
    courses: Optional[List[PydanticObjectId]] = []
    lessons_done: Optional[List[PydanticObjectId]] = []
    scheduled_lessons: Optional[List[PydanticObjectId]] = []
    books: Optional[List[PydanticObjectId]] = []
    list_word_text: Optional[List[PydanticObjectId]] = []
    gender: Optional[str]
    phone: Optional[str]
    end: Optional[str]
    country: Optional[str]
    city: Optional[str]
    spoken_language: Optional[str]
    linkedin: Optional[str]
    facebook: Optional[str]
    instagram: Optional[str]
    tiktok: Optional[str]
    x: Optional[str]
    image_url: Optional[str]
    date_create: Optional[str]
    bitcoin: Optional[List[PydanticObjectId]] = []

    def __str__(self):
        return {
            "name": self.name,
            "email": self.email,
            "status": self.status,
            "login": self.login
        }

    class Config:
        name = "StudentCollection"
        arbitrary_types_allowed = True
        json_encoders = {
            PydanticObjectId: str
        }
        id_field = "student_id"
