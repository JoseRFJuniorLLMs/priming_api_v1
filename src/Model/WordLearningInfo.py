from typing import Optional
from beanie import Document, PydanticObjectId
from bson import ObjectId
import datetime


class WordLearningInfo(Document):
    _id: Optional[PydanticObjectId] = None
    word: str
    last_reviewed: datetime.datetime
    difficulty: int

    class Settings:
        name = "WordLearningInfoCollection"

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }

    def schedule_next_review_1_hour(self):
        return self.last_reviewed + datetime.timedelta(hours=1)

    def schedule_next_review_24_hours(self):
        return self.last_reviewed + datetime.timedelta(days=1)

    def schedule_next_review_1_week(self):
        return self.last_reviewed + datetime.timedelta(weeks=1)

    def schedule_next_review_1_month(self):
        next_month = self.last_reviewed.month + 1
        next_year = self.last_reviewed.year + next_month // 12
        next_month %= 12
        if next_month == 0:
            next_month = 12
        return self.last_reviewed.replace(month=next_month, year=next_year)
