import math

def media(arr):
    return sum(arr) / len(arr)

def varianza(arr):
    m = media(arr)
    return sum((x - m) ** 2 for x in arr) / len(arr)

def desviacion_estandar(arr):
    return math.sqrt(varianza(arr))

#Funcion para obtener si un numero es primo
def es_primo(num):
    #Descarrta los numeros menores a 2 (0 y 1)
    if num < 2:
        return False
    for i in range(2, num -1): #Comprueba que no haya otro divisor que no sea 1 o el mismo numero
        if num % i == 0:
            return False
    return True

# Funcion para obtener los primeros 500 numeros primos
def primos(n):
    primos = []
    num = 2
    while len(primos) < n:
        if es_primo(num):
            primos.append(num)
        num += 1
    return primos

primos = primos(500)
print("Primos:", primos)
print("Media:", media(primos))
print("Varianza:", varianza(primos))
print("Desviacion Estandar:", desviacion_estandar(primos))