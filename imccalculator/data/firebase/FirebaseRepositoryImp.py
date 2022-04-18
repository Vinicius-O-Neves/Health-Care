import requests
import json
import asyncio
from imccalculator.domain.FirebaseRepository import FirebaseRepository
from imccalculator.data.firebase.FirebaseDb import FirebaseDb

class FirebaseRepositoryImp(FirebaseRepository):

    async def sendToFirebase(PersonInfoModel):
        try:
            request = requests.post(
                f'{FirebaseDb().url}/{PersonInfoModel.dia}/.json',
                data = json.dumps(PersonInfoModel.info)
            )
            print(request)
        except Exception as e:
            print("Erro ao tentar enviar o Firebase")
            print(str(e))