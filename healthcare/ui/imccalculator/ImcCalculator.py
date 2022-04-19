class ImcCalculator:

    def calculate(self, weight: int, height: float) -> int:
        self.imc = weight / (height ** 2)
        return round(self.imc, 1)

    def analyze(self, age: int, gender: str):
        self.gender = gender.lower()

        if age >= 20:
            print(self.adult())
        elif age < 20 and age >= 10 and self.gender == "masculino":
            self.manWith10To19(age)
        elif age < 20 and age >= 10 and self.gender == "feminino":
            self.womanWith10To19(age)
    
    def adult(self):
        interval = {
            self.imc < 18.5: "Abaixo do Peso",
            18.5 <= self.imc <= 24.9: "Peso Normal",
            25 <= self.imc <= 29.9: "Pré-Obesidade",
            30 <= self.imc <= 34.9: "Obesidade Grau 1",
            35 <= self.imc <= 39.9: "Obesidade Grau 2",
            self.imc >= 40: "Obesidade Grau 3" 
        }
        return interval[True]

    def womanWith10To19(self, age: int):
        interval = {
            age == 10 and 14.23 >= self.imc <= 15.09: 5,
            age == 10 and 15.09 >= self.imc <= 17: 15,
            age == 10 and 17 >= self.imc <= 20.19: 50,
            age == 10 and 20.19 >= self.imc <= 23.20: 85,
            age == 10 and self.imc >= 23.20: 85,

            age == 11 and 14.60 >= self.imc <= 15.53: 5,
            age == 11 and 15.53 >= self.imc <= 17.67: 15,
            age == 11 and 17.67 >= self.imc <= 21.18: 50,
            age == 11 and 21.18 >= self.imc <= 24.59: 85,
            age == 11 and self.imc >= 24.59: 95,

            age == 12 and 14.98 >= self.imc <= 15.98: 5,
            age == 12 and 15.98 >= self.imc <= 18.35: 15,
        }
        return interval[True]

    def manWith10To19(self, age: int):
        print("homem entre 10 a 19")

imc = ImcCalculator()
print(imc.calculate(61, 1.77))
print(imc.analyze(10, "feminino"))