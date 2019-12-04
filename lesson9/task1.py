"""
Сгенерировать список из 10 случайных чисел. Вывести на печать. Упорядочить в порядке возрастания. Вывести на печать отсортированный список.
"""

from random import randint

lst = list()

for i in range(0,10):
    lst.append(randint(1,100))

print("Original list:")
for i in lst:
    print(i)

lst.sort()
print("Sorted list:")
for i in lst:
    print(i)