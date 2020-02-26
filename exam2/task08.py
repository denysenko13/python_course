"""
Написать скрипт парсинга файла с информацией о балансах пользователей 
https://drive.google.com/open?id=1iItMYUF0Uwb-qB0epNTLRnJpKRU6joGV . 
Подготовить отсортированную информацию (должна содержать и баланс, и аккаунт пользователя), 
упорядоченную в порядке убывания балансов. Сохранить упорядоченную информацию в новый файл, 
sorted_balances.txt (в таком же формате как и исходный файл).

225271628159;3483.76
547852564604;45004.72
257301126284;18034.32
316447516734;13533.64
562606474869;2407.85
"""

BAL_FILE = './balances.txt'
SORT_BAL_FILE = './sorted_balances.txt'

def create_list(file=BAL_FILE):
    date_dict = dict()
    with open(file) as f:
        for line in f:
            acc, bal = line.split(';')
            date_dict[acc] = float(bal)
        return date_dict

def create_file(dct, file=SORT_BAL_FILE):
    lst = list(dct.items())
    lst.sort(key=lambda elem: elem[1], reverse=1)
    with open(file, 'w') as f:
        for elem in lst:
            f.write(f"{elem[0]};{elem[1]}\n")




dct = create_list()
create_file(dct)