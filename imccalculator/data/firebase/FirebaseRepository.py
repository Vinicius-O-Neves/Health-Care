import requests
import json
import asyncio
from imccalculator.data.firebase.FirebaseDb import FireBaseDb

class FirebaseRepository:
    
    async def sendToFirebase(dia, info):
        try:
            request = requests.post(
                f'{FireBaseDb().url}/{dia}/.json',
                data=json.dumps(info)
            )
            print(request)
        except Exception as e:
            print("Erro ao tentar enviar o Firebase")
            print(str(e))

