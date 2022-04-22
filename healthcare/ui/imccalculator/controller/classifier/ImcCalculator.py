from ImcClassifier import ImcClassifier

class ImcCalculator:

    def calculate(self, weight: int, height: float) -> int:
        self.imc = weight / (height ** 2)
        return round(self.imc, 2)

    def analyze(self, age: int, gender: str) -> str:
        self.gender = gender.lower()

        if age >= 20:
            return ImcClassifier().adult(self.imc)
        elif 20 > age >= 10 and self.gender == "masculino":
            pass
        elif 20 > age >= 10 and self.gender == "feminino":
            return ImcClassifier().womanWith10To19(age, self.imc)
            
imc = ImcCalculator()
print(imc.calculate(74, 1.67))
print(imc.analyze(17, "feminino"))