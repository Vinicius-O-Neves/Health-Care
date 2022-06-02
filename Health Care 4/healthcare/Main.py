import asyncio
from datetime import datetime
from healthcare.data.firebase.repository.FirebaseRepositoryImp import FirebaseRepositoryImp
from healthcare.data.firebase.model.PersonIngestionModel import PersonIngestionModel
from healthcare.data.firebase.model.PersonImcModel import PersonImcModel

print(FirebaseRepositoryImp.sendImcToFirebase(PersonImcModel(
    "4cd5c7c0-7918-40a8-a551-aed42b817524",
    datetime.today().strftime("%Y-%m-%d").replace('-', ''),
    {'IMC': '20', 'classification': 'magrinho'}
)
))

print(asyncio.run(
    FirebaseRepositoryImp.getImcFromFirebase(
        "4cd5c7c0-7918-40a8-a551-aed42b817524",
        datetime.today().strftime("%Y-%m-%d").replace('-', '')
    )
))

print(FirebaseRepositoryImp.sendIngestionToFirebase(PersonIngestionModel(
    "4cd5c7c0-7918-40a8-a551-aed42b817524",
    datetime.today().strftime("%Y-%m-%d").replace('-', ''),
    {'PARMEGIANA': '1000g', 'BATATA': '200g', 'type': 'Almoço'}
)
))

print(asyncio.run(
    FirebaseRepositoryImp.getIngestionFromFirebase(
        "4cd5c7c0-7918-40a8-a551-aed42b817524",
        datetime.today().strftime("%Y-%m-%d").replace('-', '')
    )
))

print(FirebaseRepositoryImp.sendAgeAndWeightToFirebase(
    "4cd5c7c0-7918-40a8-a551-aed42b817524",
    datetime.today().strftime("%Y-%m-%d").replace('-', ''),
    "19",
    "1.69"
))
