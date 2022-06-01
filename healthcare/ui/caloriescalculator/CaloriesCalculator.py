import asyncio
import re
from datetime import datetime
from healthcare.data.firebase.repository.FirebaseRepositoryImp import FirebaseRepositoryImp


class CaloriesCalculator:

    @staticmethod
    def totalConsumedCalories(id: str) -> tuple[float | int, float]:
        ingestionList = asyncio.run(FirebaseRepositoryImp.getIngestionFromFirebase(
            id,
            datetime.today().strftime("%Y-%m-%d").replace('-', '')
        ))
        total = sum([float(item) for item in re.findall("\d+", str(ingestionList))])
        dailyLimit = 3000
        consumedCalories = dailyLimit - total

        return total, consumedCalories

    @staticmethod
    def listOfIngestion(id: str) -> list[str]:
        response = asyncio.run(FirebaseRepositoryImp.getIngestionFromFirebase(
            id,
            datetime.today().strftime("%Y-%m-%d").replace('-', '')
        ))

        return [str(items).replace("'", '') for items in response]

    @staticmethod
    def manNeedsCalories(age: int, weight: float) -> float:
        interval = {
            0 >= age < 3: ((59.512 * weight) - 30.4),
            3 >= age < 10: ((22.706 * weight) + 504.3),
            10 >= age < 18: ((17.686 * weight) + 658.2),
            18 >= age < 30: ((15.057 * weight) + 692.2),
            30 >= age < 60: ((11.472 * weight) + 873.1),
            age >= 60: ((11.711 * weight) + 587.7)
        }
        return interval[True]

    @staticmethod
    def womanNeedCalories(age: int, weight: float) -> float:
        interval = {
            0 >= age < 3: ((58.317 * weight) - 31.1),
            3 >= age < 10: ((20.315 * weight) + 485.9),
            10 >= age < 18: ((13.384 * weight) + 692.6),
            18 >= age < 30: ((14.818 * weight) + 486.6),
            30 >= age < 60: ((8.126 * weight) + 845.6),
            age >= 60: ((9.082 * weight) + 658.5)

        }
        return interval[True]
