"""
2. написать скрипт для генерации словаря для шифра Цезаря,
Выбрать шаг, например 3. Ключи - символы латинского алфавита, в нижнем регистре. Значения - тоже символы, соответствующие ключам согласно шифру.
То есть скрипт должен формировать словарь вида {‘a’: ‘d’, ‘b’: ‘e’, ‘c’: ‘f’, … , ‘z’: ‘c’ }
"""

import string
lowercase = string.ascii_lowercase
step = 3
lst_key = list(lowercase)
lst_value = lst_key[step:] + lst_key[:step]
cesar = dict(zip(lst_key, lst_value))
print(cesar)