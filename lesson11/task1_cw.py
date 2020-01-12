'''
Написать с использованием бесконечного цикла скрипт, который выбирает случайный вопрос из списка вопросов, 
задает его пользователю и делает это пока пользователь не введет ‘stop’ или не нажмет Ctrl+C.
Для случайного выбора вопросов из списка, воспользуйтесь функцией random.choice
'''

import random

questions = ["How are you?", "How old are you?", "What's your name?"]

answer = ""
while answer != "stop":
    print(random.choice(questions))
    answer = input("Write your answer: ")