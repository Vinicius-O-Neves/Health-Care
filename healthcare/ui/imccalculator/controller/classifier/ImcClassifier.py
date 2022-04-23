from WomanClassifier import WomanClassifier
from ManClassifier import ManClassifier

class ImcClassifier:

    def adult(self, imc: int) -> str:
        interval = {
            imc < 18.5: "Abaixo do Peso",
            18.5 <= imc <= 24.9: "Peso Normal",
            25 <= imc <= 29.9: "Pré-Obesidade",
            30 <= imc <= 34.9: "Obesidade Grau 1",
            35 <= imc <= 39.9: "Obesidade Grau 2",
            imc >= 40: "Obesidade Grau 3" 
        }

        return interval[True]

    def womanWith10To19(self, age: int, imc: int) -> str:
        womanClassifier = WomanClassifier(imc)
        interval = {
            age == 10: womanClassifier.womanWith10(),
            age == 11: womanClassifier.womanWith11(),
            age == 12: womanClassifier.womanWith12(),
            age == 13: womanClassifier.womanWith13(),
            age == 14: womanClassifier.womanWith14(),
            age == 15: womanClassifier.womanWith15(),
            age == 16: womanClassifier.womanWith16(),
            age == 17: womanClassifier.womanWith17(),
            age == 18: womanClassifier.womanWith18(),
            age == 19: womanClassifier.womanWith19()
        }
        
        pImc = interval[True]
        percentile = {
            pImc < 5: "Abaixo do Peso",
            5 <= pImc < 85: "Adequado(a)",
            pImc >= 85: "Sobrepeso"
        }
        return percentile[True]

    def manWith10To19(self, age: int, imc: int) -> str:
        manClassifier = ManClassifier(imc)
        interval = {
            age == 10: manClassifier.manWith10(),
            age == 11: manClassifier.manWith11(),
            age == 12: manClassifier.manWith12(),
            age == 13: manClassifier.manWith13(),
            age == 14: manClassifier.manWith14(),
            age == 15: manClassifier.manWith15(),
            age == 16: manClassifier.manWith16(),
            age == 17: manClassifier.manWith17(),
            age == 18: manClassifier.manWith18(),
            age == 19: manClassifier.manWith19()
        }
        
        pImc = interval[True]
        percentile = {
            pImc < 5: "Abaixo do Peso",
            5 <= pImc < 85: "Adequado(a)",
            pImc >= 85: "Sobrepeso"
        }
        return percentile[True]