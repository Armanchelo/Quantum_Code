def particiones(numero):
    posibilidades = []
    aux = [numero, 0]
    index = 0
    while aux.count(1) != numero:
        posibilidades += [[f'{digito}-' for digito in aux if digito > 0]]
        if aux[index] > 1:
            aux[index] -= 1
            aux[index + 1] += 1
        else:
            index += 1
            aux += [0]
    posibilidades += [['1-' for n in range(numero)]]
    posibilidades = [''.join(sorted(elemento, reverse = True)) for elemento in posibilidades]
    return set(posibilidades)

limite = int(input('Tu numero: '))
for n in range(1, limite + 1):
    posibilidades = particiones(n)
    print(n, len(posibilidades))