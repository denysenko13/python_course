"""
Написать скрипт, который будет генерировать список туплов. Каждый тупл
содержит 3 элемента -- 3 случайных числа. После генерации списка,
отсортировать его, по убыванию второго элемента каждого тупла, вывести на
печать.
"""

import random

def generate_tuple():
    tpl = (random.randint(1,100),random.randint(1,100),random.randint(1,100))
    return tpl

def generate_list(count=5):
    # lst = list()
    lst = [()] * count
    for k in range(0,count):
        #lst.append(generate_tuple()) пришлось сменить реализацию генерации списка туплов, потому что линтер ругался на неипользуемую переменную k=(
        lst[k] = generate_tuple()
    return lst

def sort_list(lst):
    lst.sort(key=lambda elem: elem[1], reverse=1)
    return lst

print(sort_list(generate_list()))