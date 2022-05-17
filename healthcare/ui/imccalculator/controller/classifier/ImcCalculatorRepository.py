from ImcClassifier import ImcClassifier
from healthcare.resources.Strings import Strings


class ImcCalculatorRepository:

    def __init__(
            self,
            weight: int,
            height: float,
            age: int,
            gender: str
    ):
        self.weight = weight
        self.height = height
        self.age = age
        self.gender = gender.lower()
        self.imc = 0

    def calculate(self) -> float:
        self.imc = self.weight / (self.height ** 2)
        return round(self.imc, 2)

    def analyze(self) -> str:
        if self.age >= 20:
            return ImcClassifier().adult(self.imc)
        elif 20 > self.age >= 10 and self.gender == Strings().male:
            return ImcClassifier().manWith10To19(self.age, self.imc)
        elif 20 > self.age >= 10 and self.gender == Strings().female:
            return ImcClassifier().womanWith10To19(self.age, self.imc)


imc = ImcCalculatorRepository(62, 1.83, 19, "masculino")
print(imc.calculate())
print(imc.analyze())
