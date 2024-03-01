from typing import List, Optional
from beanie import Document, PydanticObjectId


class Books(Document):
    _id: Optional[PydanticObjectId] = None
    title: str
    author: str
    isbn: str
    publisher: str
    publication_year: str
    genre: str
    pages: str
    language: str
    description: str
    price: str
    availability: str
    url: str

    class Settings:
        name = "BooksCollection"
