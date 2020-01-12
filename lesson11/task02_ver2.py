"""
Распарсить файл с информацией о платежах, но использовать только те, где тип платежа out, 
также не все строки могут быть в корректном формате. Кто совершал больше всего покупок? 
На наибольшую сумму? Файл: https://drive.google.com/open?id=1mPTBA37SLpPbs_qftgZuGCm0JXcziW85 
"""

payments_file = "payments.txt"
dictionaries_list = list()
persons_dict = dict()
payments_dict = dict()

with open(payments_file) as file:
    for line in file:
        name, *other = line.split(";")
        if "out"  not in other:
            continue
        amount, currency = str(other[0]).split()
        if "," in amount:
            amount = amount.replace(",", ".")
        persons_dict = dict(name=name, amount=amount, currency=currency)
        dictionaries_list.append(persons_dict)

for i in dictionaries_list:
    person_name = i.get("name")
    payments_dict.update({person_name : []})

for i in dictionaries_list:
    person_name = i.get("name")
    amount = float(i.get("amount"))
    temp_list = payments_dict.get(person_name)
    temp_list.append(amount)

max_sum = 0
for k, v in payments_dict.items():
    if max(v) > max_sum:
        max_sum = sum(v)
    print(k, "Count of amount:", len(v))

print("Max sum:", max_sum)