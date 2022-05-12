import requests
from model.FoodItemsModel import FoodItemsModel
from RequestsInstance import RequestsInstance
from typing import Type


class CaloriesForFoodApiRepositoryImp:

    @staticmethod
    def getAllByFood(food=Type[str]) -> list[FoodItemsModel]:
        foodList = requests.get(
            RequestsInstance().BASE_URL + f"calorias/?descricao={food}")

        return foodList.json()


print(CaloriesForFoodApiRepositoryImp.getAllByFood("Frango"))
