import asyncio
from datetime import datetime
from healthcare.data.firebase.repository.FirebaseRepositoryImp import FirebaseRepositoryImp
from healthcare.data.firebase.model.PersonIngestionModel import PersonIngestionModel

FirebaseRepositoryImp.sendIngestionToFirebase(PersonIngestionModel(
    "4cd5c7c0-7918-40a8-a551-aed42b817524",
    datetime.today().strftime("%Y-%m-%d").replace('-', ''),
    {'tatata': '300g', 'aaa': '70g'}
    )
)

asyncio.run(
    FirebaseRepositoryImp.getIngestionFromFirebase(
        "cfa51380-7475-4449-af7e-50ba71a3b11b",
        datetime.today().strftime("%Y-%m-%d").replace('-', '')
    )
)
