"""
Есть список функций funcs. Необходимо выводить пользователю информацию (doc-строку) по каждой функции, 
выбирая ее случайным образом до тех пор, пока пользователь либо не введет ’stop’ или не закончатся все функции. 
Отображать информацию о функции и ожидать ввода пользователем чего-либо. 
Код для формирования списка функций funcs (просто скопируйте его в свой скрипт):
lst = dir(__builtins__)[80:] 
lst.remove('copyright')
  lst.remove('credits') 
 funcs = [getattr(__builtins__, attr) for attr in lst]
"""

import random

lst = dir(__builtins__)[80:] 
lst.remove('copyright')
lst.remove('credits') 
funcs = [getattr(__builtins__, attr) for attr in lst]
random.shuffle(funcs)


text = ""
for i in funcs:
    text = input("Enter stop for \"stop\" program or enter some text for continue: ")
    if text == "stop":
      break
    print("\n", i.__doc__, "\n")