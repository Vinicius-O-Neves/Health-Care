import asyncio
import re
from datetime import datetime
from healthcare.data.firebase.model.PersonIngestionModel import *
from healthcare.data.firebase.repository.FirebaseRepositoryImp import FirebaseRepositoryImp


class CaloriesCalculator:

    def totalConsumedCalories(id: str) -> tuple[float | int, float]:

        ingestionList = asyncio.run(FirebaseRepositoryImp.getIngestionFromFirebase(
            id,
            datetime.today().strftime("%Y-%m-%d").replace('-', '')
        ))
        total = sum([float(item) for item in re.findall("\d+", str(ingestionList))])
        dailyLimit = 3000
        consumedCalories = dailyLimit - total
        return total, consumedCalories

    def listOfIngestion(id: str) -> list[PersonIngestionModel]:

        response = asyncio.run(FirebaseRepositoryImp.getIngestionFromFirebase(
            id,
            datetime.today().strftime("%Y-%m-%d").replace('-', '')
        ))
        return [str(items).replace("'", '') for items in response]

print(CaloriesCalculator.totalConsumedCalories("4cd5c7c0-7918-40a8-a551-aed42b817524"))
print(CaloriesCalculator.listOfIngestion("4cd5c7c0-7918-40a8-a551-aed42b817524"))