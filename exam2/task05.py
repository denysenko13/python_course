"""
Написать функцию, которая получает в качестве аргумента список чисел, 
а в качестве результата - формирует словарь - где ключ - исходное число, 
а значение - квадрат числа. Реализовать вызов функции и печать результата. 
"""

import random

NUM = random.randint(1,10)
digit_lst = list()
for i in range(NUM):
    digit_lst.append(random.randint(1,100))

def gen_dict(lst = digit_lst):
    sqr_dict = dict()
    for elem in lst:
        sqr_dict[elem] = pow(elem, 2)
    return sqr_dict

res = gen_dict()
print(res)