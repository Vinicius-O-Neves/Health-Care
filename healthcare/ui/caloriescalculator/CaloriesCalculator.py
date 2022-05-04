#Guarda as calorias recebidas num vetor
def caloriesStorage(cal):
    return arr.append(int(cal.split("-")[2].replace("cal", "")))

#Soma as calorias do array recebido  
def addCalories(arr):
    sumOfElements = 0
    for i in range(len(arr)):
        sumOfElements  = sumOfElements  + arr[i]
    return sumOfElements
arr = []

