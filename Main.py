import json
import asyncio
from imccalculator.data.firebase.FirebaseRepositoryImp import FirebaseRepositoryImp
from imccalculator.data.firebase.model.PersonInfoModel import PersonInfoModel

asyncio.run(FirebaseRepositoryImp.sendToFirebase(PersonInfoModel("06052022", {'batata': '400g'}))) 