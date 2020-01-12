"""
Написать скрипт, осуществляющий шифрование фразы, введенной пользователем, по методу из ДЗ-3, задание 5 
(после каждой буквы исходной фразы, добавлять определенное число случайных символов, букв латинского алфавита. 
Чтобы скрыть первую букву, добавили и перед ней такое же количество случайных символов. 
Ваши специалисты узнали, что это число - 10).Проверять, что шифрование отрабатывает верно (как делали в ДЗ3-5).
"""

import string, random

lst = list(string.ascii_letters)
plain_text = input("Enter some text: ")
encrypted_text = ""
for e in plain_text:
    encrypted_text += "".join(random.choices(lst, k=10)) + e

print("Plain text:", plain_text)
print("Encrypted text:", encrypted_text)
print("Decrypted text:", encrypted_text[10::11])