"""
Переделать функцию greeting из примера слайда 6, добавить передачу
параметра msg - текст приветствия. Также добавить параметр по умолчанию
name=None.
Сделать вызов функции greeting с различными аргументами в различных
вариантах.
"""

def greeting(msg, name=None, lang="en"):
    if not name:
        return msg
    elif lang == "ru":
        return f"{msg} {name}!"
    elif lang == "en":
        return f"{msg} {name}!"
    else:
        return f"Unknown language"

print(greeting("Hello" ,"me", "en"))
print(greeting("Привет", "вам", "ru"))
print(greeting("Привет", "me", "uk"))
print(greeting("Hello everybody!"))