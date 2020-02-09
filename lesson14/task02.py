"""
Переписать игру Угадай число с помощью механизма исключений. 
В коде указан пример, как создавать собственные исключения. 
https://gist.github.com/kryskaks/881e9b8f04bda87e2e7acd5808e11618. 
Затем достаточно просто делать raise ValueTooBig(), где необходимо. 
Необходимо будет как разить исключения, так и обрабатывать их.
"""

from random import randint

SECRET = randint(1, 20)

# class ValueTooBig(ValueError):
#     '''raise it when input number is too big'''
#     pass
# class ValueTooSmall(ValueError):
#     '''raise it when input number is too small'''
#     pass

"""
сделал исключения через класс Error, 
потому что через ValueError программа по логике отрабатывала корректно,
но не печатался текст ошибки, а выводилась просто пустая строка.
"""
class Error(Exception):
    pass
class ValueTooBig(Error):
    pass
class ValueTooSmall(Error):
    pass

def game():
    need_continue = True
    while need_continue:
        try:
            num = int(input("Enter number: "))
            if num > SECRET:
                raise ValueTooBig
            elif num < SECRET:
                raise ValueTooSmall
        except ValueError as e:
            print(e)
        except ValueTooBig:
            print("Your number is more than secret")
        except ValueTooSmall:
            print("Your number is less than secret")
        else:
            if num == SECRET:
                need_continue = False
                print("Congratulations!")


game()
