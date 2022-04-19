from abc import ABC, abstractclassmethod
import asyncio
from data.firebase.model.PersonIngestionModel import PersonIngestionModel
from typing import Type

class FirebaseRepository(ABC):
    
    @abstractclassmethod
    async def sendToFirebase(self, ingestion = Type[PersonIngestionModel]):
        pass

    @abstractclassmethod
    async def getFromFirebase(self, dia: str, totalCal: int):
        pass
    

