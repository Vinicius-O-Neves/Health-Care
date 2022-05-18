import asyncio
from datetime import datetime
from healthcare.data.firebase.repository.FirebaseRepositoryImp import FirebaseRepositoryImp
from healthcare.data.firebase.model.PersonIngestionModel import PersonIngestionModel

print(FirebaseRepositoryImp.sendIngestionToFirebase(PersonIngestionModel(
    "4cd5c7c0-7918-40a8-a551-aed42b817524",
    datetime.today().strftime("%Y-%m-%d").replace('-', ''),
    {'tatata': '300g', 'aaa': '70g'}
)
))

print(asyncio.run(
    FirebaseRepositoryImp.getIngestionFromFirebase(
        "4cd5c7c0-7918-40a8-a551-aed42b817524",
        datetime.today().strftime("%Y-%m-%d").replace('-', '')
    )
))
