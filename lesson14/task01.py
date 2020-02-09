"""
1. Написать скрипт для Парсинга файла логов, для получения информации об ошибках.  
Ошибкой считать запись в файле логов, если в качестве уровня логирования указан [ERROR]. 
Данные об ошибках должны быть сохранена в новый файл, errors.log, 
в нем должна быть следующая информация: ip адрес, с которого пришел запрос, дата и время ошибки, текст ошибки. 
Файл https://drive.google.com/file/d/1zNzWPjNdMGi6_r8gya_iGctDaUChEoPK/view 
** Данные в новом файле должны быть упорядочены по возрастанию ip - как строковое значение.
"""

import re

LOG_FILE = "app.log"
ERR_FILE = "errors.log"
LOG_RE = re.compile(r'(((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?))(\s)(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}[.]\d{6})\s(\[\w+\])\s-\s(AppLog:)\s(.*$)')

def create_list(log_file):
    date_list = list()
    with open(log_file) as f:
        for line in f:
            if line.__contains__("[ERROR]"):
                date_list.append(line)
        return date_list

# def parser(err_file,lst):
#     with open(err_file, "w") as f:
#         for elem in lst:
#             try:
#                 line = LOG_RE.search(elem)
#                 ip = line.group(1)
#                 datetime = line.group(6)
#                 err_text = line.group(9)
#                 f.write(f"{ip} {datetime} {err_text}\n")
#             except AttributeError as e:
#                 print(e)
#                 continue

def parser(lst):
    err_lst = list()
    for elem in lst:
        try:
            line = LOG_RE.search(elem)
            ip = line.group(1)
            datetime = line.group(6)
            err_text = line.group(9)
            err_lst.append([ip,datetime,err_text])
            err_lst.sort(key=lambda elem: elem[0])
        except AttributeError as e:
            print(e)
            continue
    return err_lst

def write_file(err_file, err_lst):
    with open(err_file, "w") as f:
        for elem in err_lst:
            f.write(f"{elem[0]} {elem[1]} {elem[2]}\n")

lst = create_list(LOG_FILE)
err_lst = parser(lst)
write_file(ERR_FILE, err_lst)