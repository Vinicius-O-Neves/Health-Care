from dataclasses import dataclass


@dataclass(order=True)
class FoodItemsModel:
    id: dict
    description: str
    quantity: str
    calories: str
