"""
Написать скрипт, lesson1_hw01.py, который будет спрашивать, как зовут пользователя, выводить на экран Hello, (имя из ответа)! 
Затем спрашивать про возраст пользователя. 
И в конце выводить суммарную информацию, Your name - (имя из ответа), your age - (возраст из ответа). И затем выводить - You are lucky Guy!
"""

name = input("Q: What's your name?\nA: ")
print("Hello, %s!" %(name,))
age = input("Q: How old are you?\nA: ")
print("Your name - %s, your age - %s.\nYou are lucky Guy!" %(name, age,))