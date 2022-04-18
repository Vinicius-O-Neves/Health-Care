import requests
import json
import asyncio
from typing import Type
from imcproject.domain.FirebaseRepository import FirebaseRepository
from imcproject.data.firebase.FirebaseDb import FirebaseDb
from imcproject.data.firebase.model.PersonIngestionModel import PersonIngestionModel

class FirebaseRepositoryImp(FirebaseRepository()):

    async def sendToFirebase(ingestion = Type[PersonIngestionModel]):
        try:
            request = requests.post(
                f'{FirebaseDb().url}/{ingestion.dia}/.json',
                data = json.dumps(ingestion.info)
            )
            print(request)
        except Exception as e:
            print("Erro ao tentar enviar o Firebase")
            print(str(e))