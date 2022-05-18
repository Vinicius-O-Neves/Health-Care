import requests
from model.FoodItemsModel import FoodItemsModel
from RequestsInstance import RequestsInstance


class CaloriesForFoodApiRepositoryImp:

    @staticmethod
    def getAllFoodsByType(type: str) -> list[list[FoodItemsModel]]:
        response = requests.get(
            RequestsInstance().BASE_URL + f"calorias/?descricao={type}").json()
        foodList = [
            [
                item['descricao'],
                str(item['quantidade']).replace("\xa0", ""),
                item['calorias']]
            for item in response
        ]

        return foodList

