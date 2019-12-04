"""
5. ** Попросите пользователя ввести имя файла. Поддерживаемые расширения - txt, log, py. 
Если введено неподдерживаемое расширение, отображать ошибку. 
Подсчитать количество слов в файле, предварительно убедившись, что файл существует с помощью функции модуля os, os.path.exists. 
Если файл не существует, отображать ошибку
Пример использования функции
import os
print(‘Файл test.txt существует?: ’, os.path.exists(‘test.txt’))
"""

import os

filename = input("Enter some filename with extension: ")
ext = (".txt",".log",".py")
if filename.endswith(ext):
    words = 0
    if os.path.exists(filename):
        with open(filename) as file:
            for line in file:
                lst = line.split()
                words += len(lst)
        print("Count of the words in the entered file:", words)
    else:
        print("Entered filename not found")
else:
    print("Entered extension of the filename is incorrect")

