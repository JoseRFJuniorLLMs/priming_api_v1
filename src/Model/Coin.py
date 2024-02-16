from beanie import Document
from datetime import datetime
from typing import List


class PrimeCoin(Document):
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
        name = "CoinCollection"
