"""
1. Отсортировать все атрибуты модуля string по алфавиту, в обратном порядке,
 вывести полученный список на печать.
"""
import string

s = string
l = dir(s)
l.sort(reverse=1)
print(l)