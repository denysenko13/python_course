"""
Написать функцию без аргумента, которая генерирует 3 случайных числа, 
упорядоченных в порядке возрастания. 
Реализовать вызов функции и печать результата.
"""

import random

def random_digits():
    rand_lst = [0]*3
    for i in range(3):
        rand_lst[i] = random.randint(1, 100)
    rand_lst.sort()
    return rand_lst

lst = random_digits()
for elem in lst:
    print(elem)