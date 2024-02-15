from beanie import Document
from bson import ObjectId
from typing import List, Optional

from src.Model.Status import Status


class Student(Document):
    _id: Optional[str]
    name: str
    email: str
    tax_ident_number: str
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
            ObjectId: dict
        }
