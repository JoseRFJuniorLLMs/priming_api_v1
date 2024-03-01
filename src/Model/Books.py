from typing import List, Optional
from beanie import Document, PydanticObjectId
from pydantic import Field


class Books(Document):

    _id: Optional[PydanticObjectId] = None
    books_id: Optional[str] = Field(alias="_id")

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
        arbitrary_types_allowed = True
        json_encoders = {
            PydanticObjectId: str
        }
        id_field = "books_id"