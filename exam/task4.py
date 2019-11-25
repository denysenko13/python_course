"""
4. Необходимо распрасить информацию о продукте из файла products.txt в словарь вида. 
{«name»: str, «produced»: {«country»: str, «city»: str}, min_price: {currency, amount}, max_price: {currency, amount} }
Валюта currency в результирующем словаре должна быть числовым кодом, согласно соответствию curr_ codes = {«uah»: 980, «rub»: 643}

Milky Way; Ukraine, Kiev; 34.4556 uah; 56.4567 Uah
"""

with open('./products.txt', 'r') as f:
    line = f.readline()

curr_codes ={"uah": 980, "rub": 643}
name, produced, min_price, max_price= line.split(';')
country, city = produced.split()
min_cur, min_am = min_price.split()
max_cur, max_am = max_price.split()
info = info = dict(name=name,produced=dict(country=country,city=city),
                   min_price=dict(currency=float(min_cur),amount=curr_codes.get(min_am.lower())),max_price=dict(currency=float(max_cur),amount=curr_codes.get(max_am.lower())))
print(info)