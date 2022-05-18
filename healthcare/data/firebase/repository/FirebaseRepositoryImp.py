import requests
import json
from typing import Type

from requests import Response

from healthcare.data.firebase.FirebaseDb import FirebaseDb
from healthcare.data.firebase.model.PersonIngestionModel import PersonIngestionModel

'''Classe que contem todas funções para acesso e leitura no Firebase'''


class FirebaseRepositoryImp:

    @staticmethod
    async def getIngestionFromFirebase(id: str, day: str) -> list[str] | str:
        try:
            request = requests.get(
                f'{FirebaseDb().BASE_URL}/{id}/{day}/.json'
            )
            ingestionList = [
                str(request.json()[key])
                    .replace("{", "")
                    .replace("}", "")
                for key in request.json()
            ]

            return ingestionList
        except Exception as e:
            print(str(e))
            return "Erro ao tentar puxar do Firebase"

    @staticmethod
    def sendIngestionToFirebase(ingestion=Type[PersonIngestionModel]) -> Response | str:
        try:
            request = requests.post(
                f'{FirebaseDb().BASE_URL}/{ingestion.id}/{ingestion.day}/.json',
                data=json.dumps(ingestion.info)
            )

            return request
        except Exception as e:
            print(str(e))
            return "Erro ao tentar enviar o Firebase"
