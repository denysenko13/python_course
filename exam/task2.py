"""
2. Сгенерировать список из 4х случайных 2х-значных чисел. 
Сформировать еще два списка - отсортированный исходный в прямом и обратном порядке. 
Вывести на печать все три списка. 
"""

import random

l1 = [random.randint(10,99),random.randint(10,99),random.randint(10,99),random.randint(10,99)]
l2 = list(l1)
l3 = list(l1)
l2.sort(reverse=0)
l3.sort(reverse=1)
print("Original random list:",l1)
print("ASC:",l2)
print("DESC:",l3)
