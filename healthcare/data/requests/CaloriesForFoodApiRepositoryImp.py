import requests 
from .model.FoodItemsModel import FoodItemsModel
from healthcare.domain.CaloriesForFoodApiRepository import CaloriesForFoodApiRepository
from .RequestsInstance import RequestsInstance
from typing import Type


class CaloriesForFoodApiRepositoryImp(CaloriesForFoodApiRepository):

    @staticmethod
    def getAllByFood(food=Type[str]) -> list[FoodItemsModel]:
        foodList = requests.get(
            RequestsInstance().BASE_URL + f"calorias/?descricao={food}")

        return foodList.json()

    
print(CaloriesForFoodApiRepositoryImp.getAllByFood("Frango assado"))

