from typing import List, Optional
from beanie import Document
from bson import ObjectId

from Model.Status import Status


class Course(Document):
    _id: Optional[ObjectId] = None
    name: str
    objective: str
    content: List[str]
    category: str
    level: str
    price: str
    status: Status = Status.ACTIVE
    start: str
    end: str
    duration_month: int
    class Settings:
        name = "CourseCollection"