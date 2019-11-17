"""
7. Сгенерировать случайную строку из 10 символов с помощью функции random.sample и константы string.ascii_letters
"""

import string, random

lst = list(string.ascii_letters)

print("".join(random.sample(lst,10)))
