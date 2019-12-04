"""
4. написать скрипт, который предлагает пользователю ввести число, 
проверяет, если пользователь ввел символы, отличные от цифр (вспомнить подходящие методы строк) - то генерирует случайное число, 
пишет, что число сгенерировано. Выводит на печать число(сгенерированное или введенное) и его квадрат
"""

import string, random

num = input("Enter some number: ")
digits_list = tuple(string.digits)

# if num in digits_list:
#     print("yes")
# else: 
#     print("no")
print(num)
print(digits_list)
if num in digits_list:
    print("ha")