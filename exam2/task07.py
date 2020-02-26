"""
Есть словарь стран {"ua": "Ukraine", "ru": "Russia", "us": "USA", "uk": "United Kindom", "pl": "Poland", "es": "Spain"}. 
Необходимо написать функцию, которая в качестве аргумента принимает название страны, а возвращает - код страны. 
Если такая страна не найдена, функция кидает исключение. Реализовать два вызова функции - без ошибки и с ошибкой.
"""

DICT = {"ua": "Ukraine", "ru": "Russia", "us": "USA", "uk": "United Kindom", "pl": "Poland", "es": "Spain"}

def get_country_code(country):
    if country in DICT.values():
        for k, v in DICT.items():
            if country == v:
                return k
    else:
        raise Exception("Unknown country")

print(get_country_code("Russia"))
print(get_country_code("Rusia"))