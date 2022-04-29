import abc
from abc import ABC
from healthcare.data.requests.model.FoodItemsModel import FoodItemsModel


class CaloriesForFoodApiRepository(ABC):

    def __init__(self):
        pass

    @abc.abstractmethod
    def getAllByFood(self) -> FoodItemsModel:
        pass
