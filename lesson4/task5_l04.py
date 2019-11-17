"""
5. Сформировать список из трех случайных трехзначных чисел, 
вывести на печать полученный список, отсортированный в прямом и обратном порядке.
"""

from random import randint

l = [randint(100,999),randint(100,999),randint(100,999)]
asc = list(l)
desc = list(l)
asc.sort()
desc.sort(reverse=1)
print("ASC:",asc)
print("DESC:",desc)