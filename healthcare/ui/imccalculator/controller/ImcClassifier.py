class ImcClassifier:
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
    

                     


#:(self, age: int)