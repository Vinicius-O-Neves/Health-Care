import json
import asyncio
from imcproject.data.firebase.FirebaseRepositoryImp import FirebaseRepositoryImp
from imcproject.data.firebase.model.PersonIngestionModel import PersonIngestionModel

asyncio.run(
    FirebaseRepositoryImp.sendToFirebase(PersonIngestionModel("06052022", {'batata': '300g'}))
    ) 