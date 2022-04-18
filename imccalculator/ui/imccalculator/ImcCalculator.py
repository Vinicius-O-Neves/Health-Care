def imcCalculator(weight: int, height: float) -> int:
    imc = weight / (height ** 2)
    return round(imc, 1)
