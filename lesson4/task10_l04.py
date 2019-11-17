"""
10. Написать скрипт, который генерирует список из 30 одинаковых элементов (случайное int число), 
затем на базе этого списка формирует новый, заменив каждый третий элемент исходного списка на число 1000. 
Вывести на печать исходный список и новый список.
"""

import random, string

lst = [random.randint(1,100)]*30
lst_new = lst[:]
lst_replace = [1000]*10
lst_new[2::3] = lst_replace[:]
print("Original list:",lst)
print("List of replaced every third elements:",lst_new)