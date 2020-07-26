from random import randint

letras = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

def generar_codigo():
    letras_usables = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]
    diccionario = {}
    CodigoNuevo = ''
    for n in range(len(letras)):
        index = randint(0, len(letras_usables) - 1)
        diccionario[letras[n]] = letras_usables[index]
        letras_usables.pop(index)
    diccionario[' '] = ' '
    for n in diccionario.values():
        CodigoNuevo += n
    return diccionario, CodigoNuevo

diccionario, codigo = generar_codigo()

def encriptar(palabra, codigo):
    traduccion = ''
    for n in range(len(palabra)):
        traduccion += codigo[palabra[n]]
    return traduccion

def traduccion(palabra, codigo):
    nuevoDiccionario = {}
    for n in range(len(letras)):
        nuevoDiccionario[codigo[n]] = letras[n]
    nuevoDiccionario[' '] = ' '
    return encriptar(palabra, nuevoDiccionario)

palabra = 'voy a llorar con anely'
print(palabra)
print(codigo)
print(encriptar(palabra, diccionario))
print(traduccion(encriptar(palabra, diccionario), codigo))