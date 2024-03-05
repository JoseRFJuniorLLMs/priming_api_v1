from beanie import Document
from bson import ObjectId
from typing import List, Optional

from pydantic import datetime_parse

from src.Model.StatusOnline import StatusOnline


from src.Model.Status import Status



class Student(Document):
    _id: Optional[str]
    name: str
    email: str
    tax_ident_number: str

    personal_ident_number: str
    login: str
    password: str
    status: StatusOnline = StatusOnline.ACTIVE
    courses: Optional[List[ObjectId]] = []
    lessons_done: Optional[List[ObjectId]] = []
    scheduled_lessons: Optional[List[ObjectId]] = []
    books: Optional[List[ObjectId]] = []
    list_word_text: Optional[List[ObjectId]] = []
    # gender: Optional[str]
    # phone: Optional[str]
    # end: Optional[str]
    # country: Optional[str]
    # city: Optional[str]
    # spoken_language: Optional[str]
    # linkedin: Optional[str]
    # facebook: Optional[str]
    # instagram: Optional[str]
    # tiktok: Optional[str]
    # x: Optional[str]
    # image_url: Optional[str]
    # date_create: Optional[str]
    bitcoin: Optional[List[ObjectId]] = []

    login: str
    password: str
    status: Status = Status.ACTIVE
    course: List[ObjectId] = []
    lesson_done: List[ObjectId] = []


    @classmethod
    async def validate_login(cls, login: str, password: str):
        student = await cls.find_one({"login": login, "password": password})
        return student

    def __str__(self):
        return {
            "name": self.name,
            "email": self.email,
            "status": self.status,
            "login": self.login
        }

    class Settings:
        name = "StudentCollection"

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
            ObjectId: dict
        }
