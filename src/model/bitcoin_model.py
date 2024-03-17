from typing import List, Optional

from bson import ObjectId
from bson.errors import InvalidId
from pydantic import Field, validator

from src.model.mongodb_model import MongoModel


class Bitcoin(MongoModel):
    id: Optional[ObjectId] = Field(None)
    bitcoinValue: str = Field()
    creationDate: str = Field()
    dateupdate: str = Field()
    description: str = Field()
    initialBalance: int = Field()
    issue: float = Field()
    name: str = Field()
    ownerId: str = Field()
    primeCoinValue: Optional[str] = Field()
    transactionHistory:  bool = Field()
    lastUpdated: str = Field()
    privateKey: str = Field()
    publicKey: str = Field()

    @validator('id', pre=True)
    def convert_id_to_objectid(self, v):
        if isinstance(v, str):
            try:
                return ObjectId(v)
            except InvalidId:
                raise ValueError("Not a valid ObjectId")
        return v
