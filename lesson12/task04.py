"""
4. Задание с парсингом файла с платежами, переписать с помощью функций. 
Сделать имя файла значением по умолчанию. А также учитывать актуальную валюту, приводить все к USD. 
То есть если сумма в файле в евро, то пересчитать ее в доллар по курсу 1.11. 
И найти кто тратил больше всех по разным показателям, как было в задании.

Распарсить файл с информацией о платежах, но использовать только те, где тип платежа out, 
также не все строки могут быть в корректном формате. Кто совершал больше всего покупок? 
На наибольшую сумму?
"""

PAYMENTS_FILE = "payments.txt"


def create_list(file=PAYMENTS_FILE):
    dictionaries_list = list()
    persons_dict = dict()
    
    with open(file) as f:
        for line in f:
            name, *other = line.split(";")
            if "out"  not in other:
                continue
            amount, currency = str(other[0]).split()
            if "," in amount:
                amount = amount.replace(",", ".")
            if currency == "EUR":
                amount = float(amount) * 1.11
                currency = "USD"
            persons_dict = dict(name=name, amount=amount, currency=currency)
            dictionaries_list.append(persons_dict)
    
    return dictionaries_list


def create_dict(dictionaries_list):
    payments_dict = dict()

    for i in dictionaries_list:
        person_name = i.get("name")
        payments_dict.update({person_name : []})

    for i in dictionaries_list:
        person_name = i.get("name")
        amount = float(i.get("amount"))
        temp_list = payments_dict.get(person_name)
        temp_list.append(amount)
    
    return payments_dict


def max_amount(payments_dict):
    max_amount = 0
    name = ""

    for k, v in payments_dict.items():
        if max(v) > max_amount:
            max_amount = max(v)
            name = k

    return {name:max_amount}


def max_sum(payments_dict):
    max_sum = 0
    name = ""

    for k, v in payments_dict.items():
        if sum(v) > max_sum:
            max_sum = sum(v)
            name = k

    return {name:max_sum} 


def count(payments_dict):
    count_dict = dict()

    for k, v in payments_dict.items():
        count_dict.update({k:len(v)})
    
    return(count_dict)


print(max_amount(create_dict(create_list())))
print(max_sum(create_dict(create_list())))
print(count(create_dict(create_list())))