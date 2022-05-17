import requests
from model.FoodItemsModel import FoodItemsModel
from RequestsInstance import RequestsInstance
from typing import Type

class CaloriesForFoodApiRepositoryImp:

    @staticmethod
    def getAllByFood(food=Type[str]) -> list[list[FoodItemsModel]]:
        response = requests.get(
            RequestsInstance().BASE_URL + f"calorias/?descricao={food}").json()
        foodList = [
            [
                item['descricao'],
                str(item['quantidade']).replace("\xa0", ""),
                item['calorias']]
                for item in response
        ]

        return foodList


print(CaloriesForFoodApiRepositoryImp.getAllByFood("Macarrão"))
