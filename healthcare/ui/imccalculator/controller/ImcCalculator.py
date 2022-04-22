class ImcCalculator:

    def calculate(self, weight: int, height: float) -> int:
        self.imc = weight / (height ** 2)
        return round(self.imc, 1)

    def analyze(self, age: int, gender: str):
        self.gender = gender.lower()

        if age >= 20:
            print(self.adult())
        elif 20 > age >= 10 and self.gender == "masculino":
            self.manWith10To19(age)
        elif 20 > age >= 10 and self.gender == "feminino":
            self.womanWith10To19(age)
    
        
    def manWith10To19(self, age: int):
        print("homem entre 10 a 19")

imc = ImcCalculator()
print(imc.calculate(61, 1.77))
print(imc.analyze(10, "feminino"))