"""
1 Написать функцию с тремя параметрами которая возвращает минимальное значение из переданных. 
Реализовать два варианта вызова функции с печатью результатов.
"""


def min_elem(elem1, elem2, elem3):
    return min(int(elem1), int(elem2), int(elem3))

print(min_elem(3, 100, -5))
print(min_elem(1000, 1001, 999))