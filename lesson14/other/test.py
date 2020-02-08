"""
Написать скрипт, в котором пользователю предлагается ввести целое число,
а также ввести, в каком представлении это число будет отображено (hex, bin,
oct). Ввод числа и проверку введенных данных реализовать в функции
get_number, которая возвращает число, ввод типа представления и проверка
- в функции get_presentation, которая возвращает функцию, одну из (hex, bin,
oct). Если пользователь ввел некорректные значения, завершать работу
скрипта исключением.
def get_number(): pass
def get_presentation(): pass
number = get_number(); presentation = get_presentation()
print(presentation(number))
"""

def get_number():
    num = input("Enter number: ")
    if not num.isdecimal():
        raise Exception("Not number: ")
    return int(num)
    

def get_presentation():
    pres = input("Enter hex, bin or oct: ")
    if not pres in ("hex", "bin", "oct"):
        raise Exception("Wrong type")
    return getattr(__builtins__, pres)

number = get_number()
presentation = get_presentation()
print(presentation(number))