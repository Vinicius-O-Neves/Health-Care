import json
from typing import Type

import requests
from requests import Response

from healthcare.data.firebase.FirebaseDb import FirebaseDb
from healthcare.data.firebase.model.PersonImcModel import PersonImcModel
from healthcare.data.firebase.model.PersonIngestionModel import PersonIngestionModel

'''Classe que contem todas funções para acesso e leitura no Firebase'''


class FirebaseRepositoryImp:

    @staticmethod
    async def getImcFromFirebase(id: str, day: str) -> list[str] | None:
        try:
            request = requests.get(
                f'{FirebaseDb().BASE_URL}/{id}/{day}/IMC/.json'
            )
            imcList = [
                str(request.json()[key])
                    .replace("{", "")
                    .replace("}", "")
                for key in request.json()
            ]

            return imcList
        except Exception as e:
            print(str(e))
            return None

    @staticmethod
    async def sendImcToFirebase(imc=Type[PersonImcModel]) -> Response | str:
        try:
            request = requests.post(
                f'{FirebaseDb().BASE_URL}/{imc.id}/{imc.day}/IMC/.json',
                data=json.dumps(imc.info)
            )

            return request
        except Exception as e:
            print(str(e))
            return "Erro ao tentar enviar o Firebase"

    @staticmethod
    async def getIngestionFromFirebase(id: str, day: str) -> list[str] | None:
        try:
            request = requests.get(
                f'{FirebaseDb().BASE_URL}/{id}/{day}/Ingestion/.json'
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
            return None

    @staticmethod
    async def sendIngestionToFirebase(ingestion=Type[PersonIngestionModel]) -> Response | str:
        try:
            request = requests.post(
                f'{FirebaseDb().BASE_URL}/{ingestion.id}/{ingestion.day}/Ingestion/.json',
                data=json.dumps(ingestion.info)
            )

            return request
        except Exception as e:
            print(str(e))
            return "Erro ao tentar enviar o Firebase"

    @staticmethod
    async def sendAgeAndWeightToFirebase(id: str, day: str, age: str, weight: str) -> Response | str:
        try:
            request = requests.post(
                f'{FirebaseDb().BASE_URL}/{id}/{day}/PersonInformation/.json',
                data=json.dumps({'age': age, 'weight': weight})
            )

            return request
        except Exception as e:
            print(str(e))
            return "Erro ao tentar enviar o Firebase"
