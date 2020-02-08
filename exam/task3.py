"""
3. Зашифровать слово hello шифром Цезаря со сдвигом 4. (* и расшифровать зашифрованное, проверить).
"""

import string
lowercase = string.ascii_lowercase
step = 4
lst_key = list(lowercase)
lst_value = lst_key[step:] + lst_key[:step]
cesar = dict(zip(lst_key, lst_value))
rcesar = {}

orig = 'hello'
encrypted = ''
decrypted = ''
# for i in range(len(orig)):
#     encrypted += cesar.get(orig[i])
for letter in orig: 
    encrypted += cesar.get(letter, letter)


# тут можно было сформировать 2 листа с помощью values(), keys()
for key, value in cesar.items():
    rcesar[value] = key

for i in range(len(encrypted)):
    decrypted += rcesar.get(encrypted[i])

print("Encrypted:",encrypted,"Decrypted:",decrypted)