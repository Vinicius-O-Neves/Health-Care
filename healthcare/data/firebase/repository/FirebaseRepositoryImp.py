import requests
import json
from typing import Type
from healthcare.domain.FirebaseRepository import FirebaseRepository
from healthcare.data.firebase.FirebaseDb import FirebaseDb
from healthcare.data.firebase.model.PersonIngestionModel import PersonIngestionModel


class FirebaseRepositoryImp(FirebaseRepository):

    @staticmethod
    async def getFromFirebase(dia: str, totalCal: int):
        print("okok")

    @staticmethod
    async def sendToFirebase(ingestion=Type[PersonIngestionModel]):
        try:
            request = requests.post(
                f'{FirebaseDb().url}/{ingestion.personCpf}/{ingestion.dia}/.json',
                data=json.dumps(ingestion.info)
            )
            print(request)
            print(request.text)
        except Exception as e:
            print("Erro ao tentar enviar o Firebase")
            print(str(e))
