"""
Реализовать поиск информации в словаре, но не по ключу, а по значению.
Словарь валют сформировать согласно Вики
Предусмотреть вариант, что искомый элемент не будет найден.
Печатать найденный элемент или сообщение о том, что не найден.
"""

currencies_file = "currencies_list.csv"
currencies_dict = dict()

with open(currencies_file) as file:
    for line in file:
        currency_name, currency_id, *other = line.split(",")
        currency_id=int(currency_id.rstrip())
        currencies_dict.update({currency_id:currency_name})

currency_value = input("Enter currency name: ").upper()
search = ""

for k,v in currencies_dict.items():
    if v == currency_value:
        search = v
        print(k,v)
        break

if search == "":
    print("Not found")

