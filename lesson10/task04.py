"""
4. Написать игру Угадай число. Скрипт генерирует случайное целое число, диапазон на выбор разработчика. 
Пользователю предлагается вводить числа. Если угадал, то выход с отображением надписи - Поздравляю! 
Если не угадал, отображать подсказку, больше или меньше введенное число искомого.
"""

from random import randint

secret = randint(1, 20)

num = 0

while secret != num:
    num = int(input("Enter some number from 1 to 20: "))
    if num == secret:
        print("Congratulations!")
        break
    elif num > secret:
        print("Your number is more than secret")
    elif num < secret:
        print("Your number is less than secret")