"""
9. Написать скрипт, который генерирует случайные пароли случайной длины, 
не меньше 10 и не больше 20 элементов,  
из символов - букв латинского алфавита в верхнем и нижнем регистре, цифр.
"""

import string, random

char = list(string.ascii_letters) + list(string.digits)
length = random.randint(10, 20)
pwd = random.sample(char, length)
print("Random password:","".join(pwd))