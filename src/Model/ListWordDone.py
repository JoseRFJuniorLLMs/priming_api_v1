from typing import List, Optional
from beanie import Document, PydanticObjectId
from bson import ObjectId
from pydantic import Field

from src.Model.WordLearningInfo import WordLearningInfo


class ListWordDone(Document):

    _id: Optional[PydanticObjectId] = None
    list_word_done_id: Optional[str] = Field(alias="_id")

    list_word: List[str]
    student: ObjectId
    words_info: List[WordLearningInfo]

    class Settings:
        name = "ListWordDoneCollection"
        arbitrary_types_allowed = True
        json_encoders = {
            PydanticObjectId: str
        }
        id_field = "list_word_done_id"