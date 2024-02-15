from typing import List, Optional
from beanie import Document
from bson import ObjectId

from src.Model.Status import Status


class Course(Document):
    _id: Optional[ObjectId] = None
    name: str
    objective: str
    content: List[str]
    lessons: List[str]
    category: str
    level: str
    price: str
    status: Status = Status.ACTIVE
    start: str
    end: str
