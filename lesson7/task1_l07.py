
"""
1. дописать скрипт парсинга информации о человеке, который начали делать на уроке
“harry potter; 30; 127.45 galeon; auror”
“ross geller; 34; 6500.45 usd; paleontologist”
Необходимо распарсить строку(выбрать одну) и сохранить в словарь информацию о персоне. 
Для хранения имени, использовать вложенный словарь с ключами first_name, last_name. 
Для хранения информации о зарплате использовать словарь с ключами - amount и currency.
На выходе должен быть словарь вида:
{'name': {'first_name': 'Harry', 'last_name': 'Potter'}, 'age': 30, 'profession': 'auror', 'salary': {'amount': 127.45, 'currency': 'galeon'}}
Те, кто сделал на уроке, сделайте дома красиво, с множественным присваиванием с минимальным количеством строк кода без потери читабельности ) 
Не забывайте, что числовые строки - приводить к числовым типам - возраст, зп.
"""

l = ["harry potter; 30; 127.45 galeon; auror","ross geller; 34; 6500.45 usd; paleontologist"]
l1,l2 = l

# функции не учили еще, но я ее написал еще на уроке, пусть остается=)
def parser (strng):
    name, age, salary, profession = strng.split(';')
    first_name, last_name = name.split()
    amount, currency = salary.split()
    person = dict(name=dict(first_name=first_name.capitalize(),last_name=last_name.capitalize()), age=int(age), profession=profession.strip(), salary=dict(amount=float(amount),currency=currency.upper()))
    print(person)

parser(l1)
parser(l2)