from beanie import Document
from src.Model.Type import Type


class Login(Document):
    username: str
    password: str
    type: Type = Type.STUDENT
