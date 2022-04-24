from ImcClassifier import ImcClassifier
from healthcare.resources.Strings import Strings


class ImcCalculator:

    def calculate(self, weight: int, height: float) -> float:
        self.imc = weight / (height ** 2)
        return round(self.imc, 2)

    def analyze(self, age: int, gender: str) -> str:
        self.gender = gender.lower()

        if age >= 20:
            return ImcClassifier().adult(self.imc)
        elif 20 > age >= 10 and self.gender == Strings().male:
            return ImcClassifier().manWith10To19(age, self.imc)
        elif 20 > age >= 10 and self.gender == Strings().female:
            return ImcClassifier().womanWith10To19(age, self.imc)


imc = ImcCalculator()
print(imc.calculate(62, 1.83))
print(imc.analyze(19, "masculino"))
