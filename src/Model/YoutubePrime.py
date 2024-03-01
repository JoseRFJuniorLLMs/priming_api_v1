from typing import Optional, List

from beanie import Document, PydanticObjectId


class YoutubePrime(Document):
    _id: Optional[PydanticObjectId] = None
    prime: str
    target: str
    url: List[str]

    class Settings:
        name = "primeTargetYoutubeCollection"
