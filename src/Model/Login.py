import time

from beanie import Document
from Model.Type import Type


class Login(Document):
    username: str
    password: str
    type: Type = Type.STUDENT
    start: time
    end: time
