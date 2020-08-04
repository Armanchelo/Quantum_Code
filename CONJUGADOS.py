def conjugar(palabra, tiempo):
    excepciones = ['estar']
    if palabra in excepciones: return 'ijoles'

    terminacion = palabra[-2:]
    palabra = palabra[:-2]

    if tiempo.startswith('pr'):
        ar = ['o', 'as', 'a', 'amos', 'ais', 'an', 'ando']
        er = ['o', 'es', 'e', 'emos', 'eis', 'en', 'iendo']
        ir = ['o', 'es', 'e', 'imos', 'ís', 'en', 'iendo']
    elif tiempo.startswith('pa'):
        ar = ['é', 'aste', 'ó', 'amos', 'asteis', 'aron', 'ando']
        er = ['í', 'iste', 'ió', 'imos', 'isteis', 'ieron', 'iendo']
        ir = er
    elif tiempo.startswith('fu'):
        ar = ['é', 'ás', 'á', 'emos', 'éis', 'án']
        er, ir = ar, ar
        palabra += terminacion
    conjugaciones = {'ar' : ar, 'er' : er, 'ir' : ir}
    terminaciones = conjugaciones[terminacion]

    conjugados = [palabra + conjugacion for conjugacion in terminaciones]
    
    return conjugados

tiempos = ['pasado', 'presente', 'futuro']

palabra = input('Palabra: ')
for tiempo in tiempos:
    print(conjugar(palabra, tiempo))
