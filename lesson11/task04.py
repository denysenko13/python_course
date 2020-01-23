"""
Прочитать информацию из файла, в котором содержится тест дзен python
(предварительно сформировать файл, вручную скопировав текст дзен из интерпретатора). 
Упорядочить все слова из этого файла в порядке возрастания длины слова. 
То есть результирующий список слов будет иметь примерно такой вид: ['a', 'a', 'of', 'by', 'is', 'is', 'is' …  'implementation', 'implementation’]. 
Подсказка, необходимо при вызове метода sort или функции sorted указывать аргумент key. 
https://docs.python.org/3/library/functions.html#sorted, https://docs.python.org/3/library/stdtypes.html#list.sort
"""

import string

WHITESPACES_LiST = list(string.whitespace)
PUNCTUATIONS_LIST = list(string.punctuation)
zen_file = "python_zen.txt"
words = list()

with open(zen_file) as file:
    for line in file:
        words += (line.split(" "))
strips = WHITESPACES_LiST + PUNCTUATIONS_LIST
for i in strips:
    words = [word.strip(i) for word in words]

words = [word for word in words if word != ""]
words.sort(key=len)
print(words)

