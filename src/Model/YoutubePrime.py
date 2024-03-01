from typing import Optional, List

from beanie import Document, PydanticObjectId
from pydantic import Field


class YoutubePrime(Document):

    _id: Optional[PydanticObjectId] = None
    youtube_prime_id: Optional[str] = Field(alias="_id")

    prime: str
    target: str
    url: List[str]

    class Settings:
        name = "primeTargetYoutubeCollection"
        arbitrary_types_allowed = True
        json_encoders = {
            PydanticObjectId: str
        }
        id_field = "youtube_prime_id"