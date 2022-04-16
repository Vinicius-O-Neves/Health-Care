import json
import asyncio
from imccalculator.data.firebase.FirebaseRepository import FirebaseRepository

asyncio.run(FirebaseRepository.sendToFirebase("04042022", {'batata': '400g'})) 