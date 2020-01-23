"""
Переделать функцию greeting из примера слайда 6, добавить передачу
параметра lang. Если передан lang == ru - печатать приветствие на русском и
возвращать строку приветствия в качестве результата, en - на английском и
возвращать строку приветствия. Если же неизвестный язык - отображать
текст ошибки выход из функции.
Сделать вызов функции greeting с различными аргументами.
"""

def greeting(name, lang="en"):
    if not name:
        return "Hello everybody!"
    elif lang == "ru":
        return f"Привет {name}!"
    elif lang == "en":
        return f"Hello {name}!"
    else:
        return f"Unknown language"

print(greeting("me", "en"))
print(greeting("вам", "ru"))
print(greeting("me", "uk"))
print(greeting(None))