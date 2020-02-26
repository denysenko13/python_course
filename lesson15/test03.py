""" 
gen(count):
генерирует count случ. чисел
результат - словарь

ключ число
знач число в кубе
"""

import random

count = int(input("Enter int: "))

def gen_count(count):
    rand_dict = dict()
    for i in range(count):
        rand_key = random.randint(1,100)
        rand_dict[rand_key] = rand_key**3
    return rand_dict


print(gen_count(count))