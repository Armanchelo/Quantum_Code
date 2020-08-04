factorial_cache = {}
def factorial(n):
    try:
        try:
            if n in factorial_cache:
                return factorial_cache[n]
            else:
                if n == 1: return n
                elif n > 1:
                    resultado = n * factorial(n - 1) 
                    factorial_cache[n] = resultado
                    return resultado
        except RecursionError: pass
    except TypeError: pass 

print(factorial(1000))