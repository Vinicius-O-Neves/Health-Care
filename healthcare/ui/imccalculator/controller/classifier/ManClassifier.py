class ManClassifier:
    
    def __init__(self, imc: int):
        self.imc = imc

    def manWith10(self) -> int:
        interval = {
            14.42 >= self.imc <= 15.15: 5,
            15.15 >= self.imc <= 16.72: 15,
            16.72 >= self.imc <= 19.60: 50,
            19.60 >= self.imc <= 22.60: 85,
            self.imc >= 22.60: 95
        }
        return interval[True]

    def manWith11(self) -> int:
        interval = {
            14.83 >= self.imc <= 15.59: 5,
            15.59 >= self.imc <= 17.28: 15,
            17.28 >= self.imc <= 20.35: 50,
            20.35 >= self.imc <= 23.70: 85,
            self.imc >= 23.70: 95
        }
        return interval[True]

    def manWith12(self) -> int:
        interval = {
            15.24 >= self.imc <= 16.06: 5,
            16.06 >= self.imc <= 17.87: 15,
            17.87 >= self.imc <= 21.12: 50,
            21.12 >= self.imc <= 24.89: 85,
            self.imc >= 24.89: 95         
        }
        return interval[True]

    def manWith13(self) -> int:
        interval = {
            15.73 >= self.imc <= 16.62: 5,
            16.62 >= self.imc <= 18.53: 15,
            18.53 >= self.imc <= 21.93: 50,
            21.93 >= self.imc <= 25.93: 85,
            self.imc >= 25.93: 95
        }
        return interval[True]

    def manWith14(self) -> int:
        interval = {
            16.18 >= self.imc <= 17.20: 5,
            17.20 >= self.imc <= 19.22: 15,
            19.22 >= self.imc <= 22.77: 50,
            22.77 >= self.imc <= 26.93: 85,
            self.imc >= 26.93: 95
        }
        return interval[True]

    def manWith15(self) -> int:
        interval = {
            16.59 >= self.imc <= 17.76: 5,
            17.76 >= self.imc <= 19.92: 15,
            19.92 >= self.imc <= 23.63: 50,
            23.63 >= self.imc <= 27.76: 85,
            self.imc >= 27.76: 95
        }
        return interval[True]

    def manWith16(self) -> int:
        interval = {
            17.01 >= self.imc <= 18.32: 5,
            18.32 >= self.imc <= 20.63: 15,
            20.63 >= self.imc <= 24.45: 50,
            24.45 >= self.imc <= 28.53: 85,
            self.imc >= 28.53: 95 
        }
        return interval[True]

    def manWith17(self) -> int:
        interval = {
            17.31 >= self.imc <= 18.36: 5,
            18.36 >= self.imc <= 21.12: 15,
            21.12 >= self.imc <= 25.28: 50,
            25.28 >= self.imc <= 29.32: 85,
            self.imc >= 29.32: 95
        }
        return interval[True]

    def manWith18(self) -> int:
        interval = {
            17.54 >= self.imc <= 18.89: 5,
            18.89 >= self.imc <= 21.45: 15,
            21.45 >= self.imc <= 25.95: 50,
            25.95 >= self.imc <= 30.02: 85,
            self.imc >= 30.02: 95
        }
        return interval[True]

    def manWith19(self) -> int:
        interval = {
            17.80 >= self.imc <= 19.20: 5,
            19.20 >= self.imc <= 21.86: 15,
            21.86 >= self.imc <= 26.36: 50,
            26.36 >= self.imc <= 30.66: 85,
            self.imc >= 30.66: 95
        }
        return interval[True]