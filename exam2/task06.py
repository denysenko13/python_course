"""
Написать скрипт, который содержит функцию get_random_list(n), 
которая генерирует список из n случайных целых чисел(n - параметр функции, по умолчанию - 11); 
функцию get_every_second(lst), которая в качестве параметра lst получает список, 
а в качестве результата возвращает список, который содержит каждый второй элемент списка lst. 
Функцию main(n), в которой происходит вызов функции get_random_list, 
\результат печатается и передается в функцию get_every_second, возвращаемый результат выводится на печать. 
В основном скрипте сделать вызов main с аргументами: main(10), main(), main(15).
"""

import random

def get_random_list(n=11):
    rand_lst = list()
    for i in range(n):
        rand_lst.append(random.randint(1, 100))
    return rand_lst

def get_every_second(lst):
    lst_every_second = lst[1::2]
    return lst_every_second

def main(n=11):
    lst_orig = get_random_list(n)
    print(lst_orig)
    lst_every_second = get_every_second(lst_orig)
    print(lst_every_second)

main(10)
main()
main(11)