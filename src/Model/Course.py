from decimal import Decimal
from typing import List, Optional
from beanie import Document, PydanticObjectId
from pydantic import Field

from src.Model.StatusOnline import StatusOnline


class Course(Document):

    _id: Optional[PydanticObjectId] = None
    course_id: Optional[str] = Field(alias="_id")

    name: str
    objective: str
    content: List[str]
    category: str
    level: str
    price: Decimal
    status: StatusOnline = StatusOnline.ACTIVE
    start: str
    end: str
    duration_month: int

    class Settings:
        name = "CourseCollection"
        arbitrary_types_allowed = True
        json_encoders = {
            PydanticObjectId: str
        }
        id_field = "course_id"
