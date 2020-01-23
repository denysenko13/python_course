"""
Переписать функцию greeting(name, lang, msg) с использованием
именованных аргументов переменной длины. Добавить проверку, что
переданы нужные аргументы, с нужными именами
"""

def greeting(**kwargs):
    if "msg" in kwargs:
        msg = None
        name = None
        lang = None
        for k, v in kwargs.items():
            if k == "msg":
                msg = v
            elif k == "name":
                name = v
            elif k == "lang":
                lang = v
        if not name:
            return msg
        elif lang == "ru":
            return f"{msg} {name}!"
        elif lang == "en":
            return f"{msg} {name}!"
        else:
            return f"Unknown language"

print(greeting(msg="Hello" ,name="me", lang="en"))
print(greeting(msg="Привет", name="вам", lang="ru"))
print(greeting(msg="Привет", name="me", lang="uk"))
print(greeting(msg="Hello everybody!"))