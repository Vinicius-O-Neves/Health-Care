import requests
import json
from typing import Type
from healthcare.data.firebase.FirebaseDb import FirebaseDb
from healthcare.data.firebase.model.PersonIngestionModel import PersonIngestionModel

'''Classe que contem todas funções para acesso e leitura no Firebase'''
class FirebaseRepositoryImp:

    @staticmethod
    async def getIngestionFromFirebase(id: str, day: str):
        try:
            request = requests.get(
                f'{FirebaseDb().BASE_URL}/{id}/{day}/.json'
            )
            print(request.text)
        except Exception as e:
            print("Erro ao tentar puxar do Firebase")
            print(str(e))

    @staticmethod
    def sendIngestionToFirebase(ingestion=Type[PersonIngestionModel]):
        try:
            request = requests.post(
                f'{FirebaseDb().BASE_URL}/{ingestion.id}/{ingestion.day}/.json',
                data=json.dumps(ingestion.info)
            )
            print(request.text)
        except Exception as e:
            print("Erro ao tentar enviar o Firebase")
            print(str(e))
