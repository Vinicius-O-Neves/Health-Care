import json
import asyncio
from imccalculator.data.firebase.FirebaseRepositoryImp import FirebaseRepositoryImp

asyncio.run(FirebaseRepositoryImp.sendToFirebase("06052022", {'batata': '900g'})) 