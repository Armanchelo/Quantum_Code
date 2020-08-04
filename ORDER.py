def order(txt):
    aux = list(txt)
    aux.sort()
    if list(txt) == aux: return True
    return False