from typing import List, Optional
from beanie import Document
from bson import ObjectId

<<<<<<< HEAD
from src.Model.StatusOnline import StatusOnline
=======
from src.Model.Status import Status
>>>>>>> origin/main


class Course(Document):
    _id: Optional[ObjectId] = None
    name: str
    objective: str
    content: List[str]
<<<<<<< HEAD
    category: str
    level: str
    price: str
    status: StatusOnline = StatusOnline.ACTIVE
    start: str
    end: str
    duration_month: int

    class Settings:
        name = "CourseCollection"
=======
    lessons: List[str]
    category: str
    level: str
    price: str
    status: Status = Status.ACTIVE
>>>>>>> origin/main
