def is_palindrome1(word):
    if len(word) < 2: return True
    if word[0] == word[len(word) - 1]: 
        return is_palindrome(word[1 : len(word) - 1])
    else: return False

def is_palindrome(word):
    word = word.replace(' ', '')
    for n in range(int(len(word))):
        if word[n] != word[-1 -n]: return False
    return True

def is_palindrome(num):
    string = f'{num}'
    for l in range(int(len(string) / 2)):
        if string[l] != string[-l -1]: return False
    return True

def closest_palindrome(num):
    if is_palindrome(num): return num
    else:
        aux1, aux2 = num - 1, num + 1
        while True:
            if is_palindrome(aux1): return aux1
            if is_palindrome(aux2): return aux2
            aux1 -= 1
            aux2 += 1

print(is_palindrome('anita lava la tina'))