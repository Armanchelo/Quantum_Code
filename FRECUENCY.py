lista_de_numeros = [6, 3, 2, 3, 4, 3, 4, 4, 2, 1, 4, 5, 4, 2, 3, 3, 4, 4, 5, 4, 0, 3, 2, 4, 3, 4, 2, 3, 1, 2, 4, 4, 3, 4, 2, 4, 0, 3, 2, 3, 1, 2, 4, 1, 2, 3, 5, 3]
lista_de_numeros_sin_repetir = sorted(list(set(lista_de_numeros)))
total = len(lista_de_numeros)

frecuencias = [lista_de_numeros.count(numero) for numero in lista_de_numeros_sin_repetir]
frecuencias_acumuladas = [frecuencias[0]]
for i in range(len(frecuencias) - 1):
    frecuencias_acumuladas.append(frecuencias_acumuladas[i] + frecuencias[i + 1])

frecuencias_relativas = [round(frecuencia / total, ndigits = 2) for frecuencia in frecuencias]
frecuencias_relativas_acumuladas = [round(frecuencia / total, ndigits = 2) for frecuencia in frecuencias_acumuladas]
frecuencias_porcentuales = [f'{round(frecuencia * 100, ndigits = 2)}%' for frecuencia in frecuencias_relativas]
frecuencias_porcentuales_acumuladas = [f'{round(frecuencia * 100, ndigits = 2)}%' for frecuencia in frecuencias_relativas_acumuladas]

print('frecuencias:', frecuencias)
print('frecuencias acumuladas: ', frecuencias_acumuladas)
print('frecuencias relativas: ', frecuencias_relativas)
print('frecuencias relativas acumuladas: ', frecuencias_relativas_acumuladas)
print('frecuencias porcentuales: ', frecuencias_porcentuales)
print('frecuencias porcentuales acumuladas: ', frecuencias_porcentuales_acumuladas)
print(total)

rangos = [0, 0.5, 1, 1.5, 2]
numeros = [numero / 100 for numero in range(200)]
intervalos = []
for i in range(len(rangos)):
    intervalo = []
    for numero in numeros:
        if numero >= rangos[i] and numero < rangos[i + 1]:
            intervalo += [numero]
    intervalos += [intervalo]

for intervalo in intervalos:
    print(intervalo)

