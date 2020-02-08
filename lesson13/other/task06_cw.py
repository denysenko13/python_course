"""
Написать функцию, для инспектирования модуля. Вывести на печать все его
функции, вместе с doc-строкой. Для определения, является объект функцией,
воспользоваться встроенной функцией callable. Брать только те объекты,
имена которых начинаются с литеры, а не символа подчеркивания.
Выводить на печать в цикле, после каждого отображения ждать, пока
пользователь не нажмет Enter.
Вызвать функцию с модулем random, math.
"""
import math

def inspect(obj):
    attrs = dir(obj)
    for attr in attrs:
        if not attr.startswith("__") and callable(getattr(obj, attr)):
            print(getattr(obj, attr).__doc__)
            command = input()
            if command == "":
                continue
            else:
                break

inspect(math)


