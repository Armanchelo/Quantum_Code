from math import factorial

n = int(input('Numeros casos: '))
p = float(input('Probabilidad de exito (en decimal): '))
q = 1 - p
rng = input('Rango (separado con -): ')
rng = rng.split('-')
if len(rng) == 1: rng.insert(0, rng[0])
a, b = rng
rng = range(int(a), int(b) + 1)

def C(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))

final = 0
for x in rng:
    y = int(x)
    result = C(n, y) * (p ** y) * (q ** (n - y))
    print(f'P(X = {y}) = {C(n, y)}({p}^{y})({q}^{n - y})')
    print(result)
    print(f'{round(result * 100, ndigits = 2)}%')
    final += result
print(f'result: {round(final * 100, ndigits = 2)}%')
