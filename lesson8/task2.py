"""
Написать в редакторе скрипт, который предлагает пользователю ввести произвольное число.
А затем просить пользователя указать, в каком представлении вывести число - бинарном, 8-миричном, 16-ричном.
Если введена буква b или В - в бинарном. Если o, O - 8-миричном, h или H - 16-ричном. 
Если ни один из вариантов - сообщение об ошибке, Укажите желаемый формат - h, H или b, B или o, O.
В конце работы скрипта выводить на печать текст - До свидания!
Обратите внимание на отступы! Текст До свидания должен выводиться при любых условиях.
** для тех кто сделал задание 2, написать второй вариант скрипта - реализация с помощью словаря. либо другой вариант, свой выбор.

Реализовать проверку введенной литеры в трех варианта - upper, lower, и через оператор in. 
Также реализовать его через словарь, а возможно придумать и еще один вариант реализации.
"""

num = int(input("Enter some number: "))
present = input("Enter b|B or o|O or h|H: ")
num_keys = dict(b=bin(num),o=oct(num),h=hex(num))

if present in ("b", "B"):
    print(f"bin: {bin(num)}")
elif present in ("o", "O"):
    print(f"oct: {oct(num)}")
elif present in ("h", "H"):
    print(f"hex: {hex(num)}")
else:
    print("Invalid input")

if present.upper() == "B":
    print(f"bin: {bin(num)}")
elif present.upper() == "O":
    print(f"oct: {oct(num)}")
elif present.upper() == "H":
    print(f"hex: {hex(num)}")
else:
    print("Invalid input")

print(f"Dictionary type for ** task: {num_keys.get(present.lower(), 'Invalid input')}")

print("Goodbye")