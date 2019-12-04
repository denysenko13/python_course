"""
Распарсить файл с информацией о плательщиках в список словарей вида {name: str, amount: float, currency: int}, вывести на печать полученный список.
Содержимое файла:
Remus Lupin;329.76 USD;2018-08-20 19:36:32;out;
Severus Snape;397 USD;2018-08-20 20:22:26;out;
Lucius Malfoy;847.44 USD;2018-08-20 22:51:55;out;
Ron Weasley;929.93 USD;2018-08-20 19:33:58;out;
Sirius Black;573.58 USD;2018-08-20 06:47:05;out;
Harry Potter;930.93 USD;2018-08-20 18:08:20;out;
"""

persons_file = "persons_lesson9.txt"
persons_dict = dict()
dictionaries_list = list()

with open(persons_file) as file:
    for line in file:
        name, salary, *others = line.split(';')
        amount, currency = salary.split()
        persons_dict = dict(name=name, amount=amount, currency=currency)
        dictionaries_list.append(persons_dict)

for i in dictionaries_list:
    print(i)