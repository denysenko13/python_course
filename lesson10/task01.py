"""
1. Попросить пользователя ввести строку и зашифровать ее шифром Цезаря со сдвигом 4. 
Если пользователь вводит пустую строку (то есть просто нажимает Enter или один символ, то просить его вводить строку пока не введет минимум 2 символа). 
Код для реализации шифра Цезаря, могу скинуть кому нужно
"""

import string
lowercase = string.ascii_lowercase
step = 4
lst_key = list(lowercase)
lst_value = lst_key[step:] + lst_key[:step]
cesar = dict(zip(lst_key, lst_value))
print(cesar)

plain = ""
while len(plain) < 2:
    plain = input("Enter some text: ")

encrypted = ""    
for i in plain:
    encrypted += cesar.get(i)

print("Encrypted text:", encrypted)