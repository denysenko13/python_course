"""
3. Сделать парсинг файла логов сервера, подготовить информацию в разрезе ip - в какое время с каждого ip были зафиксированы запросы. 
(Подсказка - на выходе - словарь, ключ - ip,  значение - список времен)
"""
"""
127.0.0.1 2018-07-25 11:30:43.211382 [WARN] - AppLog: Using old request format
192.168.0.1 2018-07-25 11:30:44.216197 [WARN] - AppLog: Some data will be ignored
192.168.0.2 2018-07-25 11:30:47.218422 [INFO] - AppLog: Data got successfully
"""

import re

unfiltered_file = "app.log"
ipv4_regexp = re.compile(r'((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)')
ip_dict = dict()
date_list = list()

with open(unfiltered_file, "r") as file:
    for line in file:
        ip, date, time, *info = line.split()
        datetime = date + ' ' + time
        ipv4 = ipv4_regexp.search(ip)
        date_list.append(ipv4.group() + ';' + datetime)
        ip_dict.update({ipv4.group():[]})

for i in date_list:
    test = list()
    ip, datetime, *others = i.split(';')
    ipv4 = ipv4_regexp.search(ip)
    if ipv4.group() in ip_dict:
        test = ip_dict.get(ipv4.group())
        test.append(datetime)
        ip_dict[ipv4.group()] = test

for k,v in ip_dict.items():
    print(k, v)

"""
Регулярные выражения добавил, чтобы точно вытягивать IP.
Сама реализация думаю не оптимальная. 
Предполагаю что можно было обойтись без промежуточного шага формирования списка IP + datetime и апдейтить значение ключа в первом цикле, 
но как это сделать я не додумался=(
"""