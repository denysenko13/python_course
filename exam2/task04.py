"""
Написать функцию, которая получает в качестве аргумента список чисел, 
а в качестве результата - формирует список квадратов этих чисел. 
Реализовать вызов функции и печать результата. 
"""

import random

NUM = random.randint(1,10)
digit_lst = list()
for i in range(NUM):
    digit_lst.append(random.randint(1,100))

def square(lst=digit_lst):
    sqr_lst = list()
    for elem in lst:
        sqr_lst.append(pow(elem,2))
    return sqr_lst

res = square()
for elem in res:
    print(elem)