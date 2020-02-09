"""
Переделать скрипт из задания #1, а именно добавить возможность вводить
float и проверять через try-except, что введено число.
Если пользователь ввел некорректное число или представление, то просить
его ввести опять, пока не введет корректное значение.
(То есть по сути, поменять код функций get_number и get_presentation)
"""

def get_number():
    need_continue = True
    while need_continue:
        try:
            num = int(input("Enter number: "))
        except ValueError as e:
            print(e)
        else:
            need_continue = False
    return num
    
        
def get_presentation():
    need_continue = True
    while need_continue:
        try:
            pres = getattr(__builtins__, input("Enter hex, bin or oct: "))
        except AttributeError as e:
            print(e)
        else:
            need_continue = False
    return pres

number = get_number()
presentation = get_presentation()
print(presentation(number))