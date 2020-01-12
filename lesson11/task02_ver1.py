"""
Распарсить файл с информацией о платежах, но использовать только те, где тип платежа out, 
также не все строки могут быть в корректном формате. Кто совершал больше всего покупок? 
На наибольшую сумму? Файл: https://drive.google.com/open?id=1mPTBA37SLpPbs_qftgZuGCm0JXcziW85 
"""
"""
Lucius Malfoy;847,44 USD;2018-08-20 22:51:55;out;
Ron Weasley;929.93 USD;2018-08-20 19:33:58;out;
Sirius Black;573.58 USD;2018-08-20 06:47:05
Harry Potter;930.93 USD;2018-08-20 18:08:20;out;
Lucius Malfoy;482.13 USD;2018-08-20 21:08:27;in;
Ginny Weasley;658.85 USD;2018-08-2
Chandler Bing;254 USD;2018-08-20 23:07:26;out;
Remus Lupin;276 USD;2018-08-20 10:19:56;out;
Molly Weasley;454 USD;2018-08-20 08:22:20;
Bellatrix Lestrange;995.82 USD;2018-08-20 10:46:19;out;
Phoebe Buffay;474.21 USD;2018-08-20 22:35:23;out;
Chandler Bing;252,5 USD
Joseph Tribbiani;34 USD;2018-08-20 08:28:35;in;
"""
import re

payments_file = "payments.txt"
amount_regexp = re.compile(r'([;]\d{1,}[.]\d{1,2}[ ]|[;]\d{1,}[ ])')
dictionaries_list = list()
persons_dict = dict()
payments_dict = dict()

with open(payments_file) as file:
    for line in file:
        try:
            amount_exist = amount_regexp.search(line)
            if amount_exist.group() in line:
                name, *other = line.split(";")
                if "out" in other:
                    amount, currency = str(other[0]).split()
                    persons_dict = dict(name=name, amount=amount, currency=currency)
                    dictionaries_list.append(persons_dict)
        except:
            pass

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