from abc import ABC, abstractclassmethod
import asyncio

class FirebaseRepository(ABC):
    
    @abstractclassmethod
    async def sendToFirebase(self, dia, info):
        pass

    @abstractclassmethod
    async def getFromFirebase(self, dia, totalCal):
        pass

