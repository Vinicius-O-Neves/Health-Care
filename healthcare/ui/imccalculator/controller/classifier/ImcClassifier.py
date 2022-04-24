from WomanClassifier import WomanClassifier
from ManClassifier import ManClassifier
from healthcare.resources.Strings import Strings


class ImcClassifier:

    @staticmethod
    def adult(imc: float) -> str:
        interval = {
            imc < 18.5: Strings().under_weight,
            18.5 <= imc <= 24.9: Strings().normal_weight,
            25 <= imc <= 29.9: Strings().pre_obesity,
            30 <= imc <= 34.9: Strings().obesity_gdr_1,
            35 <= imc <= 39.9: Strings().obesity_gdr_2,
            imc >= 40: Strings().obesity_gdr_3
        }

        return interval[True]

    @staticmethod
    def womanWith10To19(age: int, imc: float) -> str:
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
            pImc < 5: Strings().under_weight,
            5 <= pImc < 85: Strings().appropriate,
            pImc >= 85: Strings().over_weight
        }
        return percentile[True]

    @staticmethod
    def manWith10To19(age: int, imc: float) -> str:
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
            pImc < 5: Strings().under_weight,
            5 <= pImc < 85: Strings().appropriate,
            pImc >= 85: Strings().over_weight
        }
        return percentile[True]
