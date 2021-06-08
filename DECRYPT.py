from random import choice, randint
from tqdm import tqdm
from math import ceil

printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
length = randint(3, 10)
password = ''.join([choice(printable) for _ in range(length)])

def add_index(indexes, add = True):
    if add:indexes[0] += 1
    else: indexes[0] -= 1
    for i in range(len(indexes)):
        try:
            if add:
                if indexes[i] == len(printable):
                    indexes[i] = 0
                    indexes[i + 1] += 1
            else:
                if indexes[i] == 0:
                    indexes[i] = len(printable) - 1
                    indexes[i + 1] -= 1
        except IndexError: 
            if add: indexes += [0]
            else: indexes += [len(printable) - 1]
            return indexes
    return indexes


def decrypt():  
    indexes = [0]
    end_indexes = [len(printable) - 1]
    for i in tqdm(range(len(printable) ** length // 2), desc=f"Decrypting..."):
    # for _ in range(len(printable) ** length // 2):
    # while True:
        current_string = ''.join([printable[i] for i in indexes])
        current_inverse_string = ''.join([printable[i] for i in end_indexes])
        if password == current_string: return current_string
        if password == current_inverse_string: return current_inverse_string
        indexes = add_index(indexes)
        end_indexes = add_index(end_indexes, add = False)
    return 'no se pudo carnal'
print('password: ', decrypt())



