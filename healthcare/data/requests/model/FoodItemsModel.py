from dataclasses import dataclass


@dataclass(order=True)
class FoodItemsModel:
    description: str
    quantity: str
    calories: str
