from ImcClassifier import ImcClassifier
from healthcare.resources.Strings import Strings


class ImcCalculatorRepository:

    imc = None

    @classmethod
    def calculate(cls, weight: int, height: float) -> float:
        cls.imc = weight / (height ** 2)
        return round(cls.imc, 2)

    @classmethod
    def analyze(cls, age: int, gender: str) -> str:
        gender = gender.lower()

        if age >= 20:
            return ImcClassifier().adult(cls.imc)
        elif 20 > age >= 10 and gender == Strings().male:
            return ImcClassifier().manWith10To19(age, cls.imc)
        elif 20 > age >= 10 and gender == Strings().female:
            return ImcClassifier().womanWith10To19(age, cls.imc)

imc = ImcCalculatorRepository()
print(imc.calculate(62, 1.83))
print(imc.analyze(19, "masculino"))
