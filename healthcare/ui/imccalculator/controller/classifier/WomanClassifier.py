class WomanClassifier:
    
    def __init__(self, imc: int):
        self.imc = imc
        
    def womanWith10(self) -> int:
        interval = {
            14.23 >= self.imc <= 15.09: 5,
            15.09 >= self.imc <= 17.00: 15,
            17.00 >= self.imc <= 20.19: 50,
            20.19 >= self.imc <= 23.20: 85,
            self.imc >= 23.20: 95
    }
        return interval[True]

    def womanWith11(self) -> int:
        interval = {
            14.60 >= self.imc <= 15.53: 5,
            15.53 >= self.imc <= 17.67: 15,
            17.67 >= self.imc <= 21.18: 50,
            21.18 >= self.imc <= 24.59: 85,
            self.imc >= 24.59: 95
        }
        return interval[True]

    def womanWith12(self) -> int:
        interval = {
            14.98 >= self.imc <= 15.98: 5,
            15.98 >= self.imc <= 18.35: 15,
            18.35 >= self.imc <= 22.17: 50,
            22.17 >= self.imc <= 25.95: 85,
            self.imc >= 25.95: 95
        }
        return interval[True] 
            
    def womanWith13 (self) -> int:
        interval = { 
            15.36 >= self.imc <= 16.43: 5,
            16.43 >= self.imc <= 18.95: 15,
            18.95 >= self.imc <= 23.08: 50,
            23.08 >= self.imc <= 27.07: 85,
            self.imc >= 27.07: 95
        }
        return interval[True]                    
    
    def womanWith14(self) -> int:
        interval = {
            15.67 >= self.imc <= 16.79: 5,
            16.79 >= self.imc <= 19.32: 15,
            19.32 >= self.imc <= 23.88: 50,
            23.88 >= self.imc <= 27.97: 85,
            self.imc >= 27.97: 95
        }
        return interval[True]

    def womanWith15(self) -> int:
        interval = {    
            16.01 <= self.imc <= 17.16: 5,
            17.16 <= self.imc <= 19.69: 15,
            19.69 <= self.imc <= 24.29: 50,
            24.29 <= self.imc <= 28.51: 85,
            self.imc >= 28.51: 95
        }
        return interval[True]

    def womanWith16(self) -> int:
        interval = {
            16.37 <= self.imc <= 17.54: 5,
            17.54 <= self.imc <= 20.09: 15,
            20.09 <= self.imc <= 24.74: 50,
            24.74 <= self.imc <= 29.10: 85,
            self.imc >= 29.10: 95
        }
        return interval[True]

    def womanWith17(self) -> int:
        interval = {
            16.59 >= self.imc <= 17.81: 5,
            17.81 >= self.imc <= 20.36: 15,
            20.36 >= self.imc <= 25.23: 50,
            25.23 >= self.imc <= 29.72: 85,
            self.imc >= 29.72: 95
        }
        return interval[True]

    def womanWith18(self) -> int:
        interval = {
            16.71 >= self.imc <= 17.99: 5,
            17.99 >= self.imc <= 20.57: 15,
            20.57 >= self.imc <= 25.56: 50,
            25.56 >= self.imc <= 30.22: 85,
            self.imc >= 30.22: 95
        }
        return interval[True]

    def womanWith19(self) -> int:
        interval = {
            16.87 >= self.imc <= 18.20: 5,
            18.20 >= self.imc <= 20.80: 15,
            20.80 >= self.imc <= 25.85: 50,
            25.85 >= self.imc <= 30.72: 85,
            self.imc >= 30.72: 95
        }
        return interval[True]
            
            