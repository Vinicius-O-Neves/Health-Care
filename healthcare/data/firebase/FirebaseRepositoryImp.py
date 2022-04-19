import requests
import json
import asyncio
from typing import Type
from domain.FirebaseRepository import FirebaseRepository
from data.firebase.FirebaseDb import FirebaseDb
from data.firebase.model.PersonIngestionModel import PersonIngestionModel

class FirebaseRepositoryImp(FirebaseRepository):

    async def sendToFirebase(ingestion = Type[PersonIngestionModel]):
        try:
            request = requests.post(
                f'{FirebaseDb().url}/{ingestion.personCpf}/{ingestion.dia}/.json',
                data = json.dumps(ingestion.info)
            )
            print(request)
            print(request.text)
        except Exception as e:
            print("Erro ao tentar enviar o Firebase")
            print(str(e))
