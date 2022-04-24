import asyncio
from datetime import datetime
from data.firebase.repository.FirebaseRepositoryImp import FirebaseRepositoryImp
from data.firebase.model.PersonIngestionModel import PersonIngestionModel

asyncio.run(
    FirebaseRepositoryImp.sendToFirebase(PersonIngestionModel(
        4421150987652,
        datetime.today().strftime("%Y-%m-%d").replace('-', ''),
        {'pao': '300g', 'aaaaa': '70g'}
        )
    )
)
