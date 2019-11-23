"""
4. Открыть файл из п.3 в режиме чтения,
прочитать из него содержимое, 
распарсить ее в словарь вида
persons = {‘ross’: {информация про Роса в виде словаря}, ‘harry’: {информация про Гарри в виде словаря}}.
"""

with open('./persons.txt', 'r') as f:
    lines = f.readlines()

def parser (strng):
    name, age, salary, profession = strng.split(';')
    first_name, last_name = name.split()
    amount, currency = salary.split()
    person = dict(name=dict(first_name=first_name.capitalize(),last_name=last_name.capitalize()), age=int(age), profession=profession.strip(), salary=dict(amount=float(amount),currency=currency.upper()))
    return person

l1, l2 = lines
persons = dict(ross=parser(l2),harry=parser(l1))
print(persons)