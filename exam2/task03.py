"""
Написать функцию nickname, которая генерирует кличку. 
Есть два списка 
animals = ['puppy', 'piggy', 'frog', 'kitty', 'tiger', 'monkey', 'catfish', 'duck', 'eagle', 'hen'] , 
adjs = ['ugly', 'smart', 'pretty', 'curious', 'foolish', 'charming', 'smelly', 'treacherous', 'messy', 'funny']. 
В качестве результата, функция возвращает случайные клички вида: ‘charming-eagle’, 'curious-duck' и тп. 
Реализовать вызов функции и печать результата. 
"""

import random

animals = ['puppy', 'piggy', 'frog', 'kitty', 'tiger', 'monkey', 'catfish', 'duck', 'eagle', 'hen']
adjs = ['ugly', 'smart', 'pretty', 'curious', 'foolish', 'charming', 'smelly', 'treacherous', 'messy', 'funny']

def nickname(adjs=adjs, animals=animals):
    random.shuffle(animals)
    random.shuffle(adjs)
    nicks = list()
    for i in range(len(adjs)):
        nicks.append(f"{adjs[i]}-{animals[i]}")
    return nicks

print(nickname())