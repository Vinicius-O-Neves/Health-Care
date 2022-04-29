import requests
from model.FoodItemsModel import FoodItemsModel
from healthcare.domain.CaloriesForFoodApiRepository import CaloriesForFoodApiRepository
from RequestsInstance import RequestsInstance
from typing import Type


class CaloriesForFoodApiRepositoryImp(CaloriesForFoodApiRepository):

    @staticmethod
    def getAllByFood(food=Type[str]) -> FoodItemsModel:
        foodList = requests.get(
            RequestsInstance().BASE_URL + f"calorias/?descricao={food}") \
            .json()

        return foodList


print(CaloriesForFoodApiRepositoryImp.getAllByFood("Frango"))
