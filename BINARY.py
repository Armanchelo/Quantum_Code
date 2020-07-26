from time import sleep
from FIBO import fibonacci1

def binary_search(lista, busqueda):
    min, max = 0, len(lista) - 1
    lastmin, lastmax = 0, 0
    while max > min:
        indice = round((min + max) / 2)
        print(min, max, indice, lista[indice])
        if lista[indice] == busqueda: return indice
        else:
            if lista[indice] < busqueda: min = indice + 1
            elif lista[indice] > busqueda: max = indice - 1
    return -1 

size = 100
numbers = [n for n in range(1, size)]
fibo = list(map(fibonacci1, numbers))
# print(binary_search(fibo, 8))
print(fibo)