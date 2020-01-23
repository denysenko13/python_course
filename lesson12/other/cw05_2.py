"""
Реализуйте функцию generate, которая будет генерировать случайное число
и выводить его на печать, просить пользователя ввести строку. Функция
должна вызываться в глобальном цикле, пока пользователь не введёт пустую
строку. Реализовать с помощью механизма глобальных переменных, для
этого определить need_stop = False глобальную переменную.
"""

import random

need_stop = False

def generate():
    print(random.randint(1,1000))
    global need_stop
    need_stop = input("Enter some text for Stop: ")

while not need_stop:
    generate()