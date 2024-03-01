import datetime
from typing import List, Optional
from beanie import Document, PydanticObjectId


class BitCoin(Document):
    _id: Optional[PydanticObjectId] = None
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
    dateupdate: datetime

    class Settings:
        name = "BitCoinCollection"
