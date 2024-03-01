import datetime
from typing import List, Optional
from beanie import Document, PydanticObjectId
from pydantic import Field


class BitCoin(Document):

    _id: Optional[PydanticObjectId] = None
    bitcoin_id: Optional[str] = Field(alias="_id")

    name: str
    description: str
    primeCoinValue: float
    bitcoinValue: float
    lastUpdated: datetime
    ownerId: str
    transactionHistory: List[str]
    initialBalance: float
    publicKey: str
    privateKey: str
    creationDate: datetime
    issue: str
    dateUpdate: datetime

    class Settings:
        name = "BitCoinCollection"
        arbitrary_types_allowed = True
        json_encoders = {
            PydanticObjectId: str
        }
        id_field = "bitcoin_id"