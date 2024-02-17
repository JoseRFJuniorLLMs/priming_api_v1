from beanie import Document
from bson import ObjectId
from typing import List, Optional
from pydantic import datetime_parse

from src.Model.StatusOnline import StatusOnline


class Student(Document):
    _id: Optional[str]
    name: str
    email: str
    tax_ident_number: str
    personal_ident_number: str
    login: str
    password: str
    status: StatusOnline = StatusOnline.ACTIVE
    course: List[ObjectId] = []
    lesson_done: List[ObjectId] = []
    scheduled_lessons: List[ObjectId] = []
    books: List[ObjectId] = []
    list_word_text: List[ObjectId] = []
    gender: str
    phone: str
    end: str
    country: str
    city: str
    spoken_language: str
    linkedin: str
    facebook: str
    instagram: str
    tiktok: str
    x: str
    image_url: str
    date_create: str
    bitcoin: List[ObjectId] = []

    @classmethod
    async def validate_login(cls, login: str, password: str):
        student = await cls.find_one({"login": login, "password": password})
        return student

    def __str__(self):
        return {
            "name": self.name,
            "email": self.email,
            "status": self.status,
            "online": self.online,
            "login": self.login
        }

    class Settings:
        name = "StudentCollection"

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: dict
        }
