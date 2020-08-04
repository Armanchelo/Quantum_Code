from random import randint

def select_sort(array):
    for i in range(len(array)):
        min_value = array[i]
        index = i
        for n in range(i, len(array)):
            if array[n] < min_value:
                min_value = array[n]
                index = n
        array[i], array[index] = array[index], array[i]
    return array