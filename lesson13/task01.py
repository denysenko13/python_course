"""
Попросите пользователя ввести имя файла. Поддерживаемые расширения - txt, log, py. 
Если введено неподдерживаемое расширение, кидать исключение. 
Если введенный файл не существует, кидать исключение. 
Подсчитать количество слов в файле.
def verify_file(file_name): pass  # проверка разрешения и существования файла, райзинг исключений , если что-то не так
def calc_words(): pass  # в тексте функции calc_words вызываем функцию проверки файла verify_file
words_count = calc_words()
print(words_count)
"""

import os.path

filename = input("Enter filename: ")

def verify_file(file_name):
    if not file_name.endswith(('.txt','.log','.py')):
        raise Exception("Incorrect type")
    if not os.path.exists(file_name):
        raise Exception("File not found")

def calc_words():
    verify_file(filename)
    words = list()
    with open(filename) as f:
        for line in f:
            words += (line.split(" "))
    return len(words)

print(calc_words())
