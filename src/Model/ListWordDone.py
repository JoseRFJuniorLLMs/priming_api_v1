

from typing import List, Optional
from beanie import Document
from bson import ObjectId
from Model.WordLearningInfo import WordLearningInfo

class ListWordDone(Document):
    _id: Optional[int] = None
    list_word: List[str]
    student: ObjectId
    words_info: List[WordLearningInfo]

    class Settings:
        name = "ListWordDoneCollection"

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }
